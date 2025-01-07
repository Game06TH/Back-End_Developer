import database as db
mycursor = db.mydb.cursor()
import datetime

def choice():
    print("ใส่ select = ดูข้อมูล , insert = เพิ่มข้อมูล , delete = ลบข้อมูล")
    tabie = input("เลือกรูปแบบ : ")
    if tabie == "select" :
        return select_all()
    elif tabie == "insert" :
        return choice_insert()
    elif tabie == "delete" :
        return choice_delete()
    
def select_from_all(tabie) :
    mycursor.execute(f"SELECT * FROM {tabie}")
    myresulf = mycursor.fetchall()
    for i in myresulf:
        print (i)
        return tabie

def show_table_all():
    mycursor.execute("SHOW TABLES")
    table = mycursor.fetchall()  
    print('หัวข้อทั้งหมด')  
    for i in table:
        print(i)

#-----------------------------------------------------------------------

def select_all():
    show_table_all()
    print ("ไม่ใส่อะไรจะกลับไปตัวเลือกรูปแบบ")
    tabie = input("ใส่หัวข้อที่ต้องการค้นหา :")
    while True:
        if tabie == 'users' :
            return select_users()
        elif tabie == 'products' :
            return select_products()
        elif tabie == 'categories' :
            return select_categories()
        elif tabie == 'orders' :
            return select_orders()
        else :
            return choice()


def select_users():
    name = input('ป้อนชื่อที่ต้องการค้นหา :')
    mycursor.execute(f"SELECT * FROM users where username like '%{name}%'")
    myresulf =mycursor.fetchall()
    i = myresulf
    while True:
        print(i)
        return select_all()

def select_products():
    name = input('ป้อนสินค้าที่ต้องการค้นหา :')
    mycursor.execute(f"SELECT * FROM products where product_name like '%{name}%'")
    myresulf =mycursor.fetchall()
    i = myresulf
    while True:
        print(i)
        return select_all()

def select_categories():
    name = input('ป้อนหมวดหมู่ที่ต้องการค้นหา :')
    mycursor.execute(f"SELECT * FROM categories where category_iname like '%{name}%'")
    myresulf =mycursor.fetchall()
    i = myresulf
    while True:
        print(i)
        return select_all()

def select_orders():
    name = int(input('ป้อนรหัสของผู้ซื้อที่ต้องการค้นหา :'))
    mycursor.execute(f"SELECT * FROM orders where user_id like '%{name}%'")
    myresulf =mycursor.fetchall()
    i = myresulf
    while True:
        print(i)
        return select_all()
    
#----------------------------------------------------------------------------
    
def choice_insert() :
    show_table_all()
    print ("ไม่ใส่อะไรจะกลับไปตัวเลือกรูปแบบ")
    tabie =input("ใส่หัวข้อที่ต้องการเพิ่มข้อมูล :")
    while True :
        if tabie == 'users' :
            select_from_all(tabie)
            return insert_users()
        elif tabie == 'products' :
            select_from_all(tabie)
            return insert_products()
        elif tabie == 'categories' :
            select_from_all(tabie)
            return insert_categories()
        elif tabie == 'orders' :
            select_from_all(tabie)
            return insert_orders()
        else :
            return choice()
    
def insert_users():
    tabie = 'users'
    c = int(input("ใส่ user_id : "))
    d =input("ใส่ username : ")
    b =input("ใส่ password : ")
    a =input("ใส่ email : ")
    e =input("ใส่ userscol (customer,admin) : ")
    sql = "INSERT INTO users VALUES (%s,%s,%s,%s,%s) "
    val = (f'{c}',f'{d}',f'{b}',f'{a}',f'{e}')
    mycursor.execute(sql,val)
    while True:
        i = db.mydb.commit()
        print (select_from_all(tabie))
        return choice_insert()

def insert_products():
    tabie ='products'
    c = int(input("ใส่ product_id : "))
    d =input("ใส่ product_name : ")
    b =input("ใส่ description : ")
    a =float(input("ใส่ price : "))
    e =int(input("ใส่ stock : "))
    g =int(input("ใส่ category_id :"))
    sql = "INSERT INTO products VALUES (%s,%s,%s,%s,%s,%s) "
    val = (f'{c}',f'{d}',f'{b}',f'{a}',f'{e}',f'{g}')
    mycursor.execute(sql,val)

    while True:
        i = db.mydb.commit()
        print (select_from_all(tabie))
        return choice_insert()

def insert_categories():
    tabie ='categories'
    c = int(input("ใส่ category_id : "))
    d =input("ใส่ category_iname : ")
    sql = "INSERT INTO categories VALUES (%s,%s) "
    val = (f'{c}',f'{d}')
    mycursor.execute(sql,val)
    while True:
        i = db.mydb.commit()
        print (select_from_all(tabie))
        return choice_insert()
    
#-------------------------------------------------------------------------------------

def insert_orders():
    tabie = 'orders'
    c = int(input("ใส่ order_id : "))
    d =int(input("ใส่ user_id : "))
    b = datetime.datetime.today()
    print(b.strftime("%d/%m/%Y %H:%M:%S"))
    e =float(input("ใส่ total_amount : "))
    a =input("ใส่ status (รอดำเนินการ, กำลังจัดส่ง, จัดส่งสำเร็จ, ยกเลิกรายการ) : ")
    g =int(input("ใส่ product_id : "))
    sql = "INSERT INTO orders VALUES (%s,%s,%s,%s,%s,%s) "
    val = (f'{c}',f'{d}',f'{b}',f'{e}',f'{a}',f'{g}')
    mycursor.execute(sql,val)
    while True:
        i = db.mydb.commit()
        print (select_from_all(tabie))
        return choice_insert()
    
def choice_delete() : 
    show_table_all()
    print ("ไม่ใส่อะไรจะกลับไปตัวเลือกรูปแบบ")
    tabie = input("ใส่หัวข้อที่ต้องการลบ :")
    while True:
        if tabie == 'users' :
            select_from_all(tabie)
            return delete_users()
        elif tabie == 'products' :
            select_from_all(tabie)
            return delete_products()
        elif tabie == 'categories' :
            select_from_all(tabie)
            return delete_categories()
        elif tabie == 'orders' :
            select_from_all(tabie)
            return delete_orders()
        else :
            return choice()
        

def delete_users() :
    tabie = "users"
    a = int(input("DELETE user_id :"))
    sql = "DELETE FROM users WHERE user_id = %s"
    val = (a,)
    mycursor.execute(sql,val)
    while True:
        i = db.mydb.commit()
        print (select_from_all(tabie))
        return choice_delete()

def delete_products() :
    tabie ='products'
    a = int(input("DELETE product_id :"))
    sql = "DELETE FROM products WHERE product_id = %s"
    val = (a,)
    mycursor.execute(sql,val)
    while True:
        i = db.mydb.commit()
        print (select_from_all(tabie))
        return choice_delete()

def delete_categories() :
    tabie ='categories'
    a = int(input("DELETE category_id :"))
    sql = "DELETE FROM categories WHERE category_id = %s"
    val = (a,)
    mycursor.execute(sql,val)
    while True:
        i = db.mydb.commit()
        print (select_from_all(tabie))
        return choice_delete()

def delete_orders() :
    tabie = 'orders'
    a = int(input("DELETE order_id :"))
    sql = "DELETE FROM orders WHERE order_id = %s"
    val = (a,)
    mycursor.execute(sql,val)
    while True:
        i = db.mydb.commit()
        print (select_from_all(tabie))
        return choice_delete()
    


    