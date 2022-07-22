import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="012961117",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DROP TABLE students"

mycursor.execute(sql)
