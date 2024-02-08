import redis
import requests
import json
import csv
import logging
# 转换盯盘exl为jmeter使用的csv文件
# 测试环境
# pool = redis.ConnectionPool(host='10.15.108.95', port=6385, password='test', db=0 , decode_responses=True)
# 产线
pool = redis.ConnectionPool(host='10.33.3.217', port=6379, password='Dzhinternet!', db=0, decode_responses=True)

r = redis.Redis(connection_pool=pool)


def whitecsv():
    with open('0830.csv', encoding='utf-8') as fp:
        reader = csv.reader(fp)
        # 获取标题,去标题
        next(reader)
        # print(header)
        # 遍历数据
        count_list = []
        for i in reader:
            stockid = i[0]
            # 去list空值
            while "" in i:
                i.remove("")
            # 去redis拿teamno
            try:
                teamno = (list(r.smembers('im_team_analyst_stock_team:' + stockid))[0]).split(':')[0]
            except Exception as e:
                # 打印没有群的股票代码
                print(stockid)
                logging.exception(e)

            i.append(teamno)
            # 生成总的list
            count_list.append(i)
        # print(count_list)
        # 表头
        header = ['stockid', 'stockname', 'teamid']
        # 建文件，在当前目录
        with open('stock_complete.csv', 'w', newline="", encoding='utf-8') as file_obj:
            # 1:创建writer对象
            writer = csv.writer(file_obj)
            # 2:写表头
            writer.writerow(header)
            # 3:遍历列表，将每一行的数据写入csv
            for p in count_list:
                writer.writerow(p)


if __name__ == '__main__':
    whitecsv()
