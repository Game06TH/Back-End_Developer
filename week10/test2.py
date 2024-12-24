import database1
mycursor = database1.mydb.cursor()#เก็บการทำงานของmysql


def SHOW_TABLES() :
    mycursor.execute("SHOW TABLES")
    table = mycursor.fetchall()
    for i in table:
        print (i)

def select_table(table):
    mycursor.execute(f"SELECT * FROM {table}")
    myresulf = mycursor.fetchall()
    for i in myresulf:
        print (i)

def choice():
    print(SHOW_TABLES())
    table = input("เลือกตาราง : ")
    if table== "student" :
        print (select_table(table))
        return student_()
    elif table== "subject" :
        print (select_table(table))
        return subject_()
        


def student_() :
    table = "student"
    c = int(input("ใส่ id : "))
    d = input("ใส่ name : ")
    b = float(input("ใส่ grade : "))
    sql = "INSERT INTO student VALUES (%s,%s,%s) "
    val = (f'{c}',f'{d}',f'{b}')
    mycursor.execute(sql,val)
    database1.mydb.commit()
    print (select_table(table))
    return choice()

def subject_() :
    table =  "subject"  
    c =int(input("ใส่ id_subject : "))
    d =input("ใส่ name : ")
    sql = "INSERT INTO subject VALUES (%s,%s) "
    val = (f'{c}',f'{d}')
    mycursor.execute(sql,val)
    print (select_table(table))
    database1.mydb.commit()
    print (select_table(table))
    return choice()

print(choice())