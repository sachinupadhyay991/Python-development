import pyodbc
# For connection
cur=pyodbc.connect('DRIVER=Devart ODBC Driver for MySQL;User ID=root;\
                      Password=sachin@123;Data Source=localhost;Database=mydatabase')

# Creating cursor
a=cur.cursor()

# INSERT
a.execute("insert into staff(name, number) values ('new name', '85234785325')")

# DELETE
a.execute("delete from staff where name = ?", 'new name')

# UPDATE
a.execute("UPDATE staff SET number = '123456789' WHERE name = 'sachin'")


# Displaying data
for i in a.execute("select * from staff").fetchall():
    print(i)


# Closing connection and cursor
a.close()
cur.close()


# Attempt to use a closed cursor 
a.execute("UPDATE staff SET number = '123456789' WHERE name = 'sandy'")

