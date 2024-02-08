# -*- coding: utf-8 -*-
import time
from datetime import datetime, date

import json
import pandas
import numpy as np
import pymongo
import requests

# myclient = pymongo.MongoClient('mongodb://root:!QAZ2wsxok@10.15.108.23:27017/')
myclient = pymongo.MongoClient('mongodb://rwuser:Dzhinternet1=@10.33.10.38:8635/')
mongo_db = myclient.imback
mongo_collection = mongo_db.team_info
# 获取当前时间
now = datetime.now()
today = date.today()
# path = "http://10.15.108.95:10003/im/v2/team/create"
path = "http://10.33.3.143:11002/im/v2/team/create"
headers = {
    'Content-Type': 'application/json',
    'httpdzh2': 'dzh-android-9.41',
    'Version': '9.71',
    'PlatformId': '3',
    'Connection': 'keep-alive',
    'httpdzh': 'dzh-pc-9.49',
    'Date': 'Thu, 16 Nov 2023 08:32:50 GMT',
    'httpdzh1': 'dzh-iphone-9.49'
}
params = {
    "qid": "5f87f07d0476dc6bf41297e3",
    "icon": "",
    "count": "1",
    "textType": "0",
    "maxnum": "500",
    "isvip": "true",
    "valid": "1",
    "secConfirm": "0",
    "subtype": "0",
    "intro": "",
    "name": "",
    "startNum": "1",
    "attach": "",
    "member": ["chdtest001"],
    "owner": "chdtest002"

}

df = pandas.read_excel('vipteam20231228.xlsx')

# 获取最大列数
max_columns = len(df.columns)
# 打印最大列数
print('最大列数为：', max_columns)

