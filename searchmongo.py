# Requires pymongo 3.6.0+
from pymongo import MongoClient

client = MongoClient("mongodb://root:%21QAZ2wsxok@10.15.108.23:27017/?serverSelectionTimeoutMS=5000&connectTimeoutMS=10000&authSource=admin&authMechanism=SCRAM-SHA-1&3t.uriVersion=3&3t.connection.name=imtest")
database = client["imback"]
collection = database["team_info"]

# Created with Studio 3T, the IDE for MongoDB - https://studio3t.com/

query = {}
query["owner"] = u"20202026"

cursor = collection.find(query)
try:
    for doc in cursor:
        if doc.get("stock") != None:
            print(doc.get("tid"),doc.get("name"),doc.get("stock")[0].get("code"),doc.get("stock")[0].get("name"))
        # print(doc)
finally:
    client.close()
