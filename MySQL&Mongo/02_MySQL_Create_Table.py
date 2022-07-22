import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="012961117",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE students (name VARCHAR(255), department VARCHAR(255))")

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)