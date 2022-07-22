import pymongo

myclient = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

mydb = myclient["KIT1"]

mycol = mydb["dse10"]

mylist = {"_id": 1, "name": "Daravuth", "address": "Phnom Penh"}

x = mycol.insert_one(mylist)

print(x.inserted_id)