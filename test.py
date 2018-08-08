import mysql.connector

print("-----Enter your student details")
a = input("Enter your first name:")
b = input("Enter your last name:")
c = input("Enter your ID number:")
try:
 exampledb = mysql.connector.connect(host="localhost", user="root", password="")
 print("Mysql connection established")
except:
    print("Mysql connection cannot be established")
try:
  dbcursor = exampledb.cursor()
  dbcursor.execute("CREATE DATABASE python")
  print("Database python created")
except:
    print("Database python already exists")
try:
 exampledb = mysql.connector.connect(host="localhost", user="root", password="", database="python")
 dbcursor = exampledb.cursor()
 print("Database connection established")
except:
    print("Database connection cannot be established")
try:
 dbcursor.execute("CREATE TABLE student(ID int NOT NULL AUTO_INCREMENT, fname VARCHAR(255), lname VARCHAR(255), IDnum VARCHAR(255), PRIMARY KEY(ID))")
 print("Table student created")
except:
      print("Table student already exists")
dbcursor = exampledb.cursor()
sql = "INSERT INTO student(fname,lname,IDnum)VALUES(%s,%s,%s)"
val = (a, b, c)
dbcursor.execute(sql, val)
exampledb.commit()

print("-----Students data:")

dbcursor.execute("SELECT * FROM student")
dbresult = dbcursor.fetchall()

for x in dbresult:
    print(x)
print("-----End of mydb")