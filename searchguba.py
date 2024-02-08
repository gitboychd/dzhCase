# encoding: utf-8
import redis
import random
import string
import time
import pymongo
import json

from bson import ObjectId
from kafka import KafkaProducer, KafkaConsumer

from bson import ObjectId
# use scan_iter count redis key
# support key prefix
#
bootstrapServers = "10.15.108.24:9092,10.15.108.93:9092,10.15.108.94:9092"  # imservice
producer = KafkaProducer(bootstrap_servers=bootstrapServers)


pool = redis.ConnectionPool(host='10.15.108.95', port=6385, password='test', db=0 , decode_responses=True)
r = redis.Redis(connection_pool=pool)


myclient = pymongo.MongoClient('mongodb://root:root@10.15.108.23:27017/')
mongo_db = myclient.imback
mongo_collection = mongo_db.team_info

#打印连接信息
# print(myclient.server_info())

# myquery = {"tid" : "6202989"}
#
# mydoc = mongo_collection.find(myquery)
#
# for x in mydoc:
#     print(x)
#     print(type(x))

def select_redis_key():
    start_time = time.time()
    prefix_key = "AGENT_MEMBER_MSG_UNREAD_"
    result_length = 0
    for key in r.scan_iter(match='im_guba_group_id*', count=100):
        result_length += 1
        teamname = key.split(':')[1]
        teamno = r.zrange(key, 0, -1)[0]
        # print(key)
        # print(teamname)
        # print(type(teamname))
        # print(teamno)
        # print(type(teamno))

        myquery = {"tid" : teamno}
        mydoc = mongo_collection.find(myquery)
        for _data in mydoc:

            _data.pop('_id')
            _data.pop('tid')
            if 'stock'  in _data :
                _data.pop('stock')
                _data['teamid'] = teamno
                _data['stocks'] = [teamname]
                # print(json.dumps(_data, ensure_ascii=False))
                p_topic = "gwim.groups"
                k = int(teamno)
                result = producer.send(topic=p_topic, value=json.dumps(_data, ensure_ascii=False).encode("utf8"),
                                       key=json.dumps(k, ensure_ascii=False).encode("utf8"))
    producer.close()
        # print result_length,' is ',key
    print("normal ways spend time(s) is :", time.time() - start_time)
    print("normal way seelect the keys with prefix", prefix_key, "count(*) is :", result_length)

    # print(r.keys(pattern='im_guba_group_id*'))

def main():
    select_redis_key()


if __name__ == '__main__':
    main()

