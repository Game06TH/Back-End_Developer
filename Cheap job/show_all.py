import database as db
mycursor = db.mydb.cursor()

def show_table_all():
    mycursor.execute("SHOW TABLES")
    show = mycursor.fetchall()  
    if len (show)<=0:
        return False,None
    else :
        return True,show
