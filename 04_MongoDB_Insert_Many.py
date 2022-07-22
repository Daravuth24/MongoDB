import pymongo

myclient = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

mydb = myclient["KIT1"]

mycol = mydb["dse10"]

mylist = [
    {"_id": 2, "name": "Sen", "address": "Phnom Penh"},
    {"_id": 3, "name": "Panha", "address": "Battambang"},
    {"_id": 4, "name": "Thearin", "address": "Siem Reap"}
]

x = mycol.insert_many(mylist)

print(x.inserted_ids)