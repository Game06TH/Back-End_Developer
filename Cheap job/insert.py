import database as db
mycursor = db.mydb.cursor()
import datetime



def insert_users(c,d,b,a,e):
    sql = "INSERT INTO users VALUES (%s,%s,%s,%s,%s) "
    val = (f'{c}',f'{d}',f'{b}',f'{a}',f'{e}')
    mycursor.execute(sql,val)
    if mycursor.rowcount <= 0 :
        return False
    else :
        return True
 

def insert_products(c,d,b,a,e,g):
    sql = "INSERT INTO products VALUES (%s,%s,%s,%s,%s,%s) "
    val = (f'{c}',f'{d}',f'{b}',f'{a}',f'{e}',f'{g}')
    mycursor.execute(sql,val)
    if mycursor.rowcount <= 0 :
        return False
    else :
        return True

def insert_categories(c,d):
    sql = "INSERT INTO categories VALUES (%s,%s) "
    val = (f'{c}',f'{d}')
    mycursor.execute(sql,val)
    if mycursor.rowcount <= 0 :
        return False
    else :
        return True
    
def insert_orders(c,d,b,e,a,g):
    b = datetime.datetime.today()
    sql = "INSERT INTO orders VALUES (%s,%s,%s,%s,%s,%s) "
    val = (f'{c}',f'{d}',f'{b}',f'{e}',f'{a}',f'{g}')
    mycursor.execute(sql,val)
    if mycursor.rowcount <= 0 :
        return False
    else :
        return True

    