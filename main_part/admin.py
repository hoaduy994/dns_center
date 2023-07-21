from django.contrib import admin
from .models import *

# Register your models here.


class Dns_Node_ModelsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Dns_Node_Models, Dns_Node_ModelsAdmin)

class Black_List_ModelsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Black_List_Models, Black_List_ModelsAdmin)

class White_List_ModelsAdmin(admin.ModelAdmin):
    pass
admin.site.register(White_List_Models, White_List_ModelsAdmin)

class Log_Detail_ModelsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Log_Detail_Models, Log_Detail_ModelsAdmin)

class Monitor_DNS_ModelsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Monitor_DNS_Models, Monitor_DNS_ModelsAdmin)


class DNS_filter_ModelsAdmin(admin.ModelAdmin):
    pass
admin.site.register(DNS_filter_Models, DNS_filter_ModelsAdmin)

class DnsRecordsModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(DnsRecordsModel, DnsRecordsModelAdmin)


class DnsForwarderModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(DnsForwarderModel, DnsForwarderModelAdmin)

class LogToFileModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(LogToFileModel, LogToFileModelAdmin)