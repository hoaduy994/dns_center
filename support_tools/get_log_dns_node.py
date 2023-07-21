import time
from datetime import date,datetime
from django.db import connection
import uuid

def db_multiple_rows(arr_dns):
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO main_part_log_detail_models(id,ip_client, domain, access_time,status,dns_center_id_id)VALUES (%s,%s,%s,%s,%s,%s);", arr_dns)
    print("Thành công !!!")
    
def main(dns_center_id,file_log):
    today = date.today()
    arr_dns=[]
    list_log=""
    split_log = file_log.split("\n")
    for row in split_log:
        split_row = row.split(" ")
        try: 
            if (("]: forwarded" not in row ) and 
                ("]: reply" not in row ) and
                ("]: config" not in row ) and  
                ("]: cached" not in row ) and 
                ("]: special" not in row ) and 
                ("]: read" not in row ) and 
                ("]: Mozilla" not in row ) and 
                ("]: Apple" not in row )) : 
                uuidOne = uuid.uuid1()
                dns_center_id= dns_center_id
                todays_date = date.today()
                try:
                    time = datetime.strptime(f'{todays_date.year} {split_row[0]} {split_row[1]} {split_row[2]}', '%Y %b %d %H:%M:%S')
                except:
                    time = datetime.strptime(f'{todays_date.year} {split_row[0]} {split_row[2]} {split_row[3]}', '%Y %b %d %H:%M:%S')
                ip_client = f"{split_row[-1]}"
                if "]: query[" in row:
                    status = f"{split_row[-4]}"
                    domain = f"{split_row[-3]}"
                else:
                    status = f"{split_row[-5]} {split_row[-4]}"
                    domain = f"{split_row[-3]}"
                # print(time, ip_client, status, domain)
                list_log+=f"{time} : {status} {domain} from {ip_client}\n"
                row_dns=(uuidOne,ip_client,domain,time,status,dns_center_id)
                arr_dns.append(row_dns)
        except:
            pass 
    db_multiple_rows(arr_dns=arr_dns)
    with open(f"/var/log/dns-sinkhole/{today}.log",'a+',encoding = 'utf-8') as f:
            f.write(str(list_log))
    