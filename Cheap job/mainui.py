import tkinter 
import database as db
mycursor = db.mydb.cursor()
import datetime

def show_COLUMNS(table) :
    mycursor.execute(f"SHOW COLUMNS FROM {table}")
    show = mycursor.fetchall()  
    if len (show)<=0:
        return False,None
    else :
        return True,show

def show_table():
    mycursor.execute("SHOW TABLES")
    show = mycursor.fetchall()  
    if len (show)<=0:
        return False,None
    else :
        return True,show
    
def show_tables_and_columns():
    mycursor.execute("SHOW TABLES")
    tables = mycursor.fetchall()
    result = ""
    for table in tables:
        table_name = table[0]
        result += f"Table: {table_name}\n"
        mycursor.execute(f"SHOW COLUMNS FROM {table_name}")
        columns = mycursor.fetchall()
        for column in columns:
            column_name = column[0]
            result += f"  - {column_name}\n"
        result += "\n"
    # แสดงผลใน Text Widget
    result_text.delete(1.0, tkinter.END)  # ล้างข้อความเดิม
    result_text.insert(tkinter.END, result)

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
program.minsize(width=800,height=800)

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

table_label = tkinter.Label(master=program, text="รายการตาราง")
table_label.pack()

show_button = tkinter.Button(program, text="แสดงตารางและคอลัมน์", command=show_tables_and_columns)
show_button.pack(pady=10)

result_frame = tkinter.Frame(program)
result_frame.pack(fill=tkinter.BOTH, expand=True, padx=10, pady=10)

result_text = tkinter.Text(result_frame, wrap=tkinter.NONE, font=("Courier", 10))
result_text.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)

scrollbar = tkinter.Scrollbar(result_frame, orient=tkinter.VERTICAL, command=result_text.yview)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
result_text.configure(yscrollcommand=scrollbar.set)

program.mainloop()