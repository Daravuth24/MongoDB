import pymongo

myclient = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

mydb = myclient["KIT1"]

mycol = mydb["dse10"]

myquery = { "name": "Sen"}
newvalue = { "$set": { "name": "Hanritheasen"}}

mycol.update_one(myquery, newvalue)

for x in mycol.find():
    print(x)
