import fastapi
import mysql.connector
import datetime
mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    password = "1234",
    database = 'online store'
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

# ------------------------------------------ <insert/users> ---------------------------------------- #
@app.get("/insertdb/{table}/{user_id}/{username}/{password}/{email}/{userscol}")
async def insertdb(table, user_id, username,password,email,userscol):
    sql = f"INSERT INTO {table} VALUES (%s,%s,%s,%s,%s) "
    val = (user_id,username,password,email,userscol)
    mycursor.execute(sql,val)
    if mycursor.rowcount <= 0 :
        return False,None
    else :
        return True,val
#http://127.0.0.1:8000/users///// 

# ------------------------------------------ <insert/products> ---------------------------------------- #
@app.get("/insertdb/{table}/{product_id}/{product_name}/{description}/{price}/{stock}/{category_id}")
async def insertdb(table,product_id,product_name,description,price,stock,category_id):
    sql = f"INSERT INTO {table} VALUES (%s,%s,%s,%s,%s,%s) "
    val = (product_id,product_name,description,price,stock,category_id)
    mycursor.execute(sql,val)
    mydb.commit()
    if mycursor.rowcount <= 0:
        return False,None
    else:
        return True,val
#http://127.0.0.1:8000/insertdb/products//////

# ------------------------------------------ <insert/categories> ---------------------------------------- #
@app.get("/insertdb/{table}/{category_id}/{category_iname}")
async def insertdb(table,category_id,category_iname):
    sql = f"INSERT INTO {table} VALUES (%s,%s)"
    val = (category_id,category_iname)
    mycursor.execute(sql,val)
    mydb.commit()
    if mycursor.rowcount <= 0:
        return False,None
    else:
        return True,val
#http://127.0.0.1:8000/insertdb/categories/// 

# ------------------------------------------ <insert/orders> ---------------------------------------- #
@app.get("/insertdb/{table}/{order_id}/{user_id}/{order_date1}/{total_amount}/{status}/{product_id}")
async def insertdb(table,order_id,user_id,total_amount,status,product_id):
    order_date = datetime.datetime.today()
    sql = f"INSERT INTO {table} VALUES (%s,%s,%s,%s,%s,%s)"
    val = (order_id,user_id,order_date,total_amount,status,product_id)
    mycursor.execute(sql,val)
    mydb.commit()
    if mycursor.rowcount <= 0:
        return False,None
    else:
        return True,val
#http://127.0.0.1:8000/insertdb/orders//////


#ทดสอบ API 
# cd C:\31901-2005\backend_02\api
#หลังจากรัน FastAPI (python -m uvicorn Worksheet_8:app --reload) ให้ทดสอบ API:
#Swagger UI: http://127.0.0.1:8000/docs
#Redoc: http://127.0.0.1:8000/redoc

