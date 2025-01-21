import database as db
mycursor = db.mydb.cursor()
import datetime

def show_COLUMNS() :
    mycursor.execute("SHOW COLUMNS FROM table_name")
    show = mycursor.fetchall()  
    if len (show)<=0:
        return False,None
    else :
        return True,show

def show_table_all():
    mycursor.execute("SHOW TABLES")
    show = mycursor.fetchall()  
    if len (show)<=0:
        return False,None
    else :
        return True,show

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

    