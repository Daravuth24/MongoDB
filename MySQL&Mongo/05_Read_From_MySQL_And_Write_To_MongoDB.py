import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="012961117",
  database="mydatabase"
)

mycursor = mydb.cursor(dictionary=True)

mycursor.execute("SELECT * FROM students")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

import pymongo

myclient = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

mydb = myclient["KIT1"]

mycol = mydb["dse10"]

if len(myresult) > 0:
    x = mycol.insert_many(myresult)  # myresult comes from mysql cursor

    print(len(x.inserted_ids))