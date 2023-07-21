from pickletools import pyint
from django.http import Http404
import pprint
from django.shortcuts import redirect
from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_protect
from main_part.models import (DNS_filter_Models, Dns_Node_Models,
                              Black_List_Models, DnsRecordsModel,
                              Log_Detail_Models, White_List_Models,
                              DnsForwarderModel)
from accounts.models import CustomUser
from django.db.models import Q, Count
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime, timedelta

@login_required(login_url='login_dns_center')
def user_management_split(request):
    user_management = []
    users = CustomUser.objects.all().order_by('-id')
    rule = ''
    for user in users:
        userId = user.id
        email = user.email
        username = user.username
        name = user.first_name+" "+user.last_name
        if user.is_admin:
            rule = 'Admin'
        elif user.is_super:
            rule = 'Super'
        else:
            rule = 'User'
        user_management.append({
            'id': userId,
            'email': email,
            'rule': rule,
            'username': username,
            'name': name,
            'firstName': user.first_name,
            'lastName': user.last_name
        })
    context = {
        'context': user_management
    }

    return render(request, 'frontend/usermanagement.html', context)

@login_required(login_url='login_dns_center')
def deluser(request):
    is_user_admin = request.user.is_admin
    if (request.method == 'POST' and is_user_admin == True):
        username = request.POST.get('id')
        u = CustomUser.objects.get(username=username)
        u.delete()
        print('Delete thành công', id)
    return redirect('usermanagement')

#######################updateuser#######################


@login_required(login_url='login_dns_center')
@csrf_protect
def updateuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        rule = request.POST.get('rule')
        u = CustomUser.objects.get(username=username)
        if rule == 'User':
            u.is_user = True
            u.is_active = True
        if rule == 'Super':
            u.is_super = True
            u.is_active = True
            u.is_staff = True
        if rule == 'Admin':
            u.is_admin = True
            u.is_active = True
            u.is_staff = True
            u.is_superuser = True
        u.save()
    return redirect('usermanagement')
########################createuser########################


@login_required(login_url='login_dns_center')
@csrf_protect
def createuser(request):
    is_user_admin = request.user.is_admin
    if (request.method == 'POST' and is_user_admin == True):
        email = request.POST.get('emailCreateUser')
        username = request.POST.get('userNameCreateUser')
        firstname = request.POST.get('firstNameCreateUser')
        lastname = request.POST.get('lastNameCreateUser')
        password = request.POST.get('passwordCreateUser')
        confirm = request.POST.get('passwordConfirmationCreateUser')
        rule = str(request.POST.get('roleCreate'))
        if (CustomUser.objects.filter(username=username).exists() == False and password == confirm):
            if rule == 'User':
                user = CustomUser.objects.create_user(username=username,
                                                      first_name=firstname,
                                                      last_name=lastname,
                                                      email=email,
                                                      password=password,
                                                      is_user=True,
                                                      is_active=True)
            if rule == 'Super':
                user = CustomUser.objects.create_user(username=username,
                                                      first_name=firstname,
                                                      last_name=lastname,
                                                      email=email,
                                                      password=password,
                                                      is_super=True,
                                                      is_active=True,
                                                      is_staff=True)
            if rule == 'Admin':
                user = CustomUser.objects.create_user(username=username,
                                                      first_name=firstname,
                                                      last_name=lastname,
                                                      email=email,
                                                      password=password,
                                                      is_admin=True,
                                                      is_active=True,
                                                      is_staff=True,
                                                      is_superuser=True)
            user.save()
            print('Tạo user', username)
        else:
            print('user đã tồn tại hoặc sai mật khẩu', username)
        return redirect('usermanagement')
    else:
        return HttpResponse("Không Phải ADMIN")