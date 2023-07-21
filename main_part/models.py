from django.db import models
import uuid

###############DNS NODE##################


class Dns_Node_Models(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    hostname = models.CharField(max_length=255, blank=True, default='') 
    ip_address = models.CharField(max_length=255, blank=True, default='') 
    mac_address = models.CharField(max_length=255, blank=True, default='')
    os = models.CharField(max_length=255, blank=True, default='')
    create_time = models.DateTimeField(auto_now_add=True,) 
    update_time = models.DateTimeField(auto_now=True)
    is_raw_black_list= models.BooleanField(default=False)
    is_raw_regex_black= models.BooleanField(default=False)
    is_raw_white_list= models.BooleanField(default=False)
    is_raw_regex_white_list= models.BooleanField(default=False)
    is_dns_dnsrecord = models.BooleanField(default=False)
    is_dns_forwarder = models.BooleanField(default=False)
    

    def __str__(self):
        return self.hostname

###############Black List##################


class Black_List_Models(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    title = models.CharField(max_length=255, blank=True, default='')
    data_domain = models.CharField(max_length=999, blank=True, default='') 
    note = models.CharField(max_length=999, blank=True, default='') 
    create_time = models.DateTimeField(auto_now_add=True) 
    update_time = models.DateTimeField(auto_now=True) 
    type = models.CharField(max_length=255, blank=True, default='')
    add_dns = models.TextField(blank=True, default='') 
    def __str__(self):
        return self.data_domain

###############White List##################

class White_List_Models(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    title = models.CharField(max_length=255, blank=True, default='')
    data_domain = models.CharField(max_length=225, blank=True, default='') 
    note = models.CharField(max_length=225, blank=True, default='') 
    create_time = models.DateTimeField(auto_now_add=True) 
    update_time = models.DateTimeField(auto_now=True) 
    type = models.CharField(max_length=255, blank=True, default='')
    add_dns = models.TextField(blank=True, default='') 

    def __str__(self):
        return self.data_domain
###############Log Detail##################


class Log_Detail_Models(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    dns_center_id = models.ForeignKey(
        Dns_Node_Models, 
        on_delete=models.CASCADE)
    ip_client = models.CharField(max_length=255, blank=True, default='')
    domain = models.CharField(max_length=255, blank=True, default='')
    access_time = models.DateTimeField(blank=True, default='')
    status = models.CharField(max_length=255, blank=True, default='')

    def __str__(self):
        return self.id

###############Monitor DNS##################


class Monitor_DNS_Models(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    dns_center_id = models.ForeignKey(
        Dns_Node_Models, 
        on_delete=models.CASCADE)
    ram = models.CharField(max_length=100, blank=True, default='')
    cpu = models.CharField(max_length=100, blank=True, default='')
    disk = models.CharField(max_length=100, blank=True, default='')
    status = models.CharField(max_length=100, blank=True, default='')
    create_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.id


###############DNS Filter##################

class DNS_filter_Models(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    
    title = models.CharField(max_length=255, blank=True, default='')
    data_domain=models.CharField(max_length=255, blank=True, default='')
    create_time = models.DateTimeField(auto_now_add=True) 
    update_time = models.DateTimeField(auto_now=True) 
    add_dns= models.TextField(blank=True, default='') 
    count = models.CharField(max_length=225, blank=True, default='') 
    delete_dns = models.TextField(blank=True, default='') 
    def __str__(self):
        return self.dns_center_id

class DnsRecordsModel(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    domian = models.CharField(max_length=255, blank=True, default='')
    ip = models.CharField(max_length=255, blank=True, default='')
    create_time = models.DateTimeField(auto_now_add=True) 
    update_time = models.DateTimeField(auto_now=True) 
    add_dns = models.TextField(blank=True, default='') 
    def __str__(self):
        return self.domian
    
class DnsForwarderModel(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    ip = models.CharField(max_length=255, blank=True, default='')
    title = models.CharField(max_length=255, blank=True, default='')
    create_time = models.DateTimeField(auto_now_add=True) 
    update_time = models.DateTimeField(auto_now=True) 
    add_dns = models.TextField(blank=True, default='') 
    def __str__(self):
        return self.ip

class LogToFileModel(models.Model):

    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    dns_center_id = models.ForeignKey(
        Dns_Node_Models, 
        on_delete=models.CASCADE)
    log_line = models.TextField(blank=True, default='') 
    
    def __str__(self):
        return self.id

class IpSiemToWeb(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    ip_siem =  models.CharField(max_length=255, blank=True, default='')
    port_siem = models.CharField(max_length=255, blank=True, default='')
    is_connect= models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True) 
    update_time = models.DateTimeField(auto_now=True) 
