#! /usr/bin/python
# coding:utf-8

import json
import time
import requests
import urllib.parse


class ImRequest:
    def __int__(self):
        pass

    @classmethod
    def request_send(self, request_url, request_dict, request_msg):
        headers = {"Content-Type": "application/json"}
        request_url = "%s?%s" % (request_url, urllib.parse.urlencode(request_dict))
        print("request url:", request_url)
        print("request data:", json.dumps(request_msg).replace(" ",""))
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


if __name__ == "__main__":
    environment = "production2"
    if environment == "production":
        # product
        IDENTIFIER = "ywbadmin"
        SDKAPPID = 1400124969
        sig = "eJw9ztFugjAUBuBXMb1eZgst6u6YuAnDMFPnpjeko0UKoSBUFM3efcLCzuX-nZzz38DGp48sioqT0qFuSwGeRsCYIgIeRr1JLpSWsRRVJ*35m-FcqkFZWUoeMh2aFe98yGuehb11IcIQIgPPrNnA4lLKSoQs1n9nTYTgfQkO3oiqloXqu0BEkAHxQFrmfUdkETwh9zH-f8pDB6vFbu6unbfkK83WdLn7oFETE3*cHL1XbBtFvWdX*uJJ99kdk0PtBLab2H6b6M-NdpVfm*0Ec3qqrXPiweB9MV02rppHyjumFycL9in4*QVJZVtN"
    else:
        # test
        IDENTIFIER = "dzh-admin"
        SDKAPPID = 1400007088
        ACCTYPE = 2815
        sig = "eJw9zl1PgzAUBuC-snA7P1pKHXqHUwmmxky2AbtpCi2jDBgrHfgR-7uCqefyfd5zcr6sNQmvWJYdz42m*qMV1t3Msl2IrYvZZJKLRstcCjUK-ywuGa9lY5i1reSUaYoUHwsm7-iBTjaG0AG-swCua1i8t1IJynL9dxdBCMaS8V6oTh6b6RkAMbSBY0jLenoS3mBngTFG-0ud3I-w8pgsg9XDtudRuk2rqI*TayJOfgXjjKH7jUNUuNsoe07KdVnHceAFhffslVlEUFI9vZbL4S1vV*wE50MVeXuShudb39*JwTsUTCXW9w9-9Ft4"

    url_params = dict()
    url_params["usersig"] = sig
    url_params["identifier"] = IDENTIFIER
    url_params["sdkappid"] = SDKAPPID
    url_params["random"] = int(time.time())
    url_params["contenttype"] = "json"

    # 发送消息对象
    im_request = ImRequest()

    # 单聊消息url
    single_message_url = "https://console.tim.qq.com/v4/openim/sendmsg"
    # 批量发单聊消息
    batch_message_url = "https://console.tim.qq.com/v4/openim/batchsendmsg"
    # 群组消息url
    group_message_url = "https://console.tim.qq.com/v4/group_open_http_svc/send_group_msg"

    # 消息体定义
    MsgBody = list()
    TextMsgBody = dict()
    TextMsgContent = dict()
    FaceMsgBody = dict()
    FaceMsgContent = dict()
    CustomMsgBody = dict()
    CustomMsgContent = dict()

    # 文本消息
    TextMsgBody["MsgType"] = "TIMTextElem"
    TextMsgContent["Text"] = "岂曰无衣？七兮。不如子之衣，安且吉兮。\n岂曰无衣？六兮。不如子之衣，安且燠兮。[色]"
    TextMsgContent["Text"] = "关关雎鸠，在河之洲。窈窕淑女，君子好逑。\n" \
                             "参差荇菜，左右流之。窈窕淑女，寤寐求之。\n" \
                             "求之不得，寤寐思服。悠哉悠哉，辗转反侧。\n" \
                             "参差荇菜，左右采之。窈窕淑女，琴瑟友之。\n" \
                             "参差荇菜，左右芼之。窈窕淑女，钟鼓乐之。\n"
    # TextMsgContent["Text"] = "岂曰无衣？七兮。不如子之衣，安且吉兮。\n" \
    #                          "岂曰无衣？六兮。不如子之衣，安且燠兮。\n[色][害羞]"  # 表情
    TextMsgBody["MsgContent"] = TextMsgContent

    # 表情消息
    FaceMsgBody["MsgType"] = "TIMFaceElem"
    FaceMsgContent["Index"] = 3
    FaceMsgContent["Data"] = "\u2602\u3299\u2600\u2611\u270A\u261D"
    FaceMsgContent["Data"] = "[害羞]"
    FaceMsgBody["MsgContent"] = FaceMsgContent

    # 自定义消息
    CustomMsgData = {"userAction":1014,"actionParam":{"data":{"md5":"79243f2217f313fedf41d5d381eb280c","ext":"jpg","h":226,"size":33439,"w":450,"name":"图⽚发送于2018-07-18 19:21","url":"https://newmnews.gw.com.cn/uploaded/tim/2018/07/18/5b4f229de138230800d7c939.jpg"}}}
    CustomMsgData = {"userAction":1015,"actionParam":{"data":{"size":19930,"ext":"aac","dur":4,"url":"https://newmnews.gw.com.cn/uploaded/tim/2018/07/18/5b4f1a39e138230800d7c938.aac", "md5":"b0436666fb4801a048189b58c06342d0"}}}
    CustomMsgData = {"userAction":1016,"actionParam":{"data":{"url":"https://newmnews.gw.com.cn/uploaded/tim/2018/07/18/5b4f22fce138230800d7c93a.mp4","md5":"643b98e7b319dd49f5103fcb1d5732d2","ext":"mp4","h":568,"size":280918,"w":320,"dur":2}}}
    # CustomMsgData = {"userAction":1005,"actionParam":{"CMdata":{"title":"星期五","subTitle":"大红包","redPacketId":"213213","type":11,"reqNo":"1233213","userlist":[],"amount":10}}}
    CustomMsgBody["MsgType"] = "TIMCustomElem"
    CustomMsgContent["Data"] = json.dumps(CustomMsgData, ensure_ascii=False)
    CustomMsgBody["MsgContent"] = CustomMsgContent

    # 消息体列表
    # MsgBody.append(TextMsgBody)   # 文本
    # MsgBody.append(FaceMsgBody)   # 表情
    MsgBody.append(CustomMsgBody)   # 文本

    From_Account = "hxtest-q118"
    # To_Account = "dragon2014"

    # From_Account = "lucille"
    # To_Account = "zw717038"
    # To_Account = "abc100"
    # To_Account = "花草树木天上人间"
    To_Account = ["alsy00"]  # 批量发消息

    """单聊消息"""
    SingleMsgParams = dict()
    SingleMsgParams["SyncOtherMachine"] = 1
    SingleMsgParams["From_Account"] = From_Account  # 指定发送账号，无此字段默认管理员发送
    SingleMsgParams["To_Account"] = To_Account
    SingleMsgParams["MsgLifeTime"] = 600
    SingleMsgParams["MsgRandom"] = int(time.time())
    SingleMsgParams["MsgTimeStamp"] = int(time.time())
    SingleMsgParams["MsgBody"] = MsgBody
    SingleMsgParams["OfflinePushInfo"] = {"PushFlag": 0}  # 0表示推送，1表示不离线推送
    # print("single message:", SingleMsgParams)

    # if isinstance(To_Account, str):
    #     send_msg_response = im_request.request_send(single_message_url, url_params, SingleMsgParams)  # 单发
    # else:
    #     send_msg_response = im_request.request_send(batch_message_url, url_params, SingleMsgParams)   # 批量发
    # if send_msg_response:
    #     print("single message send successful...")
    # else:
    #     print("single message send failed...")

    """发送群组消息"""
    GroupMsgParams = dict()
    GroupMsgParams["GroupId"] = "1237057"   # 1002143 @TGS#2ZYCDNLF2
    GroupMsgParams["From_Account"] = From_Account  # 指定发送账号，不指定时默认管理员发送
    GroupMsgParams["Random"] = int(time.time())
    GroupMsgParams["MsgBody"] = MsgBody

    # print("group message:", GroupMsgParams)
    # send_msg_response = im_request.request_send(group_message_url, url_params, GroupMsgParams)
    # if send_msg_response:
    #     print("group message send successful...")
    # else:
    #     print("group message send failed...")

    """操作"""
    # 删除好友
    friend_delete = "https://console.tim.qq.com/v4/sns/friend_delete"
    # 删除所有好友
    friend_del_all = "https://console.tim.qq.com/v4/sns/friend_delete_all"
    # 解散群组
    destroy_group_url = "https://console.tim.qq.com/v4/group_open_http_svc/destroy_group"

    """好友关系"""
    friend_check_url = "https://console.tim.qq.com/v4/sns/friend_check"
    FriendCheckParams = dict()
    FriendCheckParams["From_Account"] = "92750302"  # lsym
    FriendCheckParams["To_Account"] = ["wuxjdzh800"]  # 110569450
    FriendCheckParams["CheckType"] = "CheckResult_Type_Both"
    # 单向校验 CheckResult_Type_Singal  双向校验 CheckResult_Type_Both
    # friend_check_response = im_request.request_send(friend_check_url, url_params, FriendCheckParams)

    """拉取好友"""
    friend_get_all_url = "https://console.tim.qq.com/v4/sns/friend_get_all"
    FriendGetAllParams = dict()
    FriendGetAllParams["From_Account"] = "zbt3547"  # lsym
    FriendGetAllParams["TimeStamp"] = 0
    FriendGetAllParams["StartIndex"] = 0
    FriendGetAllParams["TagList"] = ["Tag_Profile_IM_Nick", "Tag_SNS_IM_Group", "Tag_SNS_IM_Remark"]
    FriendGetAllParams["LastStandardSequence"] = 0
    # FriendGetAllParams["GetCount"] = 100
    # friend_get_all_response = im_request.request_send(friend_get_all_url, url_params, FriendGetAllParams)
    # accounts = list()
    # for item in friend_get_all_response["InfoItem"]:
    #     accounts.append(item["Info_Account"])
    # print(accounts)

    friend_get_url = "https://console.tim.qq.com/v4/sns/friend_get"
    FriendGetParams = dict()
    FriendGetParams["From_Account"] = "hxtest-q110"
    FriendGetParams["StartIndex"] = 0
    # friend_get_response = im_request.request_send(friend_get_all_url, url_params, FriendGetAllParams)

    """删除好友    *** 谨慎使用"""
    # friend_delete_url = "https://console.tim.qq.com/v4/sns/friend_delete"
    # FriendDeleteParams = dict()
    # FriendDeleteParams["From_Account"] = "4b9d67d894d7dce47607b503ae430871"  # lsym
    # FriendDeleteParams["To_Account"] = ["hxtest-q1004"]
    # FriendDeleteParams["DeleteType"] = "Delete_Type_Both"
    # 单向删除 Delete_Type_Single   双向删除 Delete_Type_Both
    # friend_check_response = im_request.request_send(friend_delete_url, url_params, FriendDeleteParams)

    """添加好友"""
    friend_add_url = "https://console.tim.qq.com/v4/sns/friend_add"
    FriendAddParams = dict()
    FriendAddParams["From_Account"] = "test21"
    FriendAddParams["AddFriendItem"] = list()
    FriendAddSubParams = dict()
    FriendAddSubParams["To_Account"] = "342127"
    FriendAddSubParams["AddSource"] = "AddSource_Type_Android"
    FriendAddParams["AddFriendItem"].append(FriendAddSubParams)
    # print(FriendAddParams)
    # friend_check_response = im_request.request_send(friend_add_url, url_params, FriendAddParams)

    # """批量加好友"""
    # from pymongo import MongoClient
    # # 查询mongo里有效账号
    # conn = MongoClient(host='10.15.108.23', port=27017)
    # db = conn.imback  # 连接 imback 数据库，没有则自动创建 db = conn["optionalstock"]
    # db.authenticate(name='root', password='root', source='admin')   # 密码权限认证
    # collectionNames = db.collection_names()  # 取所有集合名称
    # # print("集合列表:\n", collectionNames)
    # collection = db['user_info']
    # count = 0
    # for item in collection.find({}).limit(400):
    # # for item in collection.find({"accid": re.compile("hxtest-q*")}).limit(400):
    # # for item in collection.find({"accid": {"$nin": [re.compile("hxtest*"), re.compile("wps*")]}}):
    #     # print(item["accid"], type(item))
    #     if "accid" in item and 0 < len(item["accid"]) < 32:
    #         # print(item["accid"])
    #         # print(chardet.detect(item["accid"].encode("utf-8")))  # 检查编码
    #         if count == 201:
    #             break
    #         FriendAddParams["From_Account"] = item["accid"]
    #         print(FriendAddParams)
    #         friend_check_response = im_request.request_send(friend_add_url, url_params, FriendAddParams)

    """设置全局禁言"""
    # set_no_speaking_url = "https://console.tim.qq.com/v4/openconfigsvr/setnospeaking"
    # SetNoSpeakingParams = dict()
    # SetNoSpeakingParams["Set_Account"] = "hxtest-q110"  # dzh155441977  262310025  625925136
    # SetNoSpeakingParams["C2CmsgNospeakingTime"] = 86400  # 单聊消息禁言时间
    # SetNoSpeakingParams["GroupmsgNospeakingTime"] = 86400  # 群组消息禁言时间
    # print("*************设置全局禁言*************")
    # set_no_speaking_response = im_request.request_send(set_no_speaking_url, url_params, SetNoSpeakingParams)

    """查询全局禁言"""
    get_no_speaking_url = "https://console.tim.qq.com/v4/openconfigsvr/getnospeaking"
    GetNoSpeakingParams = dict()
    GetNoSpeakingParams["Get_Account"] = "1242267 "  # dzh155441977  262310025  625925136
    get_no_speaking_response = im_request.request_send(get_no_speaking_url, url_params, GetNoSpeakingParams)

    """拉取群漫游消息"""
    # group_msg_get_simple_url = "https://console.tim.qq.com/v4/group_open_http_svc/group_msg_get_simple"
    # GroupMsgGetParams = dict()
    # GroupMsgGetParams["GroupId"] = "1237105"  # 群主的UserId（选填）
    # GroupMsgGetParams["ReqMsgNumber"] = 1   # 群组类型：Private/Public/ChatRoom/AVChatRoom/BChatRoom（必填）
    # print("*************拉取群漫游消息*************")
    # group_msg_get_response = im_request.request_send(group_msg_get_simple_url, url_params, GroupMsgGetParams)

    """拉取资料"""
    portrait_get_url = "https://console.tim.qq.com/v4/profile/portrait_get"
    PortraitGetParams = dict()
    PortraitGetParams["To_Account"] = ["801941856", "23718780"]   # 178554
    PortraitGetParams["TagList"] = ["Tag_Profile_IM_Nick", "Tag_Profile_IM_AllowType",
                                    "Tag_Profile_IM_SelfSignature", "Tag_Profile_IM_Image",
                                    "Tag_Profile_Custom_UStatus", "Tag_Profile_IM_AdminForbidType",
                                    "Tag_Profile_Custom_UserCert"]
    # portrait_get_response = im_request.request_send(portrait_get_url, url_params, PortraitGetParams)

    """添加黑名单"""
    # black_list_add_url = "https://console.tim.qq.com/v4/sns/black_list_add"
    # BlackListAddParams = dict()
    # BlackListAddParams["From_Account"] = "hxtest-q110"
    # BlackListAddParams["To_Account"] = ["hxtest-q1006"]
    # get_no_speaking_response = im_request.request_send(black_list_add_url, url_params, BlackListAddParams)

    """删除黑名单"""
    black_list_delete_url = "https://console.tim.qq.com/v4/sns/black_list_delete"
    BlackListDeleteParams = dict()
    BlackListDeleteParams["From_Account"] = "hxtest-q110"
    BlackListDeleteParams["To_Account"] = ["hxtest-q110"]
    # get_no_speaking_response = im_request.request_send(black_list_delete_url, url_params, BlackListDeleteParams)

    """拉取黑名单"""
    black_list_get_url = "https://console.tim.qq.com/v4/sns/black_list_get"
    BlackListGetParams = dict()
    BlackListGetParams["From_Account"] = "zw861367"
    BlackListGetParams["StartIndex"] = 0
    BlackListGetParams["MaxLimited"] = 1000
    BlackListGetParams["LastSequence"] = 0
    # black_list_get_response = im_request.request_send(black_list_get_url, url_params, BlackListGetParams)

    """校验黑名单"""
    black_list_check_url = "https://console.tim.qq.com/v4/sns/black_list_check"
    BlackListCheckParams = dict()
    BlackListCheckParams["From_Account"] = "hxtest-q110"
    BlackListCheckParams["To_Account"] = ["hxtest-q110"]
    BlackListCheckParams["CheckType"] = "BlackCheckResult_Type_Both"  # BlackCheckResult_Type_Both Singal
    # black_list_check_response = im_request.request_send(black_list_check_url, url_params, BlackListCheckParams)

    """单个账号导入"""
    account_import_url = "https://console.tim.qq.com/v4/im_open_login_svc/account_import"
    AccountImportParams = dict()
    AccountImportParams["Identifier"] = "dzhtest1_02"
    AccountImportParams["Nick"] = "dzhtest1_02"
    AccountImportParams["FaceUrl"] = ""
    AccountImportParams["Type"] = 0
    # account_import_response = im_request.request_send(account_import_url, url_params, AccountImportParams)

    # 批量跑
    # accounts = open(r"C:\Users\Administrator\Desktop\大智慧板块.txt", "r", encoding="utf8").readlines()
    # for _account in accounts:
    #     # print(_account)
    #     account, accid, nick = _account.split(",")
    #     # print(account, accid, nick)
    #     AccountImportParams["Identifier"] = accid
    #     AccountImportParams["Nick"] = nick.strip("\n")
    #     account_import_response = im_request.request_send(account_import_url, url_params, AccountImportParams)

    """批量账号导入"""
    # multiaccount_import_url = "https://console.tim.qq.com/v4/im_open_login_svc/multiaccount_import"
    # multiAccountImportParams = dict()
    # multiAccountImportParams["Accounts"] = []
    # multiaccount_import_response = im_request.request_send(multiaccount_import_url, url_params, multiAccountImportParams)

    """帐号删除接口"""
    # account_delete_url = "https://console.tim.qq.com/v4/im_open_login_svc/account_delete"
    # AccountDeleteParams = dict()
    # AccountDeleteParams["DeleteItem"] = [{"UserID": "4b9d67d894d7dce47607b503ae430871"}]
    # account_delete__response = im_request.request_send(account_delete_url, url_params, AccountDeleteParams)

    """设置资料"""
    portrait_set_url = "https://console.tim.qq.com/v4/profile/portrait_set"
    PortraitSetParams = dict()
    PortraitSetParams["From_Account"] = "98601947"
    ProfileItemList = list()
    ProfileItem = dict()
    ProfileItem["Tag"] = "Tag_Profile_IM_AdminForbidType"
    ProfileItem["Value"] = "AdminForbid_Type_None"
    # AdminForbid_Type_None 允许加好友  AdminForbid_Type_SendOut  禁止该用户发起加好友请求
    # https://cloud.tencent.com/document/product/269/1500#.E6.A0.87.E9.85.8D.E8.B5.84.E6.96.99.E5.AD.97.E6.AE.B5
    ProfileItemList.append(ProfileItem)
    # 自定义认证信息
    # ProfileItem["Tag"] = "Tag_Profile_Custom_UserCert"
    # cert = {"medal":{"edu_stat":1,"detail":[0,1,2,3],"m_list":{"L1":[1,2],"L2":[2,3]}}}
    # ProfileItem["Value"] = json.dumps(cert, ensure_ascii=False)
    # # ProfileItem["Value"] = ""
    # ProfileItemList.append(ProfileItem)
    PortraitSetParams["ProfileItem"] = ProfileItemList
    # portrait_set_response = im_request.request_send(portrait_set_url, url_params, PortraitSetParams)

