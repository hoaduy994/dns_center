import pprint
from traceback import print_tb
from django.http import Http404
from django.shortcuts import redirect
from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from main_part.models import (Dns_Node_Models, DnsForwarderModel)
from django.db.models import Q
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
import json


@login_required(login_url='login_dns_center')
def dnsnode_data_split(request):
    List_of_DNS = []
    raw_query = """
        SELECT "id"
        FROM "main_part_dns_node_models"
        LIMIT 1048575
    """
    cursor = connection.cursor() 
    cursor.execute(raw_query)
    aa = cursor.fetchall()
    for row in aa:
        ip_dns = row[0]
        raw_query = f"""
                SELECT "ram", "cpu", "disk", "status","main_part_monitor_dns_models"."create_time", "Main Part Dns Node Models - Dns Center ID"."hostname", "Main Part Dns Node Models - Dns Center ID"."ip_address", "main_part_monitor_dns_models"."dns_center_id_id"
                FROM "main_part_monitor_dns_models"
                LEFT JOIN "main_part_dns_node_models" "Main Part Dns Node Models - Dns Center ID" ON "dns_center_id_id" = "Main Part Dns Node Models - Dns Center ID"."id"
                WHERE "dns_center_id_id" = '{ip_dns}'::uuid
                ORDER BY "main_part_monitor_dns_models"."create_time" DESC
                LIMIT 1
            """
        cursor = connection.cursor()
        cursor.execute(raw_query)
        a = cursor.fetchone()
        try:
            List_of_DNS.append({'ram': a[0], 'cpu': a[1], 'disk': a[2], 'status': a[3], 'create_time': str(
                a[4]), 'name_dns': a[5], 'ip': a[6], 'id': a[7]})
        except:
            pass
    return JsonResponse({"results": List_of_DNS}, status=200)


@login_required(login_url='login_dns_center')
def dnsnodedetail_split(request, id):
    context={}
    try:
        f = open("nosql/nosql_json/data_dns_node.json")
        data = json.load(f)
        for row in data:
            try:
                context=row[str(id)]
            except:
                pass
    except:
        pass

    # ADD DNS Forwarder
    if request.method == 'POST':
        ip = request.POST.get('ip')
        title = request.POST.get('title')
        id_dnsnode = request.POST.get('id_dnsnode')
        add_dns_forwarder = DnsForwarderModel(ip=ip,
                                            title=title,
                                            add_dns=id_dnsnode )
        add_dns_forwarder.save()
        Dns_Node_Models.objects.filter(
            Q(id=id_dnsnode)).update(is_dns_forwarder=False)
        return redirect(f'/dnsnode/{id}')
    return render(request, 'frontend/dnsdetail.html',context)


@login_required(login_url='login_dns_center') 
def chartdnsdetail_split(request):
    data={}
    try:
        f = open("nosql/nosql_json/char_monitor_pihole.json")
        data = json.load(f)
    except:
        pass
    
    return JsonResponse({"chart": data}, status=200)
 
@login_required(login_url='login_dns_center')   
def deldnsforwarder_split(request):
    if request.method == 'POST':
        id_dnsnode = request.POST.get('idDnsNode')
        id_dnsforward = request.POST.get('idDnsForward')
        query = DnsForwarderModel.objects.get(id=id_dnsforward)
        query.delete()
        return redirect(f'/dnsnode/{id_dnsnode}')