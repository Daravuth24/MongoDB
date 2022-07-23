import pymongo

myclient = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

mydb = myclient["KIT1"]

mycol = mydb["dse10"]

# myquery = {"name": "Panha"}

myquery = {"address": {"$regex": "^B"}}

# x = mycol.delete_one(myquery)

x = mycol.delete_many(myquery)

print(x.deleted_count, "documents deleted.")