# -*- coding: utf-8 -*-
import time
from datetime import datetime, date

import json

import pandas
import pymongo
import requests
from numpy import random

# myclient = pymongo.MongoClient('mongodb://root:!QAZ2wsxok@10.15.108.23:27017/')
myclient = pymongo.MongoClient('mongodb://rwuser:Dzhinternet1=@10.33.10.38:8635/')
mongo_db = myclient.splservice
mongo_collection = mongo_db.serv_info_edit
# 获取当前时间
now = datetime.now()
today = date.today()
timestamp = time.time()
# path = "http://10.15.108.95:10003/im/splteam/serv/modify"
path = "http://10.33.3.143:10007/im/splteam/serv/modify"
headers = {
    'Content-Type': 'application/json',
    'httpdzh2': 'dzh-android-9.73',
    'Version': '9.73',
    'PlatformId': '3',
    'Connection': 'keep-alive',
    'httpdzh': 'dzh-pc-9.49',
    'Date': 'Thu, 16 Nov 2023 08:32:50 GMT',
    'httpdzh1': 'dzh-iphone-9.73'
}
params = {"qid": "", "account": "",
          "id": "",
          "waiter": ""}

df = pandas.read_excel('20240110ss2024-01-10.xlsx')

# 获取最大列数
max_columns = len(df.columns)
print('最大列数为：', max_columns)

# 循环遍历每一行数据
for index, row in df.iterrows():
    # 循环遍历行中的每个数据
    print("11111111111")
    row1 = [str(item) for item in list(row)]
    params["qid"] = "{}".format(int(time.time() * 1000))
    params["account"] = row1[1]
    params["id"] = row1[15]
    params["waiter"] = "{},{},{}".format(row1[8], row1[9], row1[10])
    print(params)
    response = requests.post(path, data=json.dumps(params),
                             headers=headers)
    print(response.content.decode('utf-8'))
    print(type(response.content))
    time.sleep(2)
    myquery = {"account": row1[1]}
    myteam = mongo_collection.find(myquery).sort("_id", -1).limit(1)
    teamid = "teamid"
    id = "id"
    if myteam:
        if myteam:
            teamid = myteam[0].get("teamId", "teamId")
            id = myteam[0].get("_id", "_id")
        else:
            teamid = "teamId"
            id = "id"
        df.loc[index, 'teamid'] = teamid
        df.loc[index, 'id'] = id
    print("created:{},{},{}".format(teamid, id, row1[0]))

# 保存修改后的DataFrame到新的Excel文件（可选）
df.to_excel('20240111ss{}.xlsx'.format(today), index=False)
