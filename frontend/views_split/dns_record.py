
from django.shortcuts import redirect
from django.shortcuts import render
from main_part.models import ( Dns_Node_Models,
                               DnsRecordsModel)
from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required(login_url='login_dns_center')
def dnsrecord_split(request):
    orm_query_dnsrecord = DnsRecordsModel.objects.all()
    dnsrecord = []
    for row in orm_query_dnsrecord:
        add_host_name = []
        id_dns = []
        ip_address = []
        del_dnsrecord = []
        id_dnsrecord = row.id
        Domain = row.domian
        add_dns = row.add_dns
        ip = row.ip

        for row in (row for row in add_dns.split(", ") if row != ""):
            try:
                orm_query_dns = Dns_Node_Models.objects.filter(Q(id=row))
                for client_dns in orm_query_dns:
                    id_dns.append(str(client_dns.id))
                    add_host_name.append(str(client_dns.hostname))
                    ip_address.append(client_dns.ip_address)
                del_dnsrecord.append(str(row))
            except:
                pass

            dnsrecord.append({'id': id_dnsrecord,
                              'domian': Domain,
                              'ip': str(ip),
                              'add_dns': del_dnsrecord,
                              'dns_node_name': add_host_name,
                              'dns_node_ip': ip_address
                              })
    dns_node_arr = []
    orm_query_dns_node = Dns_Node_Models.objects.all()
    for dns_node in orm_query_dns_node:
        dns_node_arr.append({'hostname': dns_node.hostname,
                             'ip': dns_node.ip_address,
                             'id': dns_node.id})

    context = {
        'dns_record_arr': dnsrecord,
        'dns_node_arr': dns_node_arr,
    }
    #########################################
    if request.method == 'POST':
        domain = request.POST.get('domain')
        ip_address = request.POST.get('ip_address')
        id_node = request.POST.getlist('id')
        arr_id_node = ""
        for row in id_node:
            arr_id_node += row+", "
        save_dnsrecord = DnsRecordsModel(domian=domain,
                                         ip=ip_address,
                                         add_dns=arr_id_node
                                         )
        save_dnsrecord.save()
        for dns_add in (dns_add for dns_add in arr_id_node.split(", ") if dns_add != ""):
            Dns_Node_Models.objects.filter(
                Q(id=dns_add)).update(is_dns_dnsrecord=False)
        return redirect('dnsrecord')
    return render(request, 'frontend/dnsrecord.html', context)


@login_required(login_url='login_dns_center')
def deldnsrecord(request):
    if request.method == 'POST':
        idIp = request.POST.getlist('idNode')
        id = request.POST.get('id')
        arr_deldnsfilter = ''
        for row in idIp:
            deldnsrecord = DnsRecordsModel.objects.get(pk=id)
            deldnsrecord.add_dns = deldnsrecord.add_dns.replace(row, '')
            deldnsrecord.save()
            Dns_Node_Models.objects.filter(
                Q(id=row)).update(is_dns_dnsrecord=False)
        return redirect('dnsrecord')