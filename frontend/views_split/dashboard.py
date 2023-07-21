import imp
from multiprocessing import context
import pprint
from unicodedata import name
from django.shortcuts import render
from django.db import connection
from django.urls import is_valid_path
from main_part.models import Dns_Node_Models
from datetime import datetime, timedelta
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import json


@login_required(login_url='login_dns_center')
def main(request):
    context={}
    try:
        f = open("nosql/nosql_json/dashboard.json")
        f2 = open("nosql/nosql_json/top_domain.json")
        data = json.load(f)
        top_domain = json.load(f2)
        context = {
            'data': data,
            'top_domain': top_domain,
            'hover_domain_blocked': top_domain['top_domain']['Top_Domain_Blocked'][0]['domain_day']['domain_day'][:7],
            'hover_domain_allowed': top_domain['top_domain']['Top_Domain_Allowed'][0]['domain_day']['domain_day'][:7]
        }
    except:
        pass
    return render(request, 'frontend/dashboard.html', context)


@login_required(login_url='login_dns_center')
def dashboard_data_split(request):
    data={}
    try:
        f = open("nosql/nosql_json/char_dashboard.json")
        data = json.load(f)
    except:
        pass
    return JsonResponse(data, status=200)


@login_required(login_url='login_dns_center')
def index_queries_split(request):
    data={}
    try:
        f = open("nosql/nosql_json/index_queries.json")
        data = json.load(f)
    except:
        pass
    return JsonResponse(data, status=200)
