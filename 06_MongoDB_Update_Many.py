import pymongo

myclient = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

mydb = myclient["KIT1"]

mycol = mydb["dse10"]

myquery = { "address": { "$regex": "^P"}}
newvalue = {"$set": {"address": "Battambang"}}

mycol.update_many(myquery, newvalue)

for x in mycol.find():
    print(x)
