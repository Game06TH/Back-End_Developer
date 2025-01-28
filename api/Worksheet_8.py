import fastapi
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    password = "1234",
    database = 'school'
)

print("Connected to Database:", mydb.is_connected())
mycursor = mydb.cursor()
app = fastapi.FastAPI()

# ------------------------------------------ < > ---------------------------------------- #
@app.get("/")
async def hi():
    return f"wellcome yo myAPI"
#http://127.0.0.1:8000

# ------------------------------------------ < > ---------------------------------------- #
@app.get("/hi/{name}")
async def hi_name(name):
    return f"Hello {name} wellcome to myAPI"
#http://127.0.0.1:8000/hi/Film

# ------------------------------------------ <select/> ---------------------------------------- #
@app.get("/select/{table}")
async def select_table(table):
    sql = (f"SELECT * FROM {table}")
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult
#http://127.0.0.1:8000/select/subject

# ------------------------------------------ <delete/> ---------------------------------------- #
@app.get("/deletedb/{table}/{column}/{id}")
async def deletedb(table,column,id):
    sql = f"DELETE FROM {table} WHERE {column} = %s"
    val = (id,)
    mycursor.execute(sql,val)
    mydb.commit()
    if mycursor.rowcount <= 0:
        return False,None
    else:
        return True,None 
#http://127.0.0.1:8000/deletedb/subject/id_subject/5

# ------------------------------------------ <updete/> ---------------------------------------- #
@app.get("/updetedb/{table}/{column}/{a}/{name}/{b}")
async def updetedb(table,column,a,name,b):
    sql = f"UPDATE {table} SET {column} = %s WHERE {name} = %s"
    val = (a,b)
    mycursor.execute(sql,val)
    mydb.commit()
    if mycursor.rowcount <= 0:
        return False,None
    else:
        return True,None
    
#http://127.0.0.1:8000/updetedb/subject/name_subject/BACKEND/id_subject/6

# ------------------------------------------ <insert/subject> ---------------------------------------- #
@app.get("/insertdb/{table}/{id}/{name}")
async def insertdb(table: str, id: int, name: str):
    sql = f"INSERT INTO {table} (id_subject ,name_subject) VALUES (%s, %s)"
    val = (id,name)
    mycursor.execute(sql,val)
    mydb.commit()
    if mycursor.rowcount <= 0:
        return False,None
    else:
        return True,val
#http://127.0.0.1:8000/insertdb/subject/5/art 

# ------------------------------------------ <insert/student> ---------------------------------------- #
@app.get("/insertdb/{table}/{id}/{name}/{grade}")
async def insertdb(table,id,name,grade):
    sql = f"INSERT INTO {table} (id_student ,name ,grade) VALUES (%s,%s,%s)"
    val = (id,name,grade)
    mycursor.execute(sql,val)
    mydb.commit()
    if mycursor.rowcount <= 0:
        return False,None
    else:
        return True,val
#http://127.0.0.1:8000/insertdb/student/15/art/3.3 


#ทดสอบ API 
#หลังจากรัน FastAPI (uvicorn main:app --reload) ให้ทดสอบ API:
#Swagger UI: http://127.0.0.1:8000/docs
#Redoc: http://127.0.0.1:8000/redoc

