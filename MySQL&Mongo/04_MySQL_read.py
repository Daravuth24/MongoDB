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
