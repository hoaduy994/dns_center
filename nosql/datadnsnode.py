from connect import connect
import json
import os 
import time

def main():
    cursor=connect()
    s=[]
    raw_query = """
            SELECT "public"."main_part_dns_node_models"."id" AS "id"
            FROM "public"."main_part_dns_node_models"
        """
    cursor.execute(raw_query)
    dns_nodes = cursor.fetchall()
    for row in dns_nodes:
        id=row[0]
        top10_total = []
        total_query_allowed = 0
        raw_query_top10_total = f"""
            SELECT "public"."main_part_log_detail_models"."domain" AS "domain", count(*) AS "count"
            FROM "public"."main_part_log_detail_models"
            WHERE ("public"."main_part_log_detail_models"."dns_center_id_id" = '{str(id)}'::uuid
            AND ("public"."main_part_log_detail_models"."status" like '%query%') 
                AND "public"."main_part_log_detail_models"."access_time" >= CAST((now() + (INTERVAL '-7 day')) AS date) 
                AND "public"."main_part_log_detail_models"."access_time" < CAST(now() AS date) 
                AND ("public"."main_part_log_detail_models"."domain" <> 'from'
                OR "public"."main_part_log_detail_models"."domain" IS NULL))
            GROUP BY "public"."main_part_log_detail_models"."domain"
            ORDER BY "count" DESC, "public"."main_part_log_detail_models"."domain" ASC
            LIMIT 20
        """
        cursor.execute(raw_query_top10_total)
        a = cursor.fetchall()
        for row in a:
            total_query_allowed += row[1]
        for row in a:
            domain = row[0]
            count = row[1]
            top10_total.append({
                "domain": domain,
                "count": count,
                "total": count / total_query_allowed * 100
            })

        # top10_Block only #######################################
        top10_block_only = []
        total_query_blocked = 0
        raw_query_top_10_block_only = f"""
            SELECT "public"."main_part_log_detail_models"."domain" AS "domain", count(*) AS "count"
            FROM "public"."main_part_log_detail_models"
            WHERE ("public"."main_part_log_detail_models"."dns_center_id_id" = '{str(id)}'::uuid
            AND ("public"."main_part_log_detail_models"."status" like '%block%') 
                AND "public"."main_part_log_detail_models"."access_time" >= CAST((now() + (INTERVAL '-7 day')) AS date) 
                AND "public"."main_part_log_detail_models"."access_time" < CAST(now() AS date) 
                AND ("public"."main_part_log_detail_models"."domain" <> 'from'
                OR "public"."main_part_log_detail_models"."domain" IS NULL))
            GROUP BY "public"."main_part_log_detail_models"."domain"
            ORDER BY "count" DESC, "public"."main_part_log_detail_models"."domain" ASC
            LIMIT 20
        """

        cursor.execute(raw_query_top_10_block_only)
        a = cursor.fetchall()
        for row in a:
            total_query_blocked += row[1]
        for row in a:
            domain = row[0]
            count = row[1]
            top10_block_only.append({
                "domain": domain,
                "count": count,
                "total": count / total_query_blocked * 100
            })

        dns_center = f"""
            SELECT "hostname", "ip_address", "os",  "mac_address"
            FROM "main_part_dns_node_models"
            WHERE "id" = '{str(id)}'::uuid
            LIMIT 1048575
        """

        cursor.execute(dns_center)
        a = cursor.fetchall()
        b = a[0]
        DNS_Name = {"Company":
                    {"Domanin_name": b[0],
                     "OS": b[2],
                     "IP_address": b[1],
                     "Mac": b[3],
                     }}
        ####################### DNS Forwards #####################     
        raw_query = f"""
            SELECT "public"."main_part_dnsforwardermodel"."ip" AS "id", "public"."main_part_dnsforwardermodel"."ip" AS "ip", "public"."main_part_dnsforwardermodel"."title" AS "title"
            FROM "public"."main_part_dnsforwardermodel"
            WHERE ("public"."main_part_dnsforwardermodel"."add_dns" like '%{str(id)}%')

        """

        cursor.execute(raw_query)
        a = cursor.fetchall()
        orm_get_dns_forward=[]
        for row in a:   
            orm_get_dns_forward.append({
                "id": row[0],
                "ip": row[1],
                "title":row[2]
            })
        context = {
            "id_dns_center": id,
            "results": DNS_Name,
            "top10_total": top10_total,
            "top10_block_only": top10_block_only,
            "dns_forward": orm_get_dns_forward
        }
        s.append({
            id:context,
            })
    
    json_object = json.dumps(s, indent = 4)
    with open(f"{os.path.dirname(os.path.abspath(__file__))}/nosql_json/data_dns_node.json", "w+") as outfile:
        outfile.write(json_object)
if __name__ == '__main__':
    while True:
        main()
        print("#################")
        time.sleep(10)
        