from multiprocessing import context
import pprint
from connect import connect
from django.db import connection
import json
import os
from datetime import datetime, timedelta
import time
import pytz


def main():
    char_pihole = []
    cursor = connect()
    raw_query = """
            SELECT "id" AS "id" FROM "public"."main_part_dns_node_models" ORDER BY "id"
        """
    cursor.execute(raw_query)
    dns_nodes = cursor.fetchall()
    
    for row in dns_nodes:
        char_monitor_pihole = []
        id = row[0]

        now = datetime.now(pytz.timezone('Asia/Ho_Chi_Minh'))
        yesterday = now - timedelta(days=1) - timedelta(minutes=1)
        six_hours_ago = now - timedelta(hours = 6) - timedelta(minutes=1)
        now_string = now.strftime("%Y/%m/%d %H:%M:%Sz")
        yesterdat_string = yesterday.strftime("%Y/%m/%d %H:%M:%Sz")

        raw_data_char_monitor = f"""
                SET TIMEZONE TO 'asia/ho_chi_minh';
                SELECT "public"."main_part_monitor_dns_models"."ram" AS "ram", "public"."main_part_monitor_dns_models"."cpu" AS "cpu", "public"."main_part_monitor_dns_models"."disk" AS "disk", "public"."main_part_monitor_dns_models"."create_time" AS "create_time"
                FROM "public"."main_part_monitor_dns_models"
                WHERE ("public"."main_part_monitor_dns_models"."create_time" >= timestamp with time zone '{six_hours_ago}'
                AND "public"."main_part_monitor_dns_models"."create_time" < timestamp with time zone '{now_string}' AND "public"."main_part_monitor_dns_models"."dns_center_id_id" = '{str(id)}'::uuid)
                LIMIT 1048575
        """
        cursor.execute(raw_data_char_monitor)
        a = cursor.fetchall()

        for row in a:
            ram = row[0]
            cpu = row[1]
            disk = row[2]
            creat_time = str(row[3])
            char_monitor_pihole.append({
                "creat_time": creat_time,
                "ram": ram,
                "cpu": cpu,
                "disk": disk,
            })
        char_pihole.append({
            str(id): char_monitor_pihole,
        })
        
    chart_node = []
    for i in range(len(char_pihole)):
        for j in char_pihole[i]:
            chart = []
            each_node = char_pihole[i][str(j)]
            first_time = each_node[0]['creat_time'][0:15]
            count_ram = 0
            count_disk = 0
            count_cpu = 0
            avg = 0
            for k in range(len(each_node)):
                each_row = each_node[k]
                if str(first_time) not in str(each_row["creat_time"]):
                    chart.append({
                        'time': time_index,
                        'cpu': round(count_cpu / avg, 2),
                        'disk': round(count_disk / avg, 2),
                        'ram': round(count_ram / avg, 2)
                        
                    })
                    first_time = each_row["creat_time"][0:15]
                    count_ram = 0
                    count_disk = 0
                    count_cpu = 0
                    avg = 0
                if str(first_time) in str(each_row["creat_time"]):
                    time_index = str(first_time)[0:15] + "0"
                    count_ram += float(each_row["ram"])
                    count_disk += float(each_row["disk"])
                    count_cpu += float(each_row["cpu"])
                    avg += 1
                  
            chart_node.append({
                str(j) : chart
            })
            
    context = {"chart_dnsnode": chart_node}
    json_object = json.dumps(context, indent=4)
    with open(f"{os.path.dirname(os.path.abspath(__file__))}/nosql_json/char_monitor_pihole.json", "w+") as outfile:
        outfile.write(json_object)


if __name__ == '__main__':
    while True:
        main()
        print("################################")
        time.sleep(300)
