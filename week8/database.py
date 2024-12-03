import mysql.connector as mysqlcon
mydb = mysqlcon.connect(
    host="localhost",
    user="root",
    password="1234",
    database="online store"
)
print (mydb)
