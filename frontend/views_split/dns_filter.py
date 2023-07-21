from django.shortcuts import redirect
from django.shortcuts import render
from django.db import connection
from main_part.models import (DNS_filter_Models)
from frontend import tasks
from django.contrib.auth.decorators import login_required

@login_required(login_url='login_dns_center')
def dns_filter_split(request):
    dns_filter = []
    cursor = connection.cursor()
    raw_query_dnsfilter = """
            SELECT "title", "data_domain", "add_dns","count", "id"
            FROM "main_part_dns_filter_models"
            ORDER BY "create_time" DESC
            LIMIT 100
        """
    cursor.execute(raw_query_dnsfilter)
    a = cursor.fetchall()
    id_dnss = []
    for row in a:
        id = row[4]
        title = row[0]
        data_domain = row[1]
        count = row[3]
        id = row[4]
        # add_dns.append(row[2])
        id_dnss = row[2].split(", ")
        id_dns = []
        hostname = []
        ip_address = []
        try:
            for i in id_dnss:
                raw_query_dns = f"""
                        SELECT "hostname","ip_address","id"
                        FROM "main_part_dns_node_models"
                        WHERE "id" = '{i}'::uuid
                        LIMIT 1048575
                    """
                cursor.execute(raw_query_dns)
                query_dns = cursor.fetchall()
                id_dns.append(str(query_dns[0][2]))
                hostname.append(query_dns[0][0])
                ip_address.append(query_dns[0][1])

        except:
            pass
        dns_filter.append({'title': title,
                           'data_domain': data_domain,
                           'add_id_dns': id_dnss,
                           'ip_dns': ip_address,
                           'name_dns': hostname,
                           'id_dnss': id_dns,
                           'count': count,
                           'id': str(id)
                           })

    ################################
    dns_node = []
    raw_query_dns_node = """
    SELECT "hostname", "ip_address", "id"
    FROM "public"."main_part_dns_node_models"
    LIMIT 1048575
    """
    cursor.execute(raw_query_dns_node)
    a = cursor.fetchall()
    for row in a:
        dns_node.append({'hostname': row[0],
                        'ip': row[1],
                         'id': row[2]})

    context = {
        'dns_node': dns_node,
        'dns_filter': dns_filter
    }
####################################################################

    if request.method == 'POST':
        dnsname = request.POST.get('dnsname')
        domain = request.POST.get('domain')
        add_dns = request.POST.getlist('id')
        #check id add dns#############################
        list_add_dns = ""
        for i in add_dns:
            list_add_dns += i+", "
        data_post_dns_filter = DNS_filter_Models(title=domain,
                                                 data_domain=dnsname,
                                                 add_dns=list_add_dns)
        # sửa đổi do_not_add_dns thành list_add_dns
        tasks.DNS_filter_List_View.delay(title=domain,
                                         data_domain=dnsname,
                                         list_add_dns=list_add_dns)
        data_post_dns_filter.save()

        return redirect('dnsfilter')

    return render(request, 'frontend/dnsfilter.html', context)

@login_required(login_url='login_dns_center')
def deldns_filter_split(request):
    cursor = connection.cursor()
    if request.method == 'POST':
        idIp = request.POST.getlist('idIp')
        id = request.POST.get('id')
        arr_deldnsfilter = ''
        for row in idIp:
            arr_deldnsfilter += f"{row}, "
        raw_query_deldnsfilter = f"""
            UPDATE main_part_dns_filter_models
            SET delete_dns = '{arr_deldnsfilter}'
            WHERE id = '{id}';
        """
        cursor.execute(raw_query_deldnsfilter)
    return redirect('dnsfilter')