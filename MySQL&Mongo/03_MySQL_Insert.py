import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="012961117",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO students (name, department) VALUES (%s, %s)"
val = [
  ('Daravuth', 'Software Engineer'),
  ('Sen', 'Software Engineer'),
  ('Panha', 'Software Engineer'),
  ('Heng', 'Architecture'),
  ('Somnang', 'Tourism Management')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")