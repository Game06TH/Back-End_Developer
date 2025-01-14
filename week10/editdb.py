import database1
mycursor = database1.mydb.cursor()
def editdb(table) :
    if table == "student" :
        call = input('ใส่ชื่อคอลัมที่ต้องการจะเปลี่ยน :')
        id = int(input("ใส่เลขไอดีที่ต้องการเปลี่ยน :"))
        vall = input('ใส่ค่าที่ต้องการจะเปลี่ยน :')
        sql =f"UPDATE student SET {call} = %s  WHERE id = %s  "
        val = (vall,id)
        mycursor.execute(sql,val)
        database1.mydb.commit()

editdb("student")