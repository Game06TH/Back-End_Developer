import database as db
mycursor = db.mydb.cursor()
import datetime

def delete(table,id,id_name) :
    sql = f"DELETE FROM {table} WHERE {id_name} = %s"
    val =(id,)
    mycursor.execute(sql,val)
    db.mydb.commit()
    if mycursor.rowcount <= 0 :
        return False
    else :
        return True
    
def editdb (table,call,id,vall) :
    sql =f"UPDATE {table} SET {call} = %s  WHERE product_id = %s  "
    val = (vall,id)
    mycursor.execute(sql,val)
    db.mydb.commit()
    if mycursor.rowcount <= 0 :
        return False
    else :
        return True
    

def insert_users(d,b,a,e):
    sql = "INSERT INTO users VALUES (%s,%s,%s,%s,%s) "
    val = (None,d,b,a,e)
    mycursor.execute(sql,val)
    if mycursor.rowcount <= 0 :
        return False
    else :
        return True
 

def insert_products(d,b,a,e,g):
    sql = "INSERT INTO products VALUES (%s,%s,%s,%s,%s,%s) "
    val = (None,d,b,a,e,g)
    mycursor.execute(sql,val)
    if mycursor.rowcount <= 0 :
        return False
    else :
        return True

def insert_categories(d):
    sql = "INSERT INTO categories VALUES (%s,%s) "
    val = (None,d)
    mycursor.execute(sql,val)
    if mycursor.rowcount <= 0 :
        return False
    else :
        return True
    
def insert_orders(d,e,a,g):
    b = datetime.datetime.today()
    sql = "INSERT INTO orders VALUES (%s,%s,%s,%s,%s,%s) "
    val = (None,d,b,e,a,g)
    mycursor.execute(sql,val)
    if mycursor.rowcount <= 0 :
        return False
    else :
        return True
    
def select(table) :
    mycursor.execute(f"SELECT * FROM {table}")
    show = mycursor.fetchall()
    if len (show)<=0:
        return False,None
    else :
        return True,show



d = input ("ใส่ประเภทของสินค้า :") 
print (insert_categories(d))
    