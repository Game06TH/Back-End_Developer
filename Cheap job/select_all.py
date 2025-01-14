import database as db
mycursor = db.mydb.cursor()

def select_from_all(table) :
    mycursor.execute(f"SELECT * FROM {table}")
    show = mycursor.fetchall()
    if len (show)<=0:
        return False,None
    else :
        return True,show