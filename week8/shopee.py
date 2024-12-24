import database as db
mycursor = db.mydb.cursor()



def show_table_all():
    mycursor.execute("SHOW TABLES")
    table = mycursor.fetchall()  
    print('หัวข้อทั้งหมด')  
    for i in table:
        print(i)

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

def select_all():
    show_table_all()
    print("ไม่พิมอะไรถือว่าหยุด")
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
            break

select_all()
