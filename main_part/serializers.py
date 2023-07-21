from rest_framework import serializers
from .models import (Dns_Node_Models, Black_List_Models, 
                     White_List_Models, Log_Detail_Models, 
                     Monitor_DNS_Models, DNS_filter_Models,
                     DnsRecordsModel,DnsForwarderModel,
                     LogToFileModel)
from accounts.models import CustomUser

class Dns_Node_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Dns_Node_Models
        fields = ['id', 'hostname', 'ip_address','mac_address', 'os', 'create_time', 
                  'update_time','is_raw_black_list','is_raw_regex_black','is_raw_white_list',
                  'is_raw_regex_white_list','is_dns_dnsrecord','is_dns_forwarder']

class Black_List_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Black_List_Models
        fields = ['id', 'title', 'data_domain','note', 'create_time', 'update_time','type','add_dns']

class White_List_Serializer(serializers.ModelSerializer):
    class Meta:
        model = White_List_Models
        fields = ['id', 'title', 'data_domain','note', 'create_time', 'update_time','type','add_dns']

class Log_Detail_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Log_Detail_Models
        fields = ['id', 'dns_center_id', 'ip_client', 'domain','access_time', 'status']

class Monitor_DNS_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Monitor_DNS_Models
        fields = ['id', 'dns_center_id', 'ram', 'cpu', 'disk', 'status','create_time']

class DNS_filter_Serializer(serializers.ModelSerializer):
    class Meta:
        model = DNS_filter_Models
        fields = ['id', 'title', 'data_domain', 'create_time', 'update_time','add_dns','count','delete_dns']

class DnsRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DnsRecordsModel
        fields = ['id', 'domian', 'ip', 'create_time', 'update_time','add_dns']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'username' ]
        
class DnsForwarderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DnsForwarderModel
        fields = ['id', 'ip','title', 'create_time', 'update_time','add_dns']

class LogToFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogToFileModel
        fields = ['id', 'dns_center_id','log_line']