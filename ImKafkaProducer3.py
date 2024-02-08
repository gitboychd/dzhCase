#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Mr.D
@software: PyCharm Community Edition
@file: kafkaProducer.py
@created on: 2017-10-12 10:05
"""
from kafka import KafkaProducer, KafkaConsumer
import time
import json
import random
import datetime

"""IM kafka"""
bootstrapServers = "10.15.108.24:9092,10.15.108.93:9092,10.15.108.94:9092"   # imservice
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
    # ImMsgCopyJson = dict()
    # ImMsgCopyJson["operateUserId"] = "hxtest-q%d" % i
    # ImMsgCopyJson["notifyUserId"] = "hxtest-q110"
    # ImMsgCopyJson["type"] = "FOLLOW_MSG_NOTIFY"
    # ImMsgCopyJson["postId"] = postId  # random.choice(postIdDict["hxtest-q110"])
    # index = random.randint(0, 7)
    # ImMsgCopyJson["time"] = (datetime.datetime.now() + datetime.timedelta(days=-index)).strftime("%Y-%m-%d %H:%M:%S")

    # _data = "{\"CallbackCommand\":\"Sns.CallbackFriendAdd\",\"From_Account\":\"wps111\",\"To_Account\":\"wps302\",\"contact\":true,\"fromDzhAc\":\"wps111\",\"source\":\"Android\",\"t\":1545040800000,\"toDzhAc\":\"wps302\"}"

    # p_topic = "STOCK_GUBA_MSG"
    # _data = {"stock":"SH601099","account":"hxtest-q118","content":"\u4e0d\u662f\u4e00\u822c\u7684\u5783\u573e","time":"2019-03-31 12:49:59"}
    # _data = {"stock":"SZ300126","account":"abc100","content":"\u7b2c\u4e00\u53f0\u9636\u4e0b\u5b8c\uff0c\u76d8\u6574\u4e00\u4e0b\uff0c\u51c6\u5907\u4e0b\u7b2c\u4e8c\u53f0\u9636","time":"2018-12-06 05:56:41"}

    # p_topic = "im_start_change_topic"
    # _data = ["{\"dt\":\"20190504\",\"username\":\"hxtest-q110\",\"before_grade\":2000,\"after_grade\":1000}","{\"dt\":\"20190504\",\"username\":\"hxtest-q118\",\"before_grade\":1000,\"after_grade\":2000}","{\"dt\":\"20190504\",\"username\":\"hxtest-q1004\",\"before_grade\":2000,\"after_grade\":1000}","{\"dt\":\"20190504\",\"username\":\"hxtest-q1006\",\"before_grade\":1000,\"after_grade\":2000}"]

    # p_topic = "gwim_group_members"
    # k = b"1001555"
    # _data = {"body":"{\"CallbackCommand\":\"Group.CallbackAfterNewMemberJoin\",\"GroupId\":\"1001555\",\"JoinType\":\"Apply\",\"NewMemberList\":[{\"Member_Account\":\"161388192\"}],\"Operator_Account\":\"161388192\",\"Type\":\"Public\"}","param":{"CallbackCommand":"Group.CallbackAfterNewMemberJoin","ClientIP":"180.168.223.146","OptPlatform":"Android","SdkAppid":"1400007088","Type":"Public","NewMemberList":[{"Member_Account":"161388192"}],"JoinType":"Apply","Operator_Account":"161388192","GroupId":"1001555"}}
    # _data = {"body":"{\"CallbackCommand\":\"Group.CallbackAfterNewMemberJoin\",\"GroupId\":\"1001555\",\"JoinType\":\"Invited\",\"NewMemberList\":[{\"Member_Account\":\"161388184\"}],\"Operator_Account\":\"hxtest-q110\",\"Type\":\"Public\"}","param":{"CallbackCommand":"Group.CallbackAfterNewMemberJoin","ClientIP":"180.168.223.146","OptPlatform":"Android","SdkAppid":"1400007088","contenttype":"json","Type":"Public","NewMemberList":[{"Member_Account":"161388184"}],"JoinType":"Invited","Operator_Account":"hxtest-q110","GroupId":"1001555"}}
    # _data = {"body":"{\"CallbackCommand\":\"Group.CallbackAfterNewMemberJoin\",\"GroupId\":\"1001555\",\"JoinType\":\"Invited\",\"NewMemberList\":[{\"Member_Account\":\"hxtest-q118\"}],\"Operator_Account\":\"hxtest-q110\",\"Type\":\"Public\"}","param":{"CallbackCommand":"Group.CallbackAfterNewMemberJoin","ClientIP":"180.168.223.146","OptPlatform":"Android","SdkAppid":"1400007088","contenttype":"json","Type":"Public","NewMemberList":[{"Member_Account":"hxtest-q118"}],"JoinType":"Invited","Operator_Account":"hxtest-q110","GroupId":"1001555"}}
    # _data = "{\"CallbackCommand\":\"Group.CallbackAfterNewMemberJoin\",\"GroupId\":\"1001555\",\"JoinType\":\"Invited\",\"NewMemberList\":[{\"Member_Account\":\"hxtest-q118\"}],\"Type\":\"Public\",\"contact\":false,\"dzhAcList\":[\"hxtest-q118\"],\"source\":\"Android\",\"t\":1558417807579}"

    # 机器人消息
    # p_topic = "im.robot.msg"  # 内
    # p_topic = "im_robot_msg"  # 外
    # 个人
    # _data = {"msg_id": "gsxw-20190420_2gsxw-test001", "from": "hxtest-q263", "broadcast": 0, "data": {"txt": "<b>20190420_2资讯机器人(公司新闻)测试111111111</b> 20190420_2资讯机器人(公司新闻)测试333333333 <a href=\"http://www.baidu.com\" style=\"color:#3366cc;\">查看全文</a>", "stock": ["SH600313", "SH601519"]}, "action": 0, "user": {"dzh113265": {"notify": 0}, "8834749": {"notify": 0}, "ls001": {"notify": 0}, "hxtest-q110": {"notify": 0}, "yehaiyun001": {"notify": 0}}, "t": 1555726396058}
    # 群
    # _data = {"msg_id": "gsxw-20190420_3gsxw-test001", "from": "hxtest-q263", "broadcast": 0, "data": {"txt": "【20190420_3资讯机器人(公司新闻)测试111111111】 20190420_3资讯机器人(公司新闻)测试333333333 <a href=\"http://www.baidu.com\" style=\"color:#3366cc;\">查看全文</a>", "stock": ["SH600181"]}, "action": 0, "t": timestamp, "group": ["1245353"]}
    # _data = {"msg_id": "gsxw-20190420_3gsxw-test001", "from": "dzhhx071", "broadcast": 0, "data": {"txt": "<b>20190420_3资讯机器人(公司新闻)测试111111111</b> 20190420_3资讯机器人(公司新闻)测试333333333 <a href=\"http://www.baidu.com\" style=\"color:#3366cc;\">查看全文</a>", "stock": ["SH600313", "SH601519"]}, "action": 0, "t": timestamp, "group": ["1000301","6084911"]}
    # _data = {"msg_id": "gsxw-20190420_3gsxw-test001", "from": "dzhhx071", "broadcast": 0, "data": {"txt": "785538180在作品中@了你", "stock": ["SH600313", "SH601519"]}, "action": 0, "t": timestamp, "user": {"785538180": {"notify": 0}}}  # 785538180
    # _data = {"msg_id": "jszbjqr-493157073", "from": "hxtest-q263", "broadcast": 0, "data": {"txt": "<a href=\"dzh_browser_url&goto=0&type=2944&code=SZ300467&kind=1&zb=DAYRSI\" style=\"color:#3366CC;\">迅游科技(300467)</a>\n盘中 <a href=\"http://mnews.gw.com.cn/wap/data/news/xmt/2019/04/301229.html\" style=\"color:#3366CC;\">RSI超卖</a> 触发价格16.25元。", "stock": ["SZ300467"]}, "action": 1043, "showTitle": "技术事件机器人-迅游科技300467", "group": ["6022989"], "t": 1559802499331}
    # _data = {"msg_id": "gsgg-20191008_4themepioneer-test001", "from": "hxtest-q263", "broadcast": 0, "data": {"txt": "<a href=\"dzh_browser_url&goto=0&type=2970&code=SH600518&kind=1\" style=\"color:#3366CC;\">ST康美(600518)</a> 【公司公告是否重复11111111111111】20191008... <a href=\"http://www.baidu.com\" style=\"color:#3366cc;\">查看全文</a>", "stock": ["SH600518"], "showTitle": "资讯监控机器人-ST康美600518"}, "action": 1043, "group": ["2139313"], "t": 1570500578993}

    """推直播间信息"""
    # account = "hxtest-q1{n}".format(n=i)
    # roomid = "17291%02d" % i
    # k = roomid.encode("utf8")
    # # _data = {"icon":"https://dzhimage.oss-cn-hangzhou.aliyuncs.com/avatar/07b2323911f5925fe244501aa659906b163c85a7","type":"AVChatRoom","qid":"0214812362771629","serverId":"server96","nick":"5188407","valid":2,"teamid":"1729470","member":"","dzhtoken":"EPcG6c1gAB8CO7M-Fllv*VIvRWeVp-kJcQI-h9F1zwM.1583369171","sn":"/im/room/open","owner":"5188407","isprivate":0,"req_status":"200","label":"10006","deviceid":"990007180411156","version":"9.16","roomid":"1729470","ots":1583282970958,"pushurl":"http://3052.livepush.myqcloud.com/live/3052_3efa4f971ad32c84e676815dc6be7a8d.m3u8","money":"0","t":1583282974534,"name":"风雨同舟啊","paytype":0,"account":"5188407","status":1}
    # _data = {"icon":"https://dzhimage.oss-cn-hangzhou.aliyuncs.com/avatar/07b2323911f5925fe244501aa659906b163c85a7","type":"AVChatRoom","qid":"0214812362771629","serverId":"server96","nick":account,"valid":2,"teamid":roomid,"member":"","dzhtoken":"EPcG6c1gAB8CO7M-Fllv*VIvRWeVp-kJcQI-h9F1zwM.1583369171","sn":"/im/room/open","owner":"5188407","isprivate":0,"req_status":"200","label":"10006","deviceid":"990007180411156","version":"9.16","roomid":roomid,"ots":1583282970958,"pushurl":"http://3052.livepush.myqcloud.com/live/3052_3efa4f971ad32c84e676815dc6be7a8d.m3u8","money":"0","t":1583282974534,"name":"风雨同舟啊","paytype":0,"account":account,"status":1}

    """推直播间人数"""
    # k = "1729120".encode("utf8")
    # _data = {"t":1583285945509,"teamid":"172912","users":1}
    # _data = {"t":1583285945509,"teamid":"172914","users":10}
    # _data = {"t":1583285945509,"teamid":"172916","users":101}
    # _data = {"t":1583285945509,"teamid":"172918","users":1002}
    # _data = {"t":1583285945509,"teamid":"1729110","users":10003}
    # _data = {"t":1583285945509,"teamid":"1729112","users":100004}
    # _data = {"t":1583285945509,"teamid":"1729114","users":111115}
    # _data = {"t":1583285945509,"teamid":"1729116","users":11112}
    # _data = {"t":1583285945509,"teamid":"1729118","users":99}
    # _data = {"t":1583285945509,"teamid":"1729120","users":999}

    """推直播间开、关播消息"""
    # p_topic = "gwim.groups"
    # 开播
    # roomid = 1754040 + (i - 1) * 2
    # roomid = str(roomid)
    # owner = "hxtest-q3%02d" % i
    # k = roomid.encode("utf8")
    # _data = {"broadcast":1,"icon":"https://dzhimage.oss-cn-hangzhou.aliyuncs.com/avatar/66e9b487bf0cd178af7c62c101a7cdba5e351195","type":"AVChatRoom","qid":"4808878666809554","serverId":"server96","nick":"拎壺衝","valid":2,"teamid":roomid,"member":"","dzhtoken":"bBs0kHx37YQjAZLxlqYZGCl6n2BTRl7QSfPAEtNcvLM.1625708130","sn":"/im/room/open","httpdzh":"dzh-android-9.39","owner":owner,"isprivate":0,"req_status":"200","ip":"10.15.176.63","label":"10003","platformId":"3","deviceid":"864684033297991","version":"9.39","roomid":roomid,"ots":1625623250570,"pushurl":"http://3052.liveplay.myqcloud.com/live/3052_d1671797e031653046a62c06b3b24671.m3u8","money":"0","t":1625623253595,"name":"了啦啦啦啦啦啦啦啦啦啦","location":{"province":"北京市","city":"北京市","district":""},"paytype":0,"account":owner,"status":1}
    # _data = {"broadcast":1,"icon":"https://dzhimage.oss-cn-hangzhou.aliyuncs.com/avatar/66e9b487bf0cd178af7c62c101a7cdba5e351195","type":"AVChatRoom","qid":"4808878666809554","serverId":"server96","nick":"拎壺衝","valid":2,"teamid":"1754106","member":"","dzhtoken":"bBs0kHx37YQjAZLxlqYZGCl6n2BTRl7QSfPAEtNcvLM.1625708130","sn":"/im/room/open","httpdzh":"dzh-android-9.39","owner":"hxtest-q110","isprivate":0,"req_status":"200","ip":"10.15.176.63","label":"10003","platformId":"3","deviceid":"864684033297991","version":"9.39","roomid":"1754106","ots":1625623250570,"pushurl":"http://3052.liveplay.myqcloud.com/live/3052_d1671797e031653046a62c06b3b24671.m3u8","money":"0","t":1625623253595,"name":"了啦啦啦啦啦啦啦啦啦啦","location":{"province":"北京市","city":"北京市","district":""},"paytype":0,"account":"hxtest-q110","status":1}
    # 关播
    # _data = {"t":1583282665946,"teamid":roomid,"type":"AVChatRoom","delete":True}

    # producer.send(topic=p_topic, value=json.dumps(_data, ensure_ascii=False).encode("utf8"), key=k)  # 带 key

    """直播间打赏数据"""
    # p_topic = "im_room_coin"
    # roomid = "1729116"
    # _data = {"orderid":"635841780683706368","from":"hxtest-q110","to":"","time":"2020-10-20 14:08:13","type":4,"roomid":"1744414","coin":1000}

    # imtxpush
    # p_topic = "im_msg_push"
    # _data = {"callback":"","param":{"SyncOtherMachine":2,"MsgRandom":4371027,"To_Account":"hxtest-q111","From_Account":"hxtest-q242","MsgBody":[{"MsgContent":{"Text":"拎壶冲给您评论“打发打发”　<a href=\\\"dzh_browser_url&goto=0&screen=298&un=hxtest-q110&postId=5db140ae2397415f64c0c4b7&title=""&summary=欧冠-利物浦4-1击败亨克 张伯伦梅开二度萨拉赫传射\nA\nAR追风\n7小时前\n北京时间10月24日凌晨3时，2019-2020赛季欧冠小组赛E组第3轮，利物浦客场4-1击败比利时球队亨克，取得小组赛两...&cover_img=\" style=\"color:#2c8ce7;\">查看详情</a>"},"MsgType":"TIMTextElem"}],"OfflinePushInfo":{"Ext":"{\"TIMOfflinePushInfo\":\"Server\"}","Desc":"拎壶冲给您评论“打发打发”","PushFlag":1}},"url":"/openim/sendmsg"}
    # 邀约卡消息  ai_invitee_accid
    # p_topic = "ai_invitee_accid"
    # _data = {"bots":["robotomrqpymtlg","robothexjuewteh","robottqaxagkjiw","robotxssjkurpqc","robotjzululvpiu","robotcqxeuarsnc","robothdbdbzjfcf","robotvunrpblabp","robotkvidbqhtve","robotljsrxiuclf","robotikomqsfrfr","robotdmnnyivjrh","robotcxmpwhivlw","robotlvupxehpyn","robotkpvmkqrcbt","robotwrgfqjyliq","robotabaoblvlan","robotgypsyovqor","robotqegjpspmda","robottrfyylrzyh","robotqbqfhugvuf","robotacrxtvqatw","robotgrotuoxgxn","robotuenzqcmoic","robotiyxpotsehm","robotpxsammmqkg","robotogwcwxmdiq","robotgrkjhusmow","robotbzczyuywxk","robotimfmwezfgg","robotholymoywbq","robotutymuhcrlc","robotnkbusgjdom","robotinxezbpldc","robotcjhaqwiqcw","robotmplefpwmrg","robotgwodyympyc","robotitnsnrxjdm","robotbqbcwysikd","robotmznnsljopg","robotbsjcyqfkmq","robotwheqocpill","robotfffwfuxsrz","robotbrhilgmowy","robotwpyooxqtpb","robotxkivqjbpxw","robotbmnlcckayd","robotcenjcmsnbh","robotuxfwamebaz","robotucivsvcxmj","robottjexeffowj","robotkjgzwucgoi"],"propId":"7efMU5KquAAAidkEm71KFJ","sceneId":6,"invaNum":100,"groupId":"1001555","icon":"https:\/\/cimage.gw.com.cn\/image\/3acffa7734b2410ae90c35074465051c\/100","name":"拎壶冲自选股群","_tag":[],"certtype":0,"certInfo":"","stock_group":-1,"_group_type":"自选","lastMessage":"欢迎加入群聊，发现更多精彩！","receivers":["hxtest-q12400075","测试测试测试测试001","test98","hxtest-q12455366","hxtest-q12455557","yehaiyun001","hxtest-q12623086","hxtest-q12678952","test011","hxtest-q12455319","342127","lsymm","hxtest-q12679046","hxtest-q263","hxtest-q12399674","hxtest-q12455229","hxtest-q88","hxtest-q256","hxtest-q12455235","hxtest-q257","hxtest-q225","hxtest-q12456170","hxtest-q12679068","dzhrb972","hxtest-q226","hxtest-q12455816","974489","hxtest-q12455298","wzh000","hxtest-q12623076","hxtest-q12455359","test087","hxtest-q12679503","hxtest-q12679055","hxtest-q12456168","hxtest-q12400081","hxtest-q262","hxtest-q12679029","hxtest-q89","hxtest-q12455338","hxtest-q12455214","test90","hxtest-q12679049","hxtest-q258","hxtest-q253","hxtest-q12455552","hxtest-q1007","hxtest-q12678936","hxtest-q242"]}
    # _data = {"propId":"7efMU5KquAAAidkEm71KFJ","sceneId":6,"invaNum":100,"groupId":"1001555","icon":"https:\/\/cimage.gw.com.cn\/image\/3acffa7734b2410ae90c35074465051c\/100","name":"拎壶冲自选股群","_tag":[],"certtype":0,"certInfo":"","stock_group":-1,"_group_type":"自选","lastMessage":"欢迎加入群聊，发现更多精彩！","receivers":["hxtest-q12400075","测试测试测试测试001","test98","hxtest-q12455366","hxtest-q12455557","yehaiyun001","hxtest-q12623086","hxtest-q12678952","test011","hxtest-q12455319","342127","lsymm","hxtest-q12679046","hxtest-q263","hxtest-q12399674","hxtest-q12455229","hxtest-q88","hxtest-q256","hxtest-q12455235","hxtest-q257","hxtest-q225","hxtest-q12456170","hxtest-q12679068","dzhrb972","hxtest-q226","hxtest-q12455816","974489","hxtest-q12455298","wzh000","hxtest-q12623076","hxtest-q12455359","test087","hxtest-q12679503","hxtest-q12679055","hxtest-q12456168","hxtest-q12400081","hxtest-q262","hxtest-q12679029","hxtest-q89","hxtest-q12455338","hxtest-q12455214","test90","hxtest-q12679049","hxtest-q258","hxtest-q253","hxtest-q12455552","hxtest-q1007","hxtest-q12678936","hxtest-q242"]}
    # _data = {"bots":[],"propId":"9efMU5KquAAAidkEm71KFJ","sceneId":6,"invaNum":100,"groupId":"1001555","icon":"https:\/\/cimage.gw.com.cn\/image\/3acffa7734b2410ae90c35074465051c\/100","name":"拎壶冲自选股群","_tag":[],"certtype":0,"certInfo":"","stock_group":-1,"_group_type":"自选","lastMessage":"欢迎加入群聊，发现更多精彩！","receivers":["hxtest-q12400075","测试测试测试测试001","test98","hxtest-q12455366","hxtest-q12455557","yehaiyun001","hxtest-q12623086","hxtest-q12678952","test011","hxtest-q12455319","342127","lsymm","hxtest-q12679046","hxtest-q263","hxtest-q12399674","hxtest-q12455229","hxtest-q88","hxtest-q256","hxtest-q12455235","hxtest-q257","hxtest-q225","hxtest-q12456170","hxtest-q12679068","dzhrb972","hxtest-q226","hxtest-q12455816","974489","hxtest-q12455298","wzh000","hxtest-q12623076","hxtest-q12455359","test087","hxtest-q12679503","hxtest-q12679055","hxtest-q12456168","hxtest-q12400081","hxtest-q262","hxtest-q12679029","hxtest-q89","hxtest-q12455338","hxtest-q12455214","test90","hxtest-q12679049","hxtest-q258","hxtest-q253","hxtest-q12455552","hxtest-q1007","hxtest-q12678936","hxtest-q242"],"propName":"100人邀约卡","source":"1"}

    # 回调消息
    # p_topic ="txim.back.service"
    # _data = {"CallbackCommand":"Sns.CallbackFriendDelete","From_Account":"wangxiaofen001","To_Account":"hxtest-q1001","contact": "false","fromDzhAc":"wangxiaofen001","source":"Android","t":1572313063846,"toDzhAc":"hxtest-q1001"}
    #
    # 积分任务——消费 consumptionOver
    # p_topic = "yun_imtask_score"  # 内
    # k = b"hxtest-q110"
    # # _data = {"id":"0123321", "taskCode":"consumptionOver", "dt":"2019-06-27 10:17:29", "username":"hxtest-q110", "level":1, "score":"99", "aggScore":"0"}
    # # _data = {"id":"0123321", "taskCode":"consumptionOver", "dt":"2019-06-27 10:17:29", "username":"hxtest-q110", "level":1, "score":"99", "aggScore":"0"}
    # # _data = {"id":"10123240","taskCode":"consumptionOver","dt":"2019-06-27 10:17:29","username":"hxtest-q110","level":3,"score":99.0,"aggScore":0.0,"message":"购买消费"}
    # _data = {"id":"10123240","taskCode":"FollowFuwuhao","dt":"2019-06-27 10:17:29","username":"hxtest-q110","level":3,"score":99.0,"aggScore":0.0,"message":"关注服务号计积分"}

    # p_topic = "gwim_users"
    # _data = {"name":"李志飞财经主播","icon":"http://cimage.gw.com.cn/image/41a3f1f93653da50af036ba040772e2e87fa81cb/100","accid":"4366413","action":"modify","gw_user":"4366413","nick":"李志飞财经主播"}

    """股群"""
    # p_topic = "STOCK_GROUP_ADD"  # 每次写入全量数据
    # p_topic = "STOCK_GROUP_CREATE"  # 首次初始化数据和增量数据
    # _data = {"code":"SZ399001","name":"深证成指","account":"hxtest-q112","type":1}
    # _data = {"code": "SMCNY0", "name": "富时A50指数连续", "account": "hxtest-q112"}
    p_topic = "gwim.groups"
    _data = {"code": "SMCNY0", "name": "富时A50指数连续", "account": "hxtest-q112"}

    """9.9元购建群"""
    # p_topic = "purchase_index_success"
    # account = "dzh20201122"
    # t = int(time.time()*1000)
    # # t = 1605669446000
    # k = "{}".format(int(time.time()*1000000)).encode("utf8")
    # _data = {"extractor":{"o":9749434488,"s":30808444848,"e":"data02.sensors.sa","n":"access_log.2020102909","f":"(dev=fd10,ino=1618832057)","c":30808444848},"ver":2,"recv_time":1603936224728,"lib":{"$lib_method":"code","$lib_detail":"dataobj.send_sensordata##send_sensordata##/opt/sensorpaydata/common/model_payment_result.py##53","$lib":"python","$lib_version":"1.10.1"},"type":"track","time":t,"event":"purchase_index_success","distinct_id":account,"map_id":"157993204","user_id":account,"properties":{"$is_login_id":True,"$ip":"180.169.140.222","$lib_version":"1.10.1","package_value":4.95,"index_name":"抢筹先锋","platform_type":"2","package_name":"12","$lib":"python","is_success":True,"fail_reason":"NULL"},"project_id":1,"project":"production"}

    """好友推荐数据"""
    # p_topic = "auto_friend_event"
    # acc = "wangxiaofen001"
    # # acc = "hxtest-q110"
    # # acc = "lichen001"
    # from_accts = ["hxtest-q1", "hxtest-q1004", "hxtest-q110", "hxtest-q111", "hxtest-q119", "hxtest-q1006",
    #               "lucille", "fengjie001", "test113", "test114", "lucille1", "4026466", "7902287", "test097",
    #               "1441764", "wzh005", "975589", "wangxiaofen002", "hxtest-q1001", "5680591", "8834749",
    #               "hxtest-q267", "htg001", "hxtest-q13", "hxtest-q5", "wangxiaofen001", "8716788", "974489", "wzh003",
    #               "test050", "test087", "dzh161224008", "花草树木天上人间", "test098", "hxtest-q1002"]
    # # from_accts = ["test098"]
    # for from_acct in from_accts:
    #     _datas = [{"from_acct":from_acct,"to_acct":acc,"event_type":1,"source":"竞赛班:吴老师抓热点培训班群主","teamid":"6524139","msg":"TA是培训班群主"},
    #               {"from_acct":from_acct,"to_acct":acc,"event_type":2,"source":"竞赛班:吴老师抓热点培训班同学，排名第1名","teamid":"6524139","msg":"TA在本周比赛中排第X"},
    #               {"from_acct":from_acct,"to_acct":acc,"event_type":3,"source":"竞赛班:吴老师抓热点培训班同学，优秀勋章获得者","teamid":"6524139","msg":"TA获得了优秀勋章"},
    #               {"from_acct":from_acct,"to_acct":acc,"event_type":4,"source":"猜你喜欢（给ta打赏金币超过5000金币）","msg":"你给TA打赏了XX金币礼物"}]
    #     _data = random.choice(_datas)
    #     # _data = {"from_acct":from_acct,"to_acct":acc,"event_type":1,"source":"竞赛班:吴老师抓热点培训班群主","teamid":"6524139"}
    #     # _data = {"from_acct":from_acct,"to_acct":acc,"event_type":2,"source":"竞赛班:吴老师抓热点培训班同学，排名第1名","teamid":"6524139"}
    #     # _data = {"from_acct":from_acct,"to_acct":acc,"event_type":3,"source":"竞赛班:吴老师抓热点培训班同学，优秀勋章获得者","teamid":"6524139"}
    #     # _data = {"from_acct":from_acct,"to_acct":acc,"event_type":4,"source":"猜你喜欢（给ta打赏金币超过5000金币）"}
    #     # _data = {"from_acct":"dzhtest001","to_acct":"dzhzhubo001","event_type":1,"source":"竞赛班:吴老师抓热点培训班群主","teamid":"6524139"}
    #     # _data = {"from_acct":"dzhtest001","to_acct":"dzhzhubo001","event_type":2,"source":"竞赛班:吴老师抓热点培训班同学，排名第1名","teamid":"6524139"}
    #     # _data = {"from_acct":"dzhtest001","to_acct":"dzhzhubo001","event_type":3,"source":"竞赛班:吴老师抓热点培训班同学，优秀勋章获得者","teamid":"6524139"}
    #     # _data = {"from_acct":"dzhtest001","to_acct":"dzhzhubo001","event_type":4,"source":"猜你喜欢（给ta打赏金币超过5000金币）"}
    #     # result = producer.send(topic=p_topic, value=json.dumps(_data, ensure_ascii=False).encode("utf8"))
    #     result = producer.send(topic=p_topic, value=json.dumps(_data, ensure_ascii=False).encode("utf8"))
    #     print(json.dumps(_data, ensure_ascii=False))

    """学习班群加人"""
    # p_topic = "exclusive_member"  # 大数据
    # # users = ["hxtest-q1", "hxtest-q1004", "hxtest-q110", "hxtest-q111", "hxtest-q119", "hxtest-q1006",
    # #               "lucille", "fengjie001", "test113", "test114", "lucille1", "4026466", "7902287", "test097",
    # #               "曹长胜9999", "1441764", "wzh005", "975589", "wangxiaofen002", "hxtest-q1001", "5680591", "8834749",
    # #               "hxtest-q267", "htg001", "hxtest-q13", "hxtest-q5", "wangxiaofen001", "8716788", "974489", "wzh003",
    # #               "test050", "test087", "dzh161224008", "花草树木天上人间", "test098", "hxtest-q1002"]
    #
    # # users = ["hxtest-q110", "wzh003"]
    # f = "曹长胜{}"
    # _format = lambda x:  [x.format(y+1) for y in range(200)]
    # # users = _format(f)
    #
    # users = ["lichen001"]
    # # teamid = "ZH000001"
    # # teamid = "HK000001"
    # teamid = "ZH0%05d" % i
    # # _data = {"user_name":users,"teamid":teamid,"operate":"join"}
    # # _data = {"user_name":users,"teamid":teamid,"operate":"join","offset":"end"}
    # # result = producer.send(topic=p_topic, value=json.dumps(_data, ensure_ascii=False).encode("utf8"))
    # # print(json.dumps(_data, ensure_ascii=False))

    # users = ["lichen001"]
    # teamids = ["HK000001","FD000001","FD000002","FT000001","FT000002"]
    # for teamid in teamids:
    #     _data = {"user_name":users,"teamid":teamid,"operate":"join","offset":"end"}
    #     result = producer.send(topic=p_topic, value=json.dumps(_data, ensure_ascii=False).encode("utf8"))
    #     print(json.dumps(_data, ensure_ascii=False))

    # 批量加
    # x = 1000
    # z = 0
    # while z < 1000:
    #     x += 1
    #     teamid= "ZH00{}".format(x)
    #     # _data = {"user_name":users,"teamid":teamid,"operate":"join"}
    #     _data = {"user_name":users,"teamid":teamid,"operate":"join","offset":"end"}
    #     result = producer.send(topic=p_topic, value=json.dumps(_data, ensure_ascii=False).encode("utf8"))
    #     print(json.dumps(_data, ensure_ascii=False))
    #     z += 1

    """解散自选股群"""
    # g = open(r"C:\Users\hp\Desktop\imback.team_info.csv", "r").readlines()
    # gs = [_g.strip("\n") for _g in g]
    # print(gs)
    # _data = {"group": gs}
    # p_topic = "AUTO_DESTROY_TEAM"   # 解散群人数为 1的群
    # p_topic = "AUTO_DESTROY_PUBTEAM"   # 解散普通公开群
    # _data = {"group": ["6188771", "6179159", "@TGS#2GRUOTKFD", "1000767", "ZH000001", "1000949","2538221","2541175","2542763","2542263","2541137","2542095","2542211","2542693","2542733","2541505","2542133","2542043","2541003","2541717","2542005","2541105","2541017","2541141","2541581","2540999","2541047","2539351","2542207","2541735","2541133","2539213","2538229","2542467","2538059","2538273","2538149","2538977","2538073","2538191","2539891","2538243","2538115","2539995","2540969","2539563","2539319","2538497","2538193","2539975","2539365","2539363","2539457","2538217","2538215","2539519","2540981","2538267","2539895","2538101","2538209","2538795","2538355","2538695","2538201","2538641","2539317","2540961","2540869","2539161","2538175","2539203","2539065","2539361","2538239","2539821","2538777","2540991","2540927","2539119","2538667","2539453","2538847","2539113","2538307","2539277","2539195","2538085","2538743","2539153","2538729","2538385","2540997","2540983","2538329","2538491","2540785","2538593","2538091","2538505","2539919","2538277","2538477","2539951","2539081","2538063","2538067","2539141","2539873","2539307","2539055","2538043","2538949","2539047","2538117","2538111","2538165","2538093","2540883","2540905","2540823","2538205","2539135","2539719","2538445","2538183","2538279","2538257","2538341","2539811","2539109","2538377","2538219","2539979","2538295","2538413","2538103","2540967","2540941","2539831","2539447","2539127","2538097","2538359","2538147","2538507","2539337","2540839","2538105","2538319","2538523","2538275","2538185","2539357","2539095","2540879","2539905","2539217","2538051","2538291","2538053","2538335","2540959","2539565","2538395","2538581","2538351","2538473","2538157","2539437","2538753","2539405","2539103","2540921","2538249","2538119","2538525","2540977","2538079","2538049","2539335","2538113","2540011","2538409","2539283","2538851","2538285","2538361","2539003","2538373","2538317","2538283","2538539","2539651","2539793","2539423","2538263","2538655","2538269","2538605","2538255","2538071","2538389","2538451","2539479","2538045","2539041","2538407","2538095","2539507","2539745","2538401","2539605","2538535","2538371","2539251","2540947","2538365","2538501","2538427","2539817","2538333","2538415","2538055","2540819","2539373","2538325","2538643","2538127","2538531","2539637","2538397","2538237","2539151","2538515","2538993","2538421","2539569","2538417","2539049","2538955","2538463","2539819","2538381","2538827","2539981","2539475","2538159","2538339","2539421","2538173","2538459","2540963","2538195","2539019","2539833","2538383","2538745","2538131","2538163","2538299","2539253","2539967","2538061","2538649","2538121","2539445","2538313","2538189","2538639","2539903","2539429","2540933","2538555","2538069","2540929","2538627","2538259","2538253","2539397","2538109","2540939","2540875","2538509","2539345","2538541","2538099","2538145","2539045","2540935","2538213","2539325","2538125","2538203","2540007","2538337","2538211","2540987","2538537","2538963","2539057","2538481","2538375","2538469","2538735","2538297","2538281","2539033","2539521","2538107","2539713","2538771","2540931","2539809","2539059","2538327","2538153","2539279","2538565","2538467","2538495","2539597","2538479","2538347","2538739","2538223","2538403","2539915","2539021","2538155","2538551","2538135","2538311","2540005","2538343","2538779","2538503","2538287","2539929","2538087","2539973","2538303","2540943","2538521","2539815","2538363","2539997","2539617","2540985","2538345","2538457","2539505","2539913","2538161","2538133","2540949","2538139","2538143","2538411","2539329","2538309","2538057","2538247","2538483","2538083","2538891","2538137","2538357","2538123","2538141","2538151","2538075","2538171","2538169","2539685","2538543","2538485","2538235","2538129","2539233","2539917","2539641","2540881","2538557","2538065","2539297","2538207","2540895","2539463","2538601","2538081","2538529","2538241","2538041","2538331","2538181","2538391","2540955","2538447","2538187","2538399","2539879","2538405","2540957","2540841","2539067","2539273","2539077","2541025","2541941","2541373","2542253","2541507","2541479","2541215","2541747","2541345","2541011","2542349","2541029","2541873","2542135","2541107","2542695","2541005","2541799","2541343","2541551","2541099","2541333","2542159","2542069","2541817","2540953","2541015","2542529","2541009","2542003","2541559","2540995","2542299","2542317","2541713","2541939","2542469","2541911","2542139","2541127","2541865","2542689","2542545","2541545","2542581","2541853","2542477","2541861","2542547","2542645","2541699","2541761","2542111","2541835","2541901","2541977","2541795","2542125","2541451","2541103","2542625","2541773","2542051","2541563","2541185","2542491","2541881","2542599","2541625","2541565","2541341","2541579","2542119","2541635","2541069","2541621","2541093","2542191","2542195","2541243","2541585","2542627","2541163","2542419","2541261","2541041","2541671","2542447","2541659","2541619","2542185","2541049","2542527","2541605","2542697","2541349","2542483","2542517","2541723","2541657","2541929","2542721","2542265","2542227","2541775","2541725","2541301","2542285","2542607","2542735","2541789","2542157","2541179","2541287","2541239","2542161","2541593","2542309","2541117","2541449","2542357","2541253","2542047","2541409","2542503","2541777","2542247","2542321","2541223","2542653","2541829","2541975","2542335","2542643","2542755","2542649","2541171","2541571","2541035","2542731","2541129","2542777","2542573","2542535","2542523","2541481","2542379","2542371","2541863","2542327","2542453","2542375","2542495","2541071","2541075","2541039","2541115","2541509","2541387","2541431","2541381","2541471","2541415","2541241","2541643","2541707","2541841","2541919","2541957","2541857","2542049","2542107","2542173","2541085","2542037","2541539","2542669","2542079","2541603","2541295","2542065","2541963","2541733","2542345","2542369","2542519","2542571","2542273","2541161","2541203","2541379","2542325","2542229","2541083","2541303","2541279","2541503","2541331","2541649","2541969","2541765","2542081","2541651","2542323","2541321","2541311","2541335","2541561","2541395","2541271","2542471","2541367","2541101","2541245","2541063","2541521","2541157","2542023","2541729","2542439","2542601","2542275","2542199","2541393","2541755","2541113","2541701","2541897","2541907","2542243","2541921","2541499","2542591","2542641","2541997","2542255","2542235","2541517","2541831","2541183","2541803","2541227","2541739","2542481","2542075","2541439","2542395","2542377","2541669","2541247","2541947","2542217","2541359","2542425","2541467","2541821","2541769","2542213","2542667","2541353","2541661","2541369","2541781","2542543","2542443","2542497","2541591","2541425","2541809","2541951","2541293","2541269","2541125","2541469","2542061","2542549","2542147","2542501","2541925","2542031","2541607","2541007","2542167","2541743","2541213","2542347","2541001","2540965","2541019","2538793","2541119","2541741","2541577","2540993","2541059","2542485","2541169","2542691","2542449","2541193","2541067","2541633","2541383","2541749","2542699","2541289","2542577","2542267","2541869","2541177","2541511","2542619","2541371","2542315","2542295","2542605","2542055","2541543","2541631","2541051","2542683","2542465","2542109"]}
    # result = producer.send(topic=p_topic, value=json.dumps(_data, ensure_ascii=False).encode("utf8"))
    result = producer.send(topic=p_topic, value=json.dumps(_data, ensure_ascii=False).encode("utf8"))
    """解散自选股群"""
    # p_topic = "AUTO_DESTROY_TEAM"
    # _data = {"group": ["6200487"]}

    """发布短视频，发送消息 imservice消费"""
    # p_topic = "ai_shortvideo_feedback"
    # _data = {"status":0,"vid":20642,"sourceId":"5285890816814666679","taskId":"1257862591-procedurev2-568b92760188c8dd3a8b9d04d5760113t0","error":None,"checkRemark":None,"title": "标题党啊","uid": "hxtest-q111","jumpURL":"dzh_browser_url&goto=0&screen=300&vid=20642"}

    """等级变动 imservice消费 大数据 144.191"""
    # p_topic = "hx_upgrade"
    # _data = {"username": "hxtest-q110", "up_time": "2020-10-30 12:00:00", "upgrade": "41000", "grade_name": "钻石",
    #          "old_grade": "31000", "old_grade_name": "皇冠", "up_down": 1}  # 升级
    # _data = {"username":"20202020","up_time":"2020-10-30 12:00:00","upgrade":"31000","grade_name":"皇冠","old_grade":"41000","old_grade_name":"钻石","up_down":-1}  # 降级

    # result = producer.send(topic=p_topic, value=json.dumps(_data, ensure_ascii=False).encode("utf8"))
    print(json.dumps(_data, ensure_ascii=False))

    """往kafka写消息"""
    # producer.send(topic=p_topic, value=_data.encode("utf8"), key=k)
    # producer.send(topic=p_topic, value=json.dumps(_data, ensure_ascii=False).encode("utf8"), key=k)  # 带 key
    # result = producer.send(topic=p_topic, value=json.dumps(_data, ensure_ascii=False).encode("utf8"))
    # producer.send(topic="NOTIFY_DATA", value=json.dumps(ImMsgCopyJson, ensure_ascii=False).encode("utf8"))
    # print("Request Json:\n", json.dumps(ImMsgCopyJson, ensure_ascii=False))
    # print("message has sent...")
    """写kafka结果"""
    # print(result.succeeded())
    # print(result.get())

    count += 1
    i += 1
producer.close()  # 不加close，kafka收不到数据
# time.sleep(2)
print("sent %d data" % count)

"""接收kafka消息"""
# bootstrapServers = "10.15.108.93:9092,10.15.108.24:9092,10.15.108.94:9092"  # 邀请好友 评论通知
# # bootstrapServers = "10.15.108.87:9092,10.15.108.88:9092,10.15.108.90:9092"   # 慧信
# # bootstrapServers = "10.33.9.123:9092,10.33.9.213:9092,10.33.9.81:9092"  # 慧信IM
# # bootstrapServers = "10.33.9.162:9092,10.33.9.251:9092,10.33.9.206:9092"  # 慧信朋友圈
# # consumerTopic = "product.booking.topic"
# consumerTopic = "gwim_friend"  # WAIT_VERIFY_DATA  NOTIFY_DATA  im_invite im_card_used  WAIT_SAVE_DATA txim_back_service
# consumer = KafkaConsumer(consumerTopic, group_id="hx.event.kafkaTest.groupid",
#                          bootstrap_servers=bootstrapServers,
#                          enable_auto_commit=True,
#                          auto_commit_interval_ms=1000)
# print("received message:")
# for message in consumer:
#     if message is not None:
#         # print("received message: \n", message.value, message.offset)
#         # print(message.topic, message.partition, message.offset, str(message.key, encoding="utf-8"),
#         #       str(message.value, encoding="utf-8"))
#         print(message.offset, str(message.value, encoding="utf-8"))
# # 问题: 1.注释掉接收消息代码，鸟问推送接收不到数据  send完加上producer.close()可解决 2.consumer不会自动停止
# # 用 pykafka
