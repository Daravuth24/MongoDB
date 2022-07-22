import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="012961117"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
print("Database created successfully")

