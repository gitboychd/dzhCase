# encoding: utf-8
import csv

import redis
from pip._internal.utils import logging



class Solution:
    def createteam(self):
        pool = redis.ConnectionPool(host='10.15.108.95', port=6385, password='Test@123', db=0, decode_responses=True)
        # pool = redis.ConnectionPool(host='10.33.3.217', port=6379, password='Dzhinternet!', db=0, decode_responses=True)
        r = redis.Redis(connection_pool=pool)
        with open('lark_talents.csv', encoding='utf-8') as fp:
            reader = csv.reader(fp)
            # 获取标题,去标题
            next(reader)
            # print(header)
            # 遍历数据
            count_list = []
            for i in reader:
                number = i[0]
                # 去list空值
                while "" in i:
                    i.remove("")
                print(number)
                key =str("im_team_user_mobile:23223025")
                try:
                    r.sadd(key,number)
                except Exception as e:
                    print(number)
                    logging.exception(e)



if __name__ == "__main__":
    print(Solution().createteam())