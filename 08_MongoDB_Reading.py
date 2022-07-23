import pymongo

myclient = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

mydb = myclient["KIT1"]

mycol = mydb["dse10"]

# myquery = {"name": "Thearin"}

# y = mycol.find(myquery)

x = mycol.find()

for data in x:
    print(data)

