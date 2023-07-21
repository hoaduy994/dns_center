from connect import connect
import json
import os
import time


def main():
    cursor = connect()
    results = []

    #     # Top Domain Blocked ################################################
    Top_Domain_Blocked = []
    raw_query = """
            SELECT "public"."main_part_log_detail_models"."domain" AS "domain", count(*) AS "count"
            FROM "public"."main_part_log_detail_models"
            WHERE ("public"."main_part_log_detail_models"."access_time" >= CAST(now() AS date)
            AND "public"."main_part_log_detail_models"."access_time" < CAST((now() + (INTERVAL '1 day')) AS date) 
            AND (NOT ("public"."main_part_log_detail_models"."status" like '%query%')
                OR "public"."main_part_log_detail_models"."status" IS NULL))
            GROUP BY "public"."main_part_log_detail_models"."domain"
            ORDER BY "count" DESC, "public"."main_part_log_detail_models"."domain" ASC
            LIMIT 10
        """
    cursor.execute(raw_query)
    Domain_block = cursor.fetchall()

    Sum_Blocked = 0
    for row in Domain_block:
        domain_blocked = get_day_domain(row[0])
        Top_Domain_Blocked.append(
            {'domain': row[0], 'count': row[1], 'domain_day': domain_blocked})
        Sum_Blocked += int(row[1])
    results = {
        'Top_Domain_Blocked': Top_Domain_Blocked,
        'Sum_Blocked': Sum_Blocked
    }

#     # Top Domain Allowed ###################################################
    Top_Domain_Allowed = []
    Sum_Allowed = 0
    raw_query = """
            SELECT "public"."main_part_log_detail_models"."domain" AS "domain", count(*) AS "count"
            FROM "public"."main_part_log_detail_models"
            WHERE ("public"."main_part_log_detail_models"."access_time" >= CAST(now() AS date)
            AND "public"."main_part_log_detail_models"."access_time" < CAST((now() + (INTERVAL '1 day')) AS date) 
            AND (lower("public"."main_part_log_detail_models"."status") like '%query%'))
            GROUP BY "public"."main_part_log_detail_models"."domain"
            ORDER BY "count" DESC, "public"."main_part_log_detail_models"."domain" ASC
            LIMIT 10
        """
    cursor.execute(raw_query)
    domain_allowed = cursor.fetchall()
    for row in domain_allowed:
        domain_allowed = get_day_domain(row[0])
        Top_Domain_Allowed.append(
            {'domain': row[0], 'count': row[1], 'domain_day': domain_allowed})
        Sum_Allowed += int(row[1])
    results.update({'Top_Domain_Allowed': Top_Domain_Allowed,
                   'Sum_Allowed': Sum_Allowed})

    context = {
        "top_domain": results
    }

    json_object = json.dumps(context, indent=4, default=str)
    with open(f"{os.path.dirname(os.path.abspath(__file__))}/nosql_json/top_domain.json", "w+") as outfile:
        outfile.write(json_object)


def get_day_domain(id):
    cursor = connect()

    raw_query = f"""
            SELECT CAST("public"."main_part_log_detail_models"."access_time" AS date) AS "access_time", count(*) AS "count"
            FROM "public"."main_part_log_detail_models"
            WHERE "public"."main_part_log_detail_models"."domain" = '{id}'
            GROUP BY CAST("public"."main_part_log_detail_models"."access_time" AS date)
            ORDER BY CAST("public"."main_part_log_detail_models"."access_time" AS date) DESC
            LIMIT 15
            """
    cursor.execute(raw_query)
    count_domain_days = cursor.fetchall()
    domain_day = []
    for row in count_domain_days:
        time = row[0]
        count = row[1]
        domain_day.append({
            'time': time,
            'count': count
        })
    results = {
        'domain_day': domain_day
    }

    return results


if __name__ == '__main__':
    while True:
        main()
        time.sleep(14400)
