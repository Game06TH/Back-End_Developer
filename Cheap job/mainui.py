import tkinter 
import database as db
mycursor = db.mydb.cursor()
import datetime

def selectdb() :
    table = table_input.get()
    mycursor.execute(f"SELECT * FROM {table}")
    show = mycursor.fetchall()
    if len (show)<=0:
        return False,None
    else :
        return True,output_label.configure(text=show)
    
def delete() :
    table = table_input.get()
    id = del_input.get()
    id_name = del2_input.get()
    sql = f"DELETE FROM {table} WHERE {id_name} = %s"
    val =(id,)
    mycursor.execute(sql,val)
    db.mydb.commit()
    if mycursor.rowcount <= 0 :
        return False
    else :
        return True
    
#--------------------------------------------------
program = tkinter.Tk()
program.title('โปรแกรมจัดการข้อมูล')
program.minsize(width=400,height=400)

program_lable = tkinter.Label(master = program , text= "แสดงผล")
program_lable.pack()

program1_lable = tkinter.Label(master = program , text= "ชื่อตาราง")
program1_lable.pack()

table_input = tkinter.Entry(master=program )
table_input.pack()

program2_lable = tkinter.Label(master = program , text= "ชื่อคอลัม")
program2_lable.pack()

del2_input = tkinter.Entry(master=program)
del2_input.pack()

program3_lable = tkinter.Label(master = program , text= "ข้อมูลที่ต้องการลบ")
program3_lable.pack()

del_input = tkinter.Entry(master=program)
del_input.pack()

search_button = tkinter.Button(master=program ,text="ค้นหาตาราง ",command=selectdb)
search_button.pack()

delete_button = tkinter.Button(master=program ,text="ลบข้อมูล ",command=delete)
delete_button.pack()

output_label =tkinter.Label(master=program , text="ผลการค้นหา" )
output_label.pack()


program.mainloop()