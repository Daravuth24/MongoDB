import pymongo
from pprint import pprint

myclient = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

mydb = myclient.admin

serverStatusResult = mydb.command("serverStatus")
pprint(serverStatusResult)