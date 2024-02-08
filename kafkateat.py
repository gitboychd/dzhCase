# -*- coding: utf-8 -*-
import time
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'zxg_incr_all',
    group_id='test_id',
    bootstrap_servers=['10.15.108.103:9092', '10.15.107.14:9092', '10.15.107.15:9092'],       # 要发送的kafka主题
    auto_offset_reset='earliest',                   # 有两个参数值，earliest和latest，如果省略这个参数，那么默认就是latest
)
for msg in consumer:
    print(msg)
    print(f"topic = {msg.topic}")           # topic default is string
    print(f"partition = {msg.partition}")
    print(f"value = {msg.value.decode()}")  # bytes to string
    print(f"timestamp = {msg.timestamp}")
    print("time = ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg.timestamp / 1000)))