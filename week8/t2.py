import database as db
mycursor = db.mydb.cursor()
def show_table():
    mycursor.execute("SHOW TABLES")
    table = mycursor.fetchall()  
    print('หัวข้อทั้งหมด')  
    for i in table:
        print(i)
def select_all():
    show_table()
    tabie = input("ใส่หัวข้อที่ต้องการค้นหา :")
    mycursor.execute(f"SELECT * FROM {tabie}")
    myresulf =mycursor.fetchall()
    for i in myresulf:
        print(i)
def select_student():
    show_table()
    tabie = input("ใส่หัวข้อที่ต้องการค้นหา :")
    name = input('ป้อนชื่อที่ต้องการค้นหา :')
    mycursor.execute(f"SELECT * FROM {tabie} where name like '%{name}%'")
    myresulf =mycursor.fetchall()
    for i in myresulf:
        print(i)

select_student()
