from connect import connect
import json
import os
import time


def main():
    cursor = connect()

    # Queries Block || Total Queries || Percent Blocked
    raw_query = """
            SELECT count(*) AS "count"
            FROM "public"."main_part_log_detail_models"
            WHERE ("public"."main_part_log_detail_models"."access_time" >= CAST(now() AS date)
            AND "public"."main_part_log_detail_models"."access_time" < CAST((now() + (INTERVAL '1 day')) AS date))
   """

    cursor.execute(raw_query)
    orm_total_queries_count = cursor.fetchall()[0][0]

    raw_query = """
            SELECT count(*) AS "count"
            FROM "public"."main_part_log_detail_models"
            WHERE ("public"."main_part_log_detail_models"."access_time" >= CAST(now() AS date)
            AND "public"."main_part_log_detail_models"."access_time" < CAST((now() + (INTERVAL '1 day')) AS date) 
            AND (NOT ("public"."main_part_log_detail_models"."status" like '%query%')
            OR "public"."main_part_log_detail_models"."status" IS NULL))
   """

    cursor.execute(raw_query)
    orm_block_queries_count = cursor.fetchall()[0][0]

    raw_query = """SELECT "public"."main_part_dns_filter_models"."count" AS "count"
                    FROM "public"."main_part_dns_filter_models"
                    LIMIT 1048575"""
    cursor.execute(raw_query)
    orm_list_block = cursor.fetchall()
    count_blocklist = 0
    for row in orm_list_block:
        count_blocklist += int(row[0])

    try:
        Percent_Blocked = (
            int(orm_block_queries_count)/int(orm_total_queries_count))*100
    except:
        Percent_Blocked = 0
    # results.update({'Percent_Blocked': f'{round(Percent_Blocked)}%'})
    results = {
        'total_queries': '{0:,}'.format(orm_total_queries_count).replace(',', '.'),
        'Queries_Blocked': '{0:,}'.format(orm_block_queries_count).replace(',', '.'),
        'Percent_Blocked': f'{round(Percent_Blocked, 2)}%',
        'Domain_Blocklist': '{0:,}'.format(count_blocklist).replace(',', '.'),
    }

    context = {
        "results": results
    }

    json_object = json.dumps(context, indent=4)
    with open(f"{os.path.dirname(os.path.abspath(__file__))}/nosql_json/index_queries.json", "w+") as outfile:
        outfile.write(json_object)


if __name__ == '__main__':
    while True:
        main()
        time.sleep(10)
