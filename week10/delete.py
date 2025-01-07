import database1
import selectdb
mycursor = database1.mydb.cursor()
#show = select_student() SHOW_TABLES() select_table(table):

show = selectdb.select_all() 
a = int(input("DELETE id :"))
sql = "DELETE FROM student WHERE id = %s"
val = (a,)
mycursor.execute(sql,val)
database1.mydb.commit()
show = selectdb.select_student()