from django.shortcuts import render
from main_part.models import (Dns_Node_Models, White_List_Models)
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from ..form import FormSearchWhitelist


@login_required(login_url='login_dns_center')
def whitelist_split(request):
    form = FormSearchWhitelist()
    whitelist = []
    orm_query_whitelist = White_List_Models.objects.all().order_by('-id')
    if request.method == 'GET':
        form = FormSearchWhitelist(request.GET)
        if form.is_valid():
            domain = form.cleaned_data['domain']
            orm_query_whitelist = White_List_Models.objects.filter(data_domain__icontains=domain).order_by('-id')
    paginator = Paginator(orm_query_whitelist, 10)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    whitelist = []
    for row in paginator.page(page_number):
        add_host_name = []
        id_dns = []
        ip_address = []
        id_whitelist = row.id
        Domain = row.data_domain
        Type = row.type
        Add_dns = row.add_dns
        Title = row.title
        id_dnss = Add_dns.split(", ")
        for row in (row for row in id_dnss if row != ""):
            try:
                orm_query_dns = Dns_Node_Models.objects.filter(Q(id=row))
                for client_dns in orm_query_dns:
                    id_dns.append(str(client_dns.id))
                    add_host_name.append(str(client_dns.hostname))
                    ip_address.append(client_dns.ip_address)
            except:
                pass
        if (len(ip_address) != 0):
            whitelist.append({'domain': Domain,
                              'type': Type,
                              'add_dns': add_host_name,
                              'title': Title,
                              'ip_address': ip_address,
                              'id_dnss': id_dns,
                              'id_whitelist': str(id_whitelist)})
    dns_node_arr = []
    orm_query_dns_node = Dns_Node_Models.objects.all()
    for dns_node in orm_query_dns_node:
        dns_node_arr.append({'hostname': dns_node.hostname,
                             'ip': dns_node.ip_address,
                             'id': dns_node.id})
    context = {
        "whitelist": whitelist,
        "dns_node": dns_node_arr,
        "page_obj": page_obj,
        'form': form
    }
    ##########################
    if request.method == 'POST':
        type = request.POST.get('type')
        title = request.POST.get('title')
        domain = request.POST.get('domain')
        add_dns = request.POST.getlist('id')
        #check id add dns#############################
        list_add_dns = ""
        for i in add_dns:
            list_add_dns += i+", "
        data_post_whitelist = White_List_Models(title=title,
                                                data_domain=domain,
                                                add_dns=list_add_dns,
                                                type=type
                                                )
        data_post_whitelist.save()
        if type == "0":
            for dns_add in (dns_add for dns_add in list_add_dns.split(", ") if dns_add != ""):
                Dns_Node_Models.objects.filter(
                    Q(id=dns_add)).update(is_raw_white_list=False)
            return HttpResponseRedirect('/whitelist?page=1')

        if type == "2":
            for dns_add in (dns_add for dns_add in list_add_dns.split(", ") if dns_add != ""):
                Dns_Node_Models.objects.filter(
                    Q(id=dns_add)).update(is_raw_regex_white_list=False)
            return HttpResponseRedirect('/whitelist?page=1')
        return HttpResponseRedirect('/whitelist?page=1')
    return render(request, 'frontend/whitelist.html', context)


@login_required(login_url='login_dns_center')
def delwhitelist_split(request):
    if request.method == 'POST':
        idIp = request.POST.getlist('idIp')
        id = request.POST.get('id')
        for row in idIp:
            delwhite = White_List_Models.objects.get(pk=id)
            delwhite.add_dns = delwhite.add_dns.replace(row, '')
            delwhite.save()
            Dns_Node_Models.objects.filter(
                Q(id=row)).update(is_raw_white_list=False)
            Dns_Node_Models.objects.filter(
                Q(id=row)).update(is_raw_regex_white_list=False)
    return HttpResponseRedirect('/whitelist?page=1')
