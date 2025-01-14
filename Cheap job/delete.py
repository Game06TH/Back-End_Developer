import database as db
mycursor = db.mydb.cursor()


def delete(table,id,id_name) :
    sql = f"DELETE FROM {table} WHERE {id_name} = %s"
    val =(id,)
    mycursor.execute(sql,val)
    db.mydb.commit()
    if mycursor.rowcount <= 0 :
        return False
    else :
        return True

