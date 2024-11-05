def hi():
    print("hello python")

hi()

def AxB(a,b):
    print("ฟังก์ชั้นคูณตัวเลข")
    print(a*b)
    c = a*b
    return c

a = AxB(a=int(input("ใส่ค่า A :")),b=int(input("ใส่ค่า B :")))

def area_rectanglr():
    print ("โปรแกรมคำนวณพื้นที่ 4เหลี่ยมผืนผ้า")
    b1 = int(input("ใส่ความกว้าง : "))
    b2 = int(input("ใส่ความยาว : "))
    b3 =  b1 * b2
    print (f"ค่าของพื้นที่ 4เหลี่ยมผืนผ้า : {b3} ")  

def area_square():
    print ("โปรแกรมคำนวณพื้นที่ 4เหลี่ยมจัตุรัส")
    a1 = int(input("ใส่ด้าน : "))
    a2 =  a1 * a1
    print (f"ค่าของพื้นที่ 4เหลี่ยมจัตุรัส : {a2} ")

def area_circle():
    print ("โปรแกรมคำนวณพื้นที่วงกลม")
    c1 = float(input("ใส่รัสมี : "))
    c2 =  3.14 * (c1**2)
    print (f"ค่าของพื้นที่วงกลม : {c2}") 

print("")

def c():
    b = int(input("ใส่ต้องกรา"))