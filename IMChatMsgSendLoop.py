#! /usr/bin/python
# coding:utf-8

import json
import time
import requests
import urllib.parse
import random
import hashlib


def _md5(bts):
    m = hashlib.md5()
    if isinstance(bts, bytes):
        m.update(bts)
    elif isinstance(bts, str):
        m.update(bts.encode("utf-8"))
    return m.hexdigest()


class ImRequest:
    def __int__(self):
        pass

    @classmethod
    def request_send(self, request_url, request_dict, request_msg):
        headers = {"Content-Type": "application/json"}
        request_url = "%s?%s" % (request_url, urllib.parse.urlencode(request_dict))
        print("request url:", request_url)
        _request = requests.post(request_url, data=json.dumps(request_msg), headers=headers)
        _response = eval(_request.content.decode("utf-8"))
        if _request.status_code != 200:
            print("Error Information: ", _request.status_code, _request.reason)
        else:
            print("response: ", _response)
            if _response["ErrorCode"] == 0:
                return True
            else:
                return False

if __name__ == "__main__":
    environment = "product2"
    if environment == "product":
        # product
        IDENTIFIER = "ywbadmin"
        SDKAPPID = 1400124969
        sig = "eJw9ztFOgzAYBeBXWbidMW1XoJjsgqFRlpEFx*LkhhRa3C9QELpNZnx3BYO35zs5OV9GtNnd8iyrT0onum*kcTczCMOmcTMbDYRUGnKQ7SD9JeWiAjUpbxoQCdfJohWDT3knimS0IcQUIUyoYzkTy88GWpnwXP-NLjBGvyU0*Vm2HdRq-IKwiQmiE2moxo-YcojFkGP-SwdvAwQPoee72-nGrrzM3l9FcJAf8e45KN8JS8ti9UTLvFtTtd2f2Fzcu7BC6fp4ZL6ZHcKwTqOeRKYlwvzRf4XYCnoWF8p7OaPM9S7LpfH9Ax9uWf0_"
    else:
        # test
        IDENTIFIER = "dzh-admin"
        SDKAPPID = 1400007088
        ACCTYPE = 2815
        sig = "eJw9zl1vgjAUBuC-Yrjdhy1QwN2ZOhY2nYIfQW9IQ4ttFiorZZGa-fcNlu5cvs*bc87N2S23j6QsL53Uhe4b5jxNHDeCyLmfjCYok1pUgqlBqOEPhNZCWiZNI2hBdOEpOhRs3tKPYrQhhD74nRBEkWV2bYRiBan0314PQjCUrH8x1YqLHJ8BEEEX*Ja0qMcnYTBzgwjMUPB-U5wHWD0fcZJiznIc62n2tqirA*0NvvYZDLBBm0XPyB6XW1keUxO*yjTh803GcxXGPo-WWdJ13Czv5mfv83B6Vy-rPm8bhk5ITWlMVs73D5FoW3c_"

    url_params = dict()
    url_params["usersig"] = sig
    url_params["identifier"] = IDENTIFIER
    url_params["sdkappid"] = SDKAPPID
    url_params["random"] = int(time.time())
    url_params["contenttype"] = "json"

    # 创建发送消息对象
    im_request = ImRequest()
    # 单聊消息url
    single_message_url = "https://console.tim.qq.com/v4/openim/sendmsg"
    # 批量发单聊消息
    batch_message_url = "https://console.tim.qq.com/v4/openim/batchsendmsg"
    # 群组消息url
    group_message_url = "https://console.tim.qq.com/v4/group_open_http_svc/send_group_msg"

    # 消息体定义
    # MsgBody = list()
    TextMsgBody = dict()
    TextMsgContent = dict()
    FaceMsgBody = dict()
    FaceMsgContent = dict()
    CustomMsgBody = dict()
    CustomMsgContent = dict()

    # 文本消息
    TextMsgBody["MsgType"] = "TIMTextElem"
    TextMsgContent["Text"] = "岂曰无衣？七兮。不如子之衣，安且吉兮。\n岂曰无衣？六兮。不如子之衣，安且燠兮。"

    TextMsgBody["MsgContent"] = TextMsgContent

    # 表情消息
    FaceMsgBody["MsgType"] = "TIMFaceElem"
    FaceMsgContent["Index"] = 3
    FaceMsgContent["Data"] = "\u2602\u3299\u2600\u2611\u270A\u261D"
    FaceMsgContent["Data"] = "[害羞]"
    FaceMsgBody["MsgContent"] = FaceMsgContent

    # 自定义消息
    imgs = ["https://newmnews.gw.com.cn/uploaded/image/2018/12/04/5c064489e13823961190d079.jpg",
            "https://newmnews.gw.com.cn/uploaded/image/2018/12/04/5c06448de13823961190d07a.jpg",
            "https://newmnews.gw.com.cn/uploaded/image/2018/12/05/5c076b6ee13823961190d07b.jpg",
            "https://newmnews.gw.com.cn/uploaded/image/2018/12/05/5c077127e13823961190d07c.jpg",
            "https://newmnews.gw.com.cn/uploaded/image/2018/12/05/5c07712fe13823961190d07d.jpg",
            "https://newmnews.gw.com.cn/uploaded/image/2018/12/05/5c07714be13823961190d07e.jpg",
            "https://newmnews.gw.com.cn/uploaded/image/2018/12/05/5c077150e13823961190d07f.jpg",
            "https://newmnews.gw.com.cn/uploaded/image/2018/12/08/5c0b7146e13823961190d081.jpg",
            "https://newmnews.gw.com.cn/uploaded/image/2018/12/08/5c0b714ce13823961190d082.jpg",
            "https://newmnews.gw.com.cn/uploaded/image/2018/12/08/5c0b71a5e13823961190d083.jpg",
            "https://newmnews.gw.com.cn/uploaded/image/2018/12/08/5c0b71a9e13823961190d084.jpg",
            "https://newmnews.gw.com.cn/uploaded/image/2018/12/08/5c0b7324e13823961190d085.jpg",
            "https://newmnews.gw.com.cn/uploaded/image/2018/12/08/5c0b7327e13823961190d086.jpg"
            ]

    videos = ["https://newmnews.gw.com.cn/uploaded/video/2018/08/06/5b68388ae13823b2b8d20665.mp4",
              "https://newmnews.gw.com.cn/uploaded/video/2018/08/06/5b683663e13823b2b8d20664.mp4",
              "https://newmnews.gw.com.cn/uploaded/video/2018/08/04/5b655ff5e13823b2b8d20558.mp4",
              "https://newmnews.gw.com.cn/uploaded/tim/2018/08/03/5b640080e13823b2b8d204eb.mp4",
              "https://newmnews.gw.com.cn/uploaded/video/2018/08/03/5b63f280e13823b2b8d204d3.mp4",
              "https://newmnews.gw.com.cn/uploaded/video/2018/08/03/5b63f1f0e13823b2b8d204cd.mp4",
              "https://newmnews.gw.com.cn/uploaded/video/2018/08/03/5b63f1c8e13823b2b8d204cc.mp4",
              "https://newmnews.gw.com.cn/uploaded/tim/2018/10/10/5bbdb78ae13823961190cf23.mp4",
              "https://newmnews.gw.com.cn/uploaded/tim/2018/07/21/5b52d904e13823dced53ba36.mp4",
              "https://newmnews.gw.com.cn/uploaded/tim/2018/07/21/5b52da41e13823dced53ba38.mp4"]

    audios = ["https://newmnews.gw.com.cn/uploaded/tim/2018/09/27/5baccf60e13823961190cea0.acc",
              "https://newmnews.gw.com.cn/uploaded/tim/2018/09/27/5baccfe2e13823961190cea2.acc",
              "https://newmnews.gw.com.cn/uploaded/tim/2018/10/15/5bc3ef18e13823961190cf3f.acc",
              "https://newmnews.gw.com.cn/uploaded/tim/2018/10/15/5bc3ef52e13823961190cf40.acc",
              "https://newmnews.gw.com.cn/uploaded/tim/2018/10/15/5bc405c7e13823961190cf43.acc",
              "https://newmnews.gw.com.cn/uploaded/tim/2018/10/15/5bc43adfe13823961190cf4a.acc",
              "https://newmnews.gw.com.cn/uploaded/tim/2018/10/15/5bc43cb2e13823961190cf4b.acc",
              "https://newmnews.gw.com.cn/uploaded/tim/2018/10/15/5bc43d12e13823961190cf4c.acc",
              "https://newmnews.gw.com.cn/uploaded/tim/2018/10/15/5bc45a9be13823961190cf4e.acc",
              "https://newmnews.gw.com.cn/uploaded/tim/2018/10/15/5bc45ae7e13823961190cf4f.acc",
              "https://newmnews.gw.com.cn/uploaded/tim/2018/10/16/5bc5a5a0e13823961190cf63.acc",
              "https://newmnews.gw.com.cn/uploaded/tim/2018/10/16/5bc5a5b3e13823961190cf64.acc",
              "https://newmnews.gw.com.cn/uploaded/tim/2018/10/16/5bc5dcfbe13823961190cf65.acc"]

    # CustomMsgData = [{"userAction":1014,"actionParam":"{\"data\":{\"md5\":\"79243f2217f313fedf41d5d381eb280c\",\"ext\":\"jpg\",\"h\":226,\"size\":33439,\"w\":450,\"name\":\"图⽚发送于2018-12-10 19:21\",\"url\":\"https://newmnews.gw.com.cn/uploaded/tim/2018/07/18/5b4f229de138230800d7c939.jpg\"}}"},
    #                  {"userAction":1015,"actionParam":"{\"data\":{\"size\":19930,\"ext\":\"aac\",\"dur\":4,\"url\":\"https://newmnews.gw.com.cn/uploaded/tim/2018/07/18/5b4f1a39e138230800d7c938.aac\", \"md5\":\"b0436666fb4801a048189b58c06342d0\"}}"},
    #                  {"userAction":1016,"actionParam":"{\"data\":{\"url\":\"https://newmnews.gw.com.cn/uploaded/tim/2018/07/18/5b4f22fce138230800d7c93a.mp4\",\"md5\":\"643b98e7b319dd49f5103fcb1d5732d2\",\"ext\":\"mp4\",\"h\":568,\"size\":280918,\"w\":320,\"dur\":2}}"}]

    # CustomMsgData = {"userAction":1014,"actionParam":{"data":{"md5":"79243f2217f313fedf41d5d381eb280c","ext":"jpg","h":226,"size":33439,"w":450,"name":"图⽚发送于2018-07-18 19:21","url":"https://newmnews.gw.com.cn/uploaded/tim/2018/07/18/5b4f229de138230800d7c939.jpg"}}}
    # CustomMsgData = {"userAction":1015,"actionParam":{"data":{"size":19930,"ext":"aac","dur":4,"url":"https://newmnews.gw.com.cn/uploaded/tim/2018/07/18/5b4f1a39e138230800d7c938.aac", "md5":"b0436666fb4801a048189b58c06342d0"}}}
    # CustomMsgData = {"userAction":1016,"actionParam":{"data":{"url":"https://newmnews.gw.com.cn/uploaded/tim/2018/07/18/5b4f22fce138230800d7c93a.mp4","md5":"643b98e7b319dd49f5103fcb1d5732d2","ext":"mp4","h":568,"size":280918,"w":320,"dur":2}}}
    # # CustomMsgData = {"userAction":1005,"actionParam":{"CMdata":{"title":"星期五","subTitle":"大红包","redPacketId":213213,"redPacketType":1,"reqNo":1233213,"userlist":[],"amount":10}}}
    CustomMsgBody["MsgType"] = "TIMCustomElem"
    # CustomMsgContent["Data"] = json.dumps(CustomMsgData, ensure_ascii=False)
    CustomMsgBody["MsgContent"] = CustomMsgContent

    # 消息体列表
    # MsgBody.append(TextMsgBody)   # 文本
    # MsgBody.append(FaceMsgBody)   # 表情
    # MsgBody.append(CustomMsgBody)   # 自定义
    # _MsgBody = random.choice([TextMsgBody, CustomMsgBody])
    # MsgBody.append(_MsgBody)

    accs = ["hxtest-q119","lucille", "wangxiaofen001", "wangxiaofen002", "test112", "test113", "test092", "test114", "test115", "hxtest-q110", "hxtest-q1001", "hxtest-q1006", "8834749", "lucille1", "8716788", "20202020", "20202022", "20202021", "20202023", "527787", "134890", "3362445", "chdtest002", "chdtest001", "hxtest-q6040"]
    # From_Account = random.choice(accs)
    From_Account = "hxtest-q{}".format(random.randint(1, 1100))
    To_Account = "ioslsy00"
    # To_Account = "abc100"
    # To_Account = ["hxtest-q110", "lucillesun"]  # 批量发消息
    GroupId = "6341835"   # 1002143 @TGS#2ZYCDNLF2
    # GroupId = "1750674"
    # GroupIds = ["1174059", "1174061", "1002761"]
    GroupIds = ["6341859", "6341861", "6341863", "6341865", "6341867", "6341869", "6341871", "6341873", "6341875",
                "6341877", "6341879", "6341881", "6341883", "6341885", "6341887", "6341889", "6341891", "6341893",
                "6341895", "6341897", "6341899", "6341901", "6341903", "6341905", "6341907", "6341909", "6341911",
                "6341913", "6341915", "6341917", "6341919", "6341921", "6341923", "6341925", "6341927", "6341929",
                "6341931", "6341933", "6341935", "6341937", "6341939", "6341941", "6341943", "6341945", "6341947",
                "6341949", "6341951", "6341953", "6341955", "6341957", "6341959", "6341961", "6341963", "6341965",
                "6341967", "6341969", "6341971", "6341973", "6341975", "6341977", "6341979", "6341981", "6341983",
                "6341985", "6341987", "6341989", "6341991", "6341993", "6341995", "6341997", "6341999", "6342001",
                "6342003", "6342005", "6342007", "6342009", "6342011", "6342013", "6342015", "6342017", "6342019",
                "6342021", "6342023", "6342025", "6342027", "6342029", "6342031", "6342033", "6342035", "6342037",
                "6341857", "6341855", "6341853", "6341851", "6341849", "6341847", "6341845", "6341843", "6341841",
                "6341839", "6341835"]
    loops = 1
    n = 1
    while True:
        MsgBody = list()
        # _MsgBody = random.choice([TextMsgBody, CustomMsgBody])  # 随机选择文本/自定义消息
        MsgBody.append(CustomMsgBody)  # 自定义消息
        # MsgBody.append(TextMsgBody)   # 文本消息
        # imgUrl = "https://newmnews.gw.com.cn/uploaded/image/2018/12/04/5c064489e13823961190d079.jpg"
        imgUrl = random.choice(imgs)
        # videoUrl = "https://newmnews.gw.com.cn/uploaded/video/2018/08/06/5b683663e13823b2b8d20664.mp4"
        # videoUrl = "https://newmnews.gw.com.cn/uploaded/video/2018/08/06/5b68388ae13823b2b8d20665.mp4"
        videoUrl = random.choice(videos)
        audioUrl = random.choice(audios)

        CustomMsgData = [{"userAction": 1014,
                          "actionParam": "{\"data\":{\"md5\":\"%s\",\"ext\":\"jpg\",\"h\":4608,\"size\":4022577,\"w\":3456,\"name\":\"图⽚发送于2018-12-10 19:21\",\"url\":\"%s\"}}" % (
                              _md5("%s%s" % (imgUrl, random.randint)), imgUrl)},
                         {"userAction": 1015,
                          "actionParam": "{\"data\":{\"size\":19930,\"ext\":\"aac\",\"dur\":7,\"url\":\"%s\", \"md5\":\"%s\"}}" % (
                              audioUrl, _md5("%s%s" % (audioUrl, random.randint)))},
                         {"userAction": 1016,
                          "actionParam": "{\"data\":{\"url\":\"%s\",\"md5\":\"%s\",\"ext\":\"mp4\",\"h\":480,\"size\":21294783,\"w\":864,\"dur\":4}}" % (
                              videoUrl, _md5("%s%s" % (videoUrl, random.randint)))}]

        content = CustomMsgData[random.choice([0, 2])]
        # content = random.choice(CustomMsgData)
        # content = CustomMsgData[0]
        # print(content)
        CustomMsgContent["Data"] = json.dumps(content, ensure_ascii=False)
        # CustomMsgContent["Data"] = json.dumps(random.choice(CustomMsgData), ensure_ascii=False)

        # TextMsgContent["Text"] = """%s. 岂曰无衣？七兮。不如子之衣，安且吉兮。\u261D
        # 岂曰无衣？六兮。不如子之衣，安且燠兮。\u261D[害羞]""" % n
        """单聊消息"""
        # SingleMsgParams = dict()
        # SingleMsgParams["SyncOtherMachine"] = 1
        # SingleMsgParams["From_Account"] = "hxtest-q{user}".format(user=n)  # 指定发送账号，无此字段默认管理员发送
        # SingleMsgParams["To_Account"] = "ioslsy00"
        # SingleMsgParams["MsgLifeTime"] = 600
        # SingleMsgParams["MsgRandom"] = int(time.time())
        # SingleMsgParams["MsgTimeStamp"] = int(time.time())
        # SingleMsgParams["MsgBody"] = MsgBody
        # print("single message:", SingleMsgParams)
        # if isinstance(To_Account, str):
        #     send_msg_response = im_request.request_send(single_message_url, url_params, SingleMsgParams)  # 单发
        # else:
        #     send_msg_response = im_request.request_send(batch_message_url, url_params, SingleMsgParams)   # 批量发
        # if send_msg_response:
        #     print("single message %s send successful..." % n)
        # else:
        #     print("single message %s send failed..." % n)

        """群组消息"""

        for GroupId in GroupIds:
            GroupMsgParams = dict()
            GroupMsgParams["GroupId"] = GroupId   # 1002143 @TGS#2ZYCDNLF2
            GroupMsgParams["From_Account"] = From_Account  # 指定发送账号，不指定时默认管理员发送
            GroupMsgParams["Random"] = int(time.time())
            GroupMsgParams["MsgBody"] = MsgBody
            # print(GroupMsgParams)

            send_msg_response = im_request.request_send(group_message_url, url_params, GroupMsgParams)
            if send_msg_response:
                print("group message %s send successful..." % n)
            else:
                print("group message %s send failed..." % n)

        # GroupMsgParams = dict()
        # GroupMsgParams["GroupId"] = GroupId   # 1002143 @TGS#2ZYCDNLF2
        # GroupMsgParams["From_Account"] = From_Account  # 指定发送账号，不指定时默认管理员发送
        # GroupMsgParams["Random"] = int(time.time())
        # GroupMsgParams["MsgBody"] = MsgBody
        # GroupMsgParams["OfflinePushInfo"] = {"PushFlag":0,"Desc":"离线推送内容","Ext":"这是透传的内容","AndroidInfo":{"Sound":"android.mp3"},"ApnsInfo":{"Sound":"apns.mp3","BadgeMode":1,"Title":"apnstitle","SubTitle":"apnssubtitle","Image":"www.image.com"}}
        # print(GroupMsgParams)
        #
        # send_msg_response = im_request.request_send(group_message_url, url_params, GroupMsgParams)
        # if send_msg_response:
        #     print("group message %s send successful..." % n)
        # else:
        #     print("group message %s send failed..." % n)

        n += 1
        loops -= 1
        time.sleep(3)


