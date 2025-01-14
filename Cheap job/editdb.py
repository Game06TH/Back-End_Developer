import database as db
mycursor = db.mydb.cursor()

def editdb_users(call,id,vall) :
    sql =f"UPDATE users SET {call} = %s  WHERE user_id = %s  "
    val = (vall,id)
    mycursor.execute(sql,val)
    db.mydb.commit()

def editdb_products(call,id,vall) :
    sql =f"UPDATE products SET {call} = %s  WHERE product_id = %s  "
    val = (vall,id)
    mycursor.execute(sql,val)
    db.mydb.commit()

def editdb_categories(call,id,vall) :
    sql =f"UPDATE categories SET {call} = %s  WHERE category_id = %s  "
    val = (vall,id)
    mycursor.execute(sql,val)
    db.mydb.commit()

def editdb_orders(call,id,vall) :
    sql =f"UPDATE orders SET {call} = %s  WHERE order_id = %s  "
    val = (vall,id)
    mycursor.execute(sql,val)
    db.mydb.commit()

