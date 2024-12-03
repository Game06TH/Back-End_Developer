import database as db
mycursor = db.mydb.cursor()
mycursor.execute("SELECT * FROM student")
myresulf =mycursor.fetchall()
for i in myresulf:
    print(i)