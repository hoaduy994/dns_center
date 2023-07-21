from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('dnsnode', views.dnsnode, name='dnsnode'),
    path('login', views.login_, name='login_dns_center'),
    path('dnsnode/<str:id>', views.dnsnodedetail, name='dnsnodedetail'),
    path('whitelist', views.whitelist, name='whitelist'),
    path('blacklist', views.blacklist, name='blacklist'),
    path('dnsfilter', views.dnsfilter, name='dnsfilter'),
    path('usermanagement', views.usermanagement, name='usermanagement'),
    path('dnsrecord', views.dnsrecord, name='dnsrecord'),
    path('indexqueries', views.indexqueries, name='indexqueries'),
    path('dashboarddata', views.dashboarddata, name='dashboarddata'),
    path('dnsnodedata', views.dnsnodedata, name='dnsnodedata'),
    path('delwhitelist', views.delwhitelist, name='delwhitelist'),
    path('delblacklist', views.delblacklist, name='delblacklist'),
    path('deldnsfilter', views.deldnsfilter, name='deldnsfilter'),
    path('deluser', views.deluser, name='deluser'),
    path('updateuser', views.updateuser, name='updateuser'),
    path('createuser', views.createuser, name='createuser'),
    path('rawblacklist/<uuid:id>', views.raw_black_list, name='rawblacklist'),
    path('rawregexblack/<uuid:id>', views.raw_regex_black, name='rawregexblack'),
    path('rawwhitelist/<uuid:id>', views.raw_white_list, name='rawwhitelist'),
    path('rawregexwhite/<uuid:id>', views.raw_regex_white, name='rawregexblack'),
    path('rawdnsrecords/<uuid:id>', views.raw_dns_records, name='rawdnsrecords'),
    path('rawdnsforwarder/<uuid:id>', views.raw_dns_forwarder, name='rawdnsforwarder'),
    path('deldnsrecord', views.deldnsrecord, name='deldnsrecord'),
    path('deldnsforwarder', views.deldnsforwarder, name='deldnsforwarder'),
    path('chartdnsdetail', views.chartdnsdetail, name='chartdnsdetail'),
    path('getonedomain/<str:id>', views.get_one_domain, name='getonedomain'),
    path('log', views.log, name='log'),
    path('datalog', views.datalog, name='datalog'),
    path('getipsiemtoweb', views.getipsiemtoweb, name='getipsiemtoweb'),
    path('searchtime', views.searchtime, name='searchtime'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
