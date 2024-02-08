# # coding:utf-8
# import requests
# import json
# import os
# import chardet
#
#
# # params = {
# #     "qid": "",
# #     "name": "",
# #     "startNum": 1,
# #     "owner": "",
# #     "subtype": 0,
# #     "valid": 2,
# #     "count": 10,
# #     "stocks": [{"code": "", "name": ""}],
# #     "admin": [],
# #     "member": [],
# #     "icon": "",
# #     "attach": {"text": "", "imgurl": "", "link": ""},
# #     "intro": "",
# #     "cert": {"type": 1, "info": "", "group": 1},
# #     "location": {"province": "", "city": "", "district": ""},
# #     "beans": [{"bean": 10, "t": 5}],
# #     "secConfirm": 0,
# #      "shop": {"type": "zdy", "intro": "佣金万2.5", "btntxt": "立即开户", "icon": "", "name": "", "url": ""},
# #     "maxnum": 500
# # }
#
#
# # 读取参数文件
# # with open('111.csv', 'r') as f:
# #     for line in f:
# #         lists = [line.strip().split(',')]
# #         # data = json.loads(line)
# #         # params["qid"] = data["qid"]
# #         # params["name"] = data["name"]
# #         # params["owner"] = data["owner"]
# #         print(lists)
#
# # 发送创建群组请求
# # for params_str in params:
# #     data = json.loads(params_str)
# #     response = requests.post('http://10.15.108.95:10003/im/v2/team/create', data=json.dumps(data), headers=headers)
# #     if response.status_code == 200:
# #         print(f"成功创建群组：{data['name']}")
# #     else:
# #         print(f"创建群组失败：{response.text}")
#
#
# headers = {
#     'Content-Type': 'application/json',
# 'httpdzh2': 'dzh-android-9.41',
# 'Version': '9.71',
# 'PlatformId': '3',
# 'Connection': 'keep-alive',
# 'httpdzh': 'dzh-pc-9.49',
# 'Date': 'Thu, 16 Nov 2023 08:32:50 GMT',
# 'httpdzh1': 'dzh-iphone-9.49'
# }
# params = {
#     "qid": "5f87f07d0476dc6bf41297e3",
#     "account": "chdtest001"
# }
# # data = json.loads(params)
# # response = requests.post('http://10.15.108.95:10003/im/v2/team/list/mine', data=json.dumps(params), headers=headers)
# # # print(response.content.decode("utf-8")
# # # )
# #
# # try:
# #     print(response.content.decode("utf-8"))
# # except UnicodeEncodeError:
# #     try:
# #         print(response.content.decode('unicode-escape'))
# #     except UnicodeDecodeError:
# #         print("Unable to decode content")
# # if response.status_code == 200:
# #     print(response.raw
# # )
# # else:
# #     print(f"创建群组失败：{response.text}")
#
#
# import sys
# response = requests.post('http://10.15.108.95:10003/im/v2/team/list/mine', data=json.dumps(params), headers=headers)
# print(response.content.decode('utf-8'))
# # try:
# #     sys.stdout.buffer.write(response.content)
# # except UnicodeEncodeError:
# #     try:
# #         print(response.content.decode('utf-8'))
# #     except UnicodeDecodeError:
# #         print("Unable to decode content")
#
# -*- coding: utf-8 -*-
import json
import pandas
import requests
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
    "icon":"http://mnews.dzh.com.cn/wap/data/im/hotgroup/images/20231116144202.png",
    "count":"1",
    "textType":"0",
    "maxnum":"500",
    "isvip":"true",
    "valid":"1",
    "secConfirm":"0",
    "subtype":"0",
    "intro":"",
    "name":"一个测试群",
    "startNum":"1",
    "attach":"",
    "member":["chdtest001"],
    "owner":"chdtest002"

}

# df = pandas.read_excel('test.xlsx')
# # 获取最大列数
# max_columns = len(df.columns)
# # 打印最大列数
# print('最大列数为：', max_columns)

# # 循环遍历每一行数据
# for index, row in df.iterrows():
#     # 循环遍历行中的每个数据
#     for value in row:
#         print(value)
response = requests.post('http://10.15.108.95:10003/im/v2/team/create', data=json.dumps(params),
                                 headers=headers)
print(response.content.decode('utf-8'))