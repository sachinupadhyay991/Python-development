import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="sachin@123",
  database="mydatabase"
)

mycursor = mydb.cursor()

#Creating database 
#mycursor.execute("CREATE DATABASE mydatabase")

#Create table
#mycursor.execute("CREATE TABLE employee (name VARCHAR(255), number VARCHAR(255))")

#Alter table
#mycursor.execute("AlTER TABLE employee ADD COLUMN(id INTEGER)")

#Insert
'''
sql = "INSERT INTO employee (id, name, number) VALUES (%s, %s, %s)"
val = ("1","sachin","9413775527")
mycursor.execute(sql, val)

sql = "INSERT INTO employee (id, name, number) VALUES (%s, %s, %s)"
val = ("2","Raj","9413775528")
mycursor.execute(sql, val)

'''

#New table
#mycursor.execute("CREATE TABLE staff (name VARCHAR(255), number VARCHAR(255))")

#Multiple Insert
'''
sql = "INSERT INTO staff (name, number) VALUES (%s, %s)"
val = [
  ('Sachin', '9413775517'),
  ('Saksham', '9413775528'),
  ('yash', '9413775529'),
  ('Michael Jackson', '9413775530'),
  ('Sandy', '9413775531'),
  ('priyanka', '9413775532'),
  ('Rich', '9413775533'),
  ('Susan', '9413775534'),
  ('Vishal', '9413775535'),
  ('Ben 10', '9413775536'),
  ('William ', '9413775537')
]

mycursor.executemany(sql, val)

mydb.commit()
'''

#Select statement to fetch all rows
'''
mycursor.execute("SELECT * FROM staff")

for x in mycursor.fetchall():
  print(x)
'''

#Select statement to fetch one rows
'''
mycursor.execute("SELECT * FROM staff")
print(mycursor.fetchone())
'''

#Where condition
'''
sql = "SELECT * FROM staff WHERE number ='9413775528'"
mycursor.execute(sql)

for x in mycursor.fetchall():
  print(x)
'''

#Using wildcraft character
'''
sql = "SELECT * FROM staff WHERE name LIKE '%sa%'"
mycursor.execute(sql)

for x in mycursor.fetchall():
  print(x)
'''

#Ascending order
'''
sql = "SELECT * FROM staff ORDER BY name"
mycursor.execute(sql)

for x in mycursor.fetchall():
  print(x)
'''

#Descending order
'''
sql = "select * from staff order by name desc"
mycursor.execute(sql)

for x in mycursor.fetchall():
  print(x)
'''

#Deleting a paricular row
'''
sql = "DELETE FROM staff WHERE name = 'Sandy'"
mycursor.execute(sql)

sql = "select * from staff order by name desc"
mycursor.execute(sql)
for x in mycursor.fetchall():
  print(x)
'''

#Drop table employee
'''
sql = "DROP TABLE employee"
mycursor.execute(sql)
'''

#Update column
'''
sql = "UPDATE staff SET number = '7412558896' WHERE name = 'sachin'"
mycursor.execute(sql)

sql = "select * from staff order by name desc"
mycursor.execute(sql)
for x in mycursor.fetchall():
  print(x)
'''

#Limit keyword
'''
mycursor.execute("SELECT * FROM staff LIMIT 5")

for x in mycursor.fetchall():
  print(x)
'''

#Use of offset
'''
mycursor.execute("SELECT * FROM staff LIMIT 5 OFFSET 3")

for x in mycursor.fetchall():
  print(x)
'''
