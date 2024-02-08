# Requires pymongo 3.6.0+
from pymongo import MongoClient
import csv

client = MongoClient("mongodb://root:%21QAZ2wsxok@10.15.108.23:27017/?serverSelectionTimeoutMS=5000&connectTimeoutMS=10000&authSource=admin&authMechanism=SCRAM-SHA-1")

database = client["imback"]
collection = database["user_vip"]
res=[]

# documents = collection.find().limit(100)
# query={"quasiVip":1}
query={"vip":1}
documents = collection.find(query).limit(500)
try:
    with open('20231107.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for account in documents:
            if account.get("account") is not None:
                row = account.get("account")
                writer.writerow([row])
                res.append(row)
        print(res)
        # test = "hxtest-q"
        # for i  in range(6001,8501):
        #     test1 = test + str(i)
        #     res.append(test1)
        # print(res)

finally:
    client.close()