# 循环遍历每一行数据
for index, row in df.iterrows():
    # 循环遍历行中的每个数据
    print("111111111111111")
    row1 = [str(item) for item in list(row)]

    if row1[0] == "cbl":
        params["icon"] = "http://mnews.dzh.com.cn/wap/data/im/hotgroup/images/20231116144202.png"
        params[
            "attach"] = "{\"text\":\"欢迎加入大智慧VIP群，我们致力于为VIP客户提供学习大智慧VIP产品和提升投资者专业知识和能力的服务。作为领先的投资平台，大智慧VIP集合了20年的产品优势，创新引领着投资潮流，并为专业交易用户量身定制了高端功能、企业预警、策略交易和慧信服务。感谢您选择大智慧VIP，期待与您共同成长！\"}"
        # params[
        #     "attach"] = {"text":"欢迎加入大智慧VIP群，我们致力于为VIP客户提供学习大智慧VIP产品和提升投资者专业知识和能力的服务。作为领先的投资平台，大智慧VIP集合了20年的产品优势，创新引领着投资潮流，并为专业交易用户量身定制了高端功能、企业预警、策略交易和慧信服务。感谢您选择大智慧VIP，期待与您共同成长！"}

        params["owner"] = row1[2]
        params["name"] = row1[3]
        params["member"] = [row1[4], row1[5], row1[6]]
        print(params)
        response = requests.post(path, data=json.dumps(params),
                                 headers=headers)
        print(response.content.decode('utf-8'))
        time.sleep(3)
        myquery = {"owner": row1[2]}
        myteam = mongo_collection.find(myquery).sort("_id", -1).limit(1)
        teamid ="teamid"
        for queryteamid in myteam:
            teamid = queryteamid["tid"]
            uptime = queryteamid["upTime"]
            # 将字符串转换为日期对象
            target_time = datetime.strptime(uptime, "%Y-%m-%d %H:%M:%S")
            if target_time > now:
                df.loc[index, 'teamid'] = teamid
        print("teamid:{}".format(teamid))

    if row1[0] == "xdr":
        params["icon"] = "http://mnews.dzh.com.cn/wap/data/im/hotgroup/images/20231204181054.png"
        params["attach"] = ""
        params["intro"] = ""
        params["owner"] = row1[2]
        # params["name"] = row1[3]
        params["name"] = "\uD83D\uDD25资讯及数据机会解盘"
        params["member"] = [row1[4], row1[5], row1[6], row1[7]]
        print(params)
        response = requests.post(path, data=json.dumps(params),
                                 headers=headers)
        print(response.content.decode('utf-8'))
        time.sleep(3)
        myquery = {"owner": row1[2]}
        myteam = mongo_collection.find(myquery).sort("_id", -1).limit(1)
        teamid ="teamid"
        for queryteamid in myteam:
            teamid = queryteamid["tid"]
            uptime = queryteamid["upTime"]
            # 将字符串转换为日期对象
            target_time = datetime.strptime(uptime, "%Y-%m-%d %H:%M:%S")
            if target_time > now:
                df.loc[index, 'teamid'] = teamid
        print("teamid:{}".format(teamid))
    if row1[0] == "dyh":
        params["icon"] = "http://mnews.dzh.com.cn/wap/data/im/hotgroup/images/20231204190249.png"
        params["attach"] = "{'text':'提供最新热门因子、策略动向，量化工具使用技巧及优质策略的构建分享等，因子专家伴您同行。'}"
        # params["attach"] = {'text':'提供最新热门因子、策略动向，量化工具使用技巧及优质策略的构建分享等，因子专家伴您同行。'}
        params[
            "intro"] = "本群致力于为大智慧VIP用户提供量化因子投研的相关的疑问解答，使用教学和优质策略分享等，有着定期的热门因子及策略内容播报以及不定期的优质策略构建和工具使用技巧分享，全心全意助力用户创建出自己的高质量的量化策略。"
        params["owner"] = row1[2]
        params["name"] = row1[3]
        params["member"] = [row1[4]]
        print(params)
        response = requests.post(path, data=json.dumps(params),
                                 headers=headers)
        print(response.content.decode('utf-8'))
        time.sleep(3)
        myquery = {"owner": row1[2]}
        myteam = mongo_collection.find(myquery).sort("_id", -1).limit(1)
        teamid ="teamid"
        for queryteamid in myteam:
            teamid = queryteamid["tid"]
            uptime = queryteamid["upTime"]
            # 将字符串转换为日期对象
            target_time = datetime.strptime(uptime, "%Y-%m-%d %H:%M:%S")
            if target_time > now:
                df.loc[index, 'teamid'] = teamid
        print("teamid:{}".format(teamid))
    if row1[0] == "tzw":
        params["icon"] = "http://mnews.dzh.com.cn/wap/data/im/hotgroup/images/20231206145556.jpg"
        params["attach"] = "{'text':'每个交易日，与你分享有价值的冷知识/热资讯/新产品。'}"
        # params["attach"] = {'text':'每个交易日，与你分享有价值的冷知识/热资讯/新产品。'}
        params["intro"] = "懂期货，更懂你。"
        params["owner"] = row1[2]
        params["name"] = row1[3]
        params["member"] = [row1[4], row1[5]]
        print(params)
        response = requests.post(path, data=json.dumps(params),
                                 headers=headers)
        print(response.content.decode('utf-8'))
        time.sleep(3)
        myquery = {"owner": row1[2]}
        myteam = mongo_collection.find(myquery).sort("_id", -1).limit(1)
        teamid ="teamid"
        for queryteamid in myteam:
            teamid = queryteamid["tid"]
            uptime = queryteamid["upTime"]
            # 将字符串转换为日期对象
            target_time = datetime.strptime(uptime, "%Y-%m-%d %H:%M:%S")
            if target_time > now:
                df.loc[index, 'teamid'] = teamid
        print("teamid:{}".format(teamid))
    if row1[0] == "yjy":
        params["icon"] = "http://mnews.dzh.com.cn/wap/data/im/hotgroup/images/20231116144202.png"
        params["attach"] = ""
        params["intro"] = ""
        params["owner"] = row1[2]
        params["name"] = row1[3]
        params["member"] = [row1[4], row1[5], row1[6], row1[7], row1[8], row1[9]]
        print(params)
        response = requests.post(path, data=json.dumps(params),
                                 headers=headers)
        print(response.content.decode('utf-8'))
        time.sleep(3)
        myquery = {"owner": row1[2]}
        myteam = mongo_collection.find(myquery).sort("_id", -1).limit(1)
        teamid ="teamid"
        for queryteamid in myteam:
            teamid = queryteamid["tid"]
            uptime = queryteamid["upTime"]
            # 将字符串转换为日期对象
            target_time = datetime.strptime(uptime, "%Y-%m-%d %H:%M:%S")
            if target_time > now:
                df.loc[index, 'teamid'] = teamid
        print("teamid:{}".format(teamid))
    # 保存修改后的DataFrame到新的Excel文件（可选）
    df.to_excel('vipteam{}.xlsx'.format(today), index=False)
