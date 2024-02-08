#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Mr.D
@software: PyCharm Community Edition
@file: kafkaProducer.py
@created on: 2017-10-12 10:05
"""
from bson import ObjectId
from kafka import KafkaProducer, KafkaConsumer
import time
import json
import random
import datetime

"""IM kafka"""
bootstrapServers = "10.15.108.24:9092,10.15.108.93:9092,10.15.108.94:9092"  # imservice
# bootstrapServers = "10.15.108.87:9092,10.15.108.88:9092,10.15.108.90:9092"   # pyq和股吧
# bootstrapServers = "10.15.207.219:9092,10.15.207.143:9092,10.15.207.179:9092"   # 云平台
# bootstrapServers = "10.33.9.218:9092,10.33.9.163:9092,10.33.9.72:9092"   # 外
# bootstrapServers = "10.15.114.203:9092,10.15.114.204:9092,10.15.114.205:9092"
# bootstrapServers = "10.15.144.191:9092,10.15.144.193:9092,10.15.144.194:9092"  # 大数据

producer = KafkaProducer(bootstrap_servers=bootstrapServers)

timestamp = int(time.time() * 1000)

n = 1
i = 1
count = 0
while i <= n:
    p_topic = "gwim.groups"
    _data = {
	"teamid": "6307749",
	"owner": "wps406",
	"dzhAc": "wps406",
	"name": "岭南股份交流01群",
	"type": "Public",
	"subtype": 3,
	"intro": "欢迎讨论切磋以碰撞出思想的火花，但请文明发言，出现违规会被踢出群聊哦",
	"stocks": ["SZ002717"],
	"star": 0,
	"valid": 2,
	"addTime": "2021-05-29 15:54:23",
	"upTime": "2021-05-29 15:54:23",
	"status": 1,
	"iconStatus": 0,
	"sysc": 1,
	"cert": "{\"type\":1,\"info\":\"\",\"group\":1}",
	"allowShowUser": 2,
	"extType": 0,
	"secConfirm": 0
}

    k = 6307749

    result = producer.send(topic=p_topic, value=json.dumps(_data, ensure_ascii=False).encode("utf8"),
                           key=json.dumps(k, ensure_ascii=False).encode("utf8"))

    print(json.dumps(_data, ensure_ascii=False))

    count += 1
    i += 1
producer.close()  # 不加close，kafka收不到数据
# time.sleep(2)
print("sent %d data" % count)
