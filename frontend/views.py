from multiprocessing import context
import pprint
from re import search
from django.shortcuts import redirect
from django.shortcuts import render
from django.db import connection
from django.views.decorators.csrf import csrf_protect
from main_part.models import DnsRecordsModel, DnsForwarderModel,IpSiemToWeb
from django.db.models import Q
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from datetime import datetime, timedelta, date
from . import tasks
from nosql.connect import connect
import json
from .views_split import (dashboard, dns_node,
                          white_list, black_list,
                          dns_filter, user_management,
                          dns_record,search_time)
# Create your views here.


def login_(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Sai thông tin đăng nhập')
            return render(request, 'frontend/login.html')

    return render(request, 'frontend/login.html')


@login_required(login_url='login_dns_center')
def index(request):
    return dashboard.main(request=request)


@login_required(login_url='login_dns_center')
def indexqueries(request):
    return dashboard.index_queries_split(request=request)


@login_required(login_url='login_dns_center')
def dashboarddata(request):
    return dashboard.dashboard_data_split(request=request)


@login_required(login_url='login_dns_center')
def dnsnode(request):
    return render(request, 'frontend/dnsnode.html')


@login_required(login_url='login_dns_center')
def dnsnodedata(request):
    return dns_node.dnsnode_data_split(request=request)


@login_required(login_url='login_dns_center')
def dnsnodedetail(request, id):
    return dns_node.dnsnodedetail_split(request=request, id=id)


@login_required(login_url='login_dns_center')
def chartdnsdetail(request):
    return dns_node.chartdnsdetail_split(request=request)


@login_required(login_url='login_dns_center')
@csrf_protect
def deldnsforwarder(request):
    return dns_node.deldnsforwarder_split(request=request)


@login_required(login_url='login_dns_center')
@csrf_protect
def whitelist(request):  
    return white_list.whitelist_split(request=request)


@login_required(login_url='login_dns_center')
@csrf_protect
def delwhitelist(request):
    return white_list.delwhitelist_split(request=request)


@login_required(login_url='login_dns_center')
@csrf_protect
def blacklist(request):
    return black_list.blacklist_split(request=request)


@login_required(login_url='login_dns_center')
@csrf_protect
def delblacklist(request):
    return black_list.delblack_list_split(request=request)


@login_required(login_url='login_dns_center')
@csrf_protect
def dnsfilter(request):
    return dns_filter.dns_filter_split(request=request)


@login_required(login_url='login_dns_center')
@csrf_protect
def deldnsfilter(request):
    return dns_filter.deldns_filter_split(request=request)


@login_required(login_url='login_dns_center')
def usermanagement(request):
    return user_management.user_management_split(request=request)

#######################deluser#######################


@login_required(login_url='login_dns_center')
@csrf_protect
def deluser(request):
    return user_management.deluser(request=request)

#######################updateuser#######################


@login_required(login_url='login_dns_center')
@csrf_protect
def updateuser(request):
    return user_management.updateuser(request=request)
########################createuser########################


@login_required(login_url='login_dns_center')
@csrf_protect
def createuser(request):
    return user_management.createuser(request=request)


@login_required(login_url='login_dns_center')
def dnsrecord(request):
    return dns_record.dnsrecord_split(request=request)


@login_required(login_url='login_dns_center')
def deldnsrecord(request):
    return dns_record.deldnsrecord(request=request)


@login_required(login_url='login_dns_center')
def testuser(request):
    return render(request, 'frontend/test_user.html')


def raw_black_list(request, id):
    cursor = connection.cursor()
    raw_query_dnsfilter = f"""
        SELECT "data_domain"
        FROM "main_part_black_list_models"
        WHERE (("add_dns" like '%{id}%')
        AND "type" = '1')
        LIMIT 1048575
        """
    cursor.execute(raw_query_dnsfilter)
    a = cursor.fetchall()
    data_domains = []
    for row in a:
        data_domains.append({'data_domain': row[0]})
    return render(request, 'frontend/raw_black_list.html', {'orm_get_all_blacklist': data_domains})


def raw_regex_black(request, id):
    cursor = connection.cursor()
    raw_query_dnsfilter = f"""
        SELECT "data_domain"
        FROM "main_part_black_list_models"
        WHERE (("add_dns" like '%{id}%')
        AND "type" = '3')
        LIMIT 1048575
        """
    cursor.execute(raw_query_dnsfilter)
    a = cursor.fetchall()
    data_domains = []
    for row in a:
        data_domains.append({'data_domain': row[0]})
    return render(request, 'frontend/raw_black_list.html', {'orm_get_all_blacklist': data_domains})


def raw_white_list(request, id):
    cursor = connection.cursor()
    raw_query_dnsfilter = f"""
        SELECT "data_domain"
        FROM "main_part_white_list_models"
        WHERE (("add_dns" like '%{id}%')
        AND "type" = '0')
        LIMIT 1048575
        """
    cursor.execute(raw_query_dnsfilter)
    a = cursor.fetchall()
    data_domains = []
    for row in a:
        data_domains.append({'data_domain': row[0]})
    return render(request, 'frontend/raw_black_list.html', {'orm_get_all_blacklist': data_domains})


def raw_regex_white(request, id):
    cursor = connection.cursor()
    raw_query_dnsfilter = f"""
        SELECT "data_domain"
        FROM "main_part_white_list_models"
        WHERE (("add_dns" like '%{id}%')
        AND "type" = '2')
        LIMIT 1048575
        """
    cursor.execute(raw_query_dnsfilter)
    a = cursor.fetchall()
    data_domains = []
    for row in a:
        data_domains.append({'data_domain': row[0]})
    return render(request, 'frontend/raw_black_list.html', {'orm_get_all_blacklist': data_domains})


def raw_dns_records(request, id):
    orm_get_dns_records = DnsRecordsModel.objects.filter(
        Q(add_dns__icontains=id))
    return render(request, 'frontend/raw_dns_records.html', {'dns_records': orm_get_dns_records})


def raw_dns_forwarder(request, id):
    orm_get_dns_forward = DnsForwarderModel.objects.filter(
        Q(add_dns__icontains=id))
    return render(request, 'frontend/raw_dns_forwarder.html', {'dns_forwarder': orm_get_dns_forward})


def get_one_domain(request, id):
    f = open("nosql/nosql_json/top_domain.json")
    top_domain = json.load(f)
    top_domain_allowed = top_domain['top_domain']['Top_Domain_Blocked']
    top_domain_blocked = top_domain['top_domain']['Top_Domain_Allowed']
    for item in top_domain_allowed:
        if item['domain'] == id:
            data_domain = item
    for item in top_domain_blocked:
        if item['domain'] == id:
            data_domain = item

    results = {
        'sum_count': data_domain['count'],
        'domain_day': data_domain['domain_day']['domain_day'],
        'domain': id
    }
    return render(request, 'frontend/domaininformation.html', results)


def log(request):
    return render(request, 'frontend/log.html')


def datalog(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'GET':
            context={}
            try:
                today = datetime.today().strftime("%Y-%m-%d")
                infile = r"/var/log/dns-sinkhole/" + today +".log"
                results = []

                with open(infile) as f:
                    f = f.readlines()[-100:]

                k = 0
                for line in f:
                    date = line[0:20]
                    data = line[22:]
                    log = {
                        'date': date,
                        'data': data
                    }
                    results.append(log)
                    k += 1
                    if k == 100:
                        break

                results.reverse()
                context = {
                    'results': results
                }
            except:
                pass
        return JsonResponse(context, status=200)
    else:
        return HttpResponseBadRequest('Invalid request')

def getipsiemtoweb(request):
    cursor = connect()
    if request.method == 'POST':
        ip=request.POST.get('ip')
        port=request.POST.get('port')
        saveipport = IpSiemToWeb(ip_siem=ip, port_siem=port)
        try:
            saveipport.save()
            tasks.taskgetipsiemtoweb.delay(ip_siem=ip, port_siem=port)
        except:
            pass
        return redirect('index')
    raw_getipsiemtoweb = '''
    SELECT "public"."main_part_ipsiemtoweb"."ip_siem" AS "ip_siem", "public"."main_part_ipsiemtoweb"."port_siem" AS "port_siem", "public"."main_part_ipsiemtoweb"."is_connect" AS "is_connect"
    FROM "public"."main_part_ipsiemtoweb"
    ORDER BY "public"."main_part_ipsiemtoweb"."update_time" DESC
    LIMIT 1
    '''
    cursor.execute(raw_getipsiemtoweb)
    total_queries = cursor.fetchall()
    for query in total_queries:
        ip_siem=query[0]
        port_siem=query[1]
        is_connect=query[2]
    context = {
        'ip_siem': ip_siem,
        'port_siem': port_siem,
        'is_connect': is_connect
    }
    return render(request, 'frontend/getipsiemtoweb.html', context)

    
@login_required(login_url='login_dns_center')
def searchtime(request):
    return search_time.main(request=request)
