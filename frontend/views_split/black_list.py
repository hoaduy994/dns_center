from django.shortcuts import render
from main_part.models import (Dns_Node_Models,
                              Black_List_Models)
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from ..form import FormSearchBlacklist
from django.http import HttpResponseRedirect


@login_required(login_url='login_dns_center')
def blacklist_split(request):
    form = FormSearchBlacklist()
    blacklist_ = []
    # orm_get_all_blacklist = Black_List_Models.objects.all().order_by('add_dns').exclude(add_dns=", ")
    if request.method == 'GET':
        form = FormSearchBlacklist(request.GET)
        if form.is_valid():
            domain = form.cleaned_data['domain']
            orm_get_all_blacklist = Black_List_Models.objects.filter(
                data_domain__icontains=domain).order_by('add_dns').exclude(add_dns=", ").exclude(add_dns="")
        
    paginator = Paginator(orm_get_all_blacklist, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    for blacklist in paginator.page(page_number):
        add_host_name = []
        id_dns = []
        ip_address = []
        id_blacklist = blacklist.id
        Domain = blacklist.data_domain
        Type = blacklist.type
        Add_dns = blacklist.add_dns
        Title = blacklist.title
        id_dnss = Add_dns.split(", ")
        for row in (row for row in id_dnss if row != ""):
            try:
                orm_query_dns = Dns_Node_Models.objects.filter(Q(id=row))
                for client_dns in orm_query_dns:
                    id_dns.append(str(client_dns.id))
                    add_host_name.append(str(client_dns.hostname))
                    ip_address.append(str(client_dns.ip_address))
            except:
                pass
        if (len(ip_address) != 0):
            blacklist_.append({'domain': Domain,
                               'type': Type,
                               'add_dns': add_host_name,
                               'title': Title,
                               'ip_address': ip_address,
                               'id_dnss': id_dns,
                               'id_blacklist': str(id_blacklist)})

    dns_node_arr = []
    orm_query_dns_node = Dns_Node_Models.objects.all()
    for dns_node in orm_query_dns_node:
        dns_node_arr.append({'hostname': dns_node.hostname,
                             'ip': dns_node.ip_address,
                             'id': dns_node.id})
    context = {
        "blacklist": blacklist_,
        "dns_node": dns_node_arr,
        "page_obj": page_obj,
        'form': form
    }

    #########################
    if request.method == 'POST':
        # type = request.POST.get('type')
        title = request.POST.get('title')
        domain = request.POST.get('domain')
        add_dns = request.POST.getlist('id')
        #check id add dns#############################
        list_add_dns = ""
        for i in add_dns:
            list_add_dns += i+", "

        all_dns_node = Dns_Node_Models.objects.all()
        data_post_blacklist = Black_List_Models(title=title,
                                                data_domain=domain,
                                                add_dns=list_add_dns,
                                                type=type
                                                )
        data_post_blacklist.save()
        if type == "1":
            for dns_add in (dns_add for dns_add in list_add_dns.split(", ") if dns_add != ""):
                Dns_Node_Models.objects.filter(
                    Q(id=dns_add)).update(is_raw_black_list=False)
            return HttpResponseRedirect('/blacklist?page=1')

        if type == "3":
            for dns_add in (dns_add for dns_add in list_add_dns.split(", ") if dns_add != ""):
                Dns_Node_Models.objects.filter(
                    Q(id=dns_add)).update(is_raw_regex_black=False)
            return HttpResponseRedirect('/blacklist?page=1')
    return render(request, 'frontend/blacklist.html', context)


@login_required(login_url='login_dns_center')
def delblack_list_split(request):
    if request.method == 'POST':
        idIp = request.POST.getlist('idIp')
        id = request.POST.get('id')
        for row in idIp:
            delblack = Black_List_Models.objects.get(pk=id)
            delblack.add_dns = delblack.add_dns.replace(f'{row}, ', '')
            delblack.save()
            Dns_Node_Models.objects.filter(
                Q(id=row)).update(is_raw_regex_black=False)
            Dns_Node_Models.objects.filter(
                Q(id=row)).update(is_raw_black_list=False)
    return HttpResponseRedirect('/blacklist?page=1')
