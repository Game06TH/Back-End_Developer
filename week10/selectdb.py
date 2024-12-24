import database1
mycursor = database1.mydb.cursor()#เก็บการทำงานของmysql
mycursor.execute("SHOW TABLES")
table = mycursor.fetchall()
print(table)

