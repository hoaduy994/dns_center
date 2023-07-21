
from itertools import count
import requests
from support_tools.Module import regex_dns
import uuid
from datetime import datetime
from django.db import connection
from main_part.models import DNS_filter_Models,Dns_Node_Models
from django.db.models import Q,Count
def db_multiple_rows(arr_dns):
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO main_part_black_list_models(id,title, data_domain, type,note,create_time,update_time,add_dns)VALUES (%s,%s,%s,%s,%s,%s,%s,%s);", arr_dns)
    print("Thành công !!!")
    

def main(title,data_domain,list_add_dns):
    arr_dns=[]
    now = datetime.now()
    r = requests.get(data_domain)
    data_dns=str(r.text).split("\n")
    total = 0
    for i in data_dns:
        if "#" not in i:
            uuidOne = uuid.uuid1()
            dns=regex_dns.regex_dns(i)
            if dns != None:
                row_dns=(uuidOne,title,dns,'1','',now,now,list_add_dns)
                arr_dns.append(row_dns)
                total+=1
    DNS_filter_Models.objects.filter(Q(data_domain=data_domain)).update(count=total)
    db_multiple_rows(arr_dns=arr_dns)
    for dns_add in (dns_add for dns_add in list_add_dns.split(", ") if dns_add != ""):
        Dns_Node_Models.objects.filter(Q(id=dns_add)).update(is_raw_black_list=False)
        
# if __name__ == "__main__":
#     filter_List='https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts'
#     main(filter_List)