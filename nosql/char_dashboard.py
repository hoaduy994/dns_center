import pprint
from connect import connect
import json
import os
from datetime import datetime, timedelta
import pytz
import time


def main():
    cursor = connect()

    # Block Char || White Char
    # tong
    now = datetime.now(pytz.timezone('Asia/Ho_Chi_Minh'))
    yesterday = now - timedelta(days=1) - timedelta(minutes=1)
    now_string = now.strftime("%Y/%m/%d %H:%M:%S")
    yesterdat_string = yesterday.strftime("%Y/%m/%d %H:%M:%S")
    raw_query = f"""
            SET TIMEZONE TO 'asia/ho_chi_minh';
            SELECT date_trunc('minute', "public"."main_part_log_detail_models"."access_time") AS "access_time", count(*) AS "count"
            FROM "public"."main_part_log_detail_models"
            WHERE ("public"."main_part_log_detail_models"."access_time" >= timestamp with time zone '{yesterdat_string}'
            AND "public"."main_part_log_detail_models"."access_time" < timestamp with time zone '{now_string}' AND (lower("public"."main_part_log_detail_models"."status") like '%query%'))
            GROUP BY date_trunc('minute', "public"."main_part_log_detail_models"."access_time")
            ORDER BY date_trunc('minute', "public"."main_part_log_detail_models"."access_time") ASC
            """

    cursor.execute(raw_query)
    total_queries = cursor.fetchall()

    len_time = len(total_queries)

    raw_query = f"""
            SET TIMEZONE TO 'asia/ho_chi_minh';
            SELECT date_trunc('minute', "public"."main_part_log_detail_models"."access_time") AS "access_time", count(*) AS "count"
            FROM "public"."main_part_log_detail_models"
            WHERE ("public"."main_part_log_detail_models"."access_time" >= timestamp with time zone '{yesterdat_string}'
            AND "public"."main_part_log_detail_models"."access_time" < timestamp with time zone '{now_string}' AND (NOT (lower("public"."main_part_log_detail_models"."status") like '%query%')
            OR "public"."main_part_log_detail_models"."status" IS NULL))
            GROUP BY date_trunc('minute', "public"."main_part_log_detail_models"."access_time")
            ORDER BY date_trunc('minute', "public"."main_part_log_detail_models"."access_time") ASC
            """
    cursor.execute(raw_query)
    block_char = cursor.fetchall()
    White_Block_Char = []
    j = 0
    for i in range(len_time):
        time = str(total_queries[i][0])
        White_Char = int(total_queries[i][1])
        try:
            time_block = str(block_char[j][0])
            if time == time_block:
                Block_Char = int(block_char[j][1])
                j += 1
            else:
                Block_Char = 0
        except:
            Block_Char = 0

        White_Block_Char.append({'time': time,
                                  'block_char': Block_Char,
                                 'white_char': White_Char})

    White_Block_Char.reverse()

    results_chart = []
    
    first_time = White_Block_Char[0]['time'][0:15]
    count_block = 0
    count_white = 0

    for i in range(len(White_Block_Char)):
        if str(first_time) not in str(White_Block_Char[i]['time']):
            results_chart.append({
                'time': time_index,
                'white_chart': count_white,
                'block_chart': count_block
            })
            time_index = ""
            count_block = 0
            count_white = 0
            first_time = str(White_Block_Char[i]['time'])[0:15]

        if str(first_time) in str(White_Block_Char[i]['time']):
            time_index = str(first_time)[0:15] + "0"
            count_block += int(White_Block_Char[i]['block_char'])
            count_white += int(White_Block_Char[i]['white_char'])

    context = {"White_Block_Char": results_chart}
    json_object = json.dumps(context, indent=4)
    with open(f"{os.path.dirname(os.path.abspath(__file__))}/nosql_json/char_dashboard.json", "w+") as outfile:
        outfile.write(json_object)


if __name__ == '__main__':
    while True:
        check =1
        while check ==1:
            try:
                main()
                check =0
            except:
                print("!!!!!!!")
                time.sleep(5)
                
        
        time.sleep(300)
