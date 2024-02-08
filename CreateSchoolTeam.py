
import json
import time

import redis
import requests
import urllib.parse
import csv
import logging

class Solution:
    def request_send(self, request_url, request_dict, request_msg):
        headers = {"Content-Type": "application/json"}
        request_url = "%s?%s" % (request_url, urllib.parse.urlencode(request_dict))
        print("request url:", request_url)
        print("request data:", json.dumps(request_msg).replace(" ", ""))
        _request = requests.post(request_url, data=json.dumps(request_msg), headers=headers)
        # print(_request.content.decode("utf-8"))
        _response = eval(_request.content.decode("utf-8"))
        if _request.status_code != 200:
            print("Error Information: ", _request.status_code, _request.reason)
        else:
            print("response: ", _request.content.decode("utf-8"))
            if _response["ErrorCode"] == 0:
                return _response
            else:
                return {}
    def createteam(self):
        pool = redis.ConnectionPool(host='10.15.108.95', port=6385, password='Test@123', db=0, decode_responses=True)
        r = redis.Redis(connection_pool=pool)
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

    def speakreview(self):
        pass
    def whitlist(self):
        pass








if __name__ == "__main__":
    s = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s))
    s = "bbbbb"
    print(Solution().lengthOfLongestSubstring(s))
    s = "pwwkew"
    print(Solution().lengthOfLongestSubstring(s))