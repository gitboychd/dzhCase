import requests
import json

#host = "http://10.15.108.96:10002/im/v2/team/shop/batchSet"
#hosta = "http://10.15.108.95:10003/im/v2/team/shop/batchSet"
# hosta = "http://10.15.108.95:10003/im/v2/team/adverts/bottomSet"
hosta = "http://10.33.3.143:11002/im/v2/team/adverts/bottomSet"





headers = {"content-type":"application/json"}

f = open('prod.txt', encoding='utf-8')

result = list()
for line in f.readlines():  # 逐行读取数据
    res = line.split(',')  # 以逗号切割
    account = res[0]
    teamid = res[1]
    print( account ,teamid )
    params = {"qid": "1609308520937", "account": account, "teamid": teamid, "startTime": 1650591979000,
              "endTime": 1650678379000, "url": "https://newmnews.gw.com.cn/wap/data/im/shop/images/20201229102509.jpg",
              "height": 130}
    data = json.dumps(params)
    r = requests.post( url=hosta , data=data )
    rep = json.loads(r.text)
    print( r.headers)
    print(rep)
#过期时间
#params = {"qid":"1609308520937","account":account,"teamid":teamid,"startTime":1650591979000,"endTime":1650678379000,"url":"https://newmnews.gw.com.cn/wap/data/im/shop/images/20201229102509.jpg","height":130}
#生效时间
# params = {"qid":"1609308520937","account":account,"teamid":teamid,"startTime":1650764779000,"endTime":1650851179000,"url":"https://newmnews.gw.com.cn/wap/data/im/shop/images/20201229102509.jpg","height":130}





# data = json.dumps(params)


#r = requests.post( url=hosta , data=data )

# rep = json.loads(r.text)
#
# print( r.url)
# print( r.status_code)
# print( rep)
# print( r.headers)



