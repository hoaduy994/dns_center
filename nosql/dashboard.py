from traceback import print_tb
from connect import connect
import json
import os
import time


def main():
    cursor = connect()

#     # Top IP####################
    top_ip = []
    raw_query = """
            SELECT "public"."main_part_dns_node_models"."id" AS "id"
            FROM "public"."main_part_dns_node_models"
   """

    cursor.execute(raw_query)
    id_dns_center = cursor.fetchall()

    for row in id_dns_center:
        dns_center_id_ = row[0]
        # ip_address_dns_node = Dns_Node_Models.objects.get(pk=dns_center_id_)
        raw_query = f"""
            SELECT "public"."main_part_dns_node_models"."ip_address" AS "ip_address",
                   "public"."main_part_dns_node_models"."id" AS "id"
            FROM "public"."main_part_dns_node_models"
            WHERE "public"."main_part_dns_node_models"."id" = '{dns_center_id_}'::uuid
            """

        cursor.execute(raw_query)
        data_address_dns_node = cursor.fetchall()
        ip_address_dns_node = data_address_dns_node[0][0]
        id_address_dns_node = data_address_dns_node[0][1]

        raw_query = f"""
                    SELECT count(*) AS "count"
                    FROM "public"."main_part_log_detail_models"
                    WHERE ("public"."main_part_log_detail_models"."access_time" >= CAST(now() AS date)
                    AND "public"."main_part_log_detail_models"."access_time" < CAST((now() + (INTERVAL '1 day')) AS date) 
                    AND "public"."main_part_log_detail_models"."dns_center_id_id" = '{dns_center_id_}'::uuid)
                    """

        cursor.execute(raw_query)
        total_send_request = cursor.fetchall()[0][0]

        raw_query = f"""
                    SELECT count(*) AS "count"
                    FROM "public"."main_part_log_detail_models"
                    WHERE ("public"."main_part_log_detail_models"."access_time" >= CAST(now() AS date)
                    AND "public"."main_part_log_detail_models"."access_time" < CAST((now() + (INTERVAL '1 day')) AS date) 
                    AND "public"."main_part_log_detail_models"."dns_center_id_id" = '{dns_center_id_}'::uuid 
                    AND (NOT (lower("public"."main_part_log_detail_models"."status") like '%query%')
                    OR "public"."main_part_log_detail_models"."status" IS NULL))
                    """

        cursor.execute(raw_query)
        total_denied_request = cursor.fetchall()[0][0]

        total_forwarded = int(total_send_request)-int(total_denied_request)
        top_ip.append({
            "id_dns": id_address_dns_node,
            "ip_dns": ip_address_dns_node,
            "total_send_request": total_send_request,
            "block_send_request": total_denied_request,
            "forwarded_send_request": total_forwarded
        })
    
    results = {
        'top_ip': top_ip
    }

    context = {
        "results": results
    }
    
    json_object = json.dumps(context, indent=4)
    with open(f"{os.path.dirname(os.path.abspath(__file__))}/nosql_json/dashboard.json", "w+") as outfile:
        outfile.write(json_object)


if __name__ == '__main__':
    while True:
        main()
        time.sleep(10)
