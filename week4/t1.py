def choice_area_Rock_Paper_Scissors():
    while True:
        a = int(input("เลือกว่าทำอะไร \n เป่ายิงฉุบ คือ 1\n หาพื้นที่ คือ 2 \n หรือ 0 หยุดการทำงาน \n :"))
        if a == 1 :
            print(Rock_Paper_Scissors())
        elif a == 2:
            print(choice_area())
        else :
            break

def Rock_Paper_Scissors() :
    import random
    print ("ดปรแกรมเป่ายิงฉุบ")
    while True:
        a = random.choice(["ค้อน","กรรไกร","กระดาษ"])
        b=input("เลือก ค้อน กรรไกร กระดาษ:")
        if a == b :
           print ("เสมอ")
        elif (a == "ค้อน" and  b == "กระดาษ") or (a == "กรรไกร" and  b == "ค้อน") or (a == "กระดาษ" and  b == "กรรไกร") :
            print ("ชนะ")
        else :
            print ("แพ้")

def choice_area():
    while True:
        a = int(input("เลือกว่าทำอะไร \n 4เหลี่ยมจัตุรัส คือ 1\n 4เหลี่ยมผืนผ้า คือ 2 \n วงกลม คือ 3 \n 0 ย้อนกลับ \n :"))
        if a == 1 :
            print(area_square())
        elif a == 2:
            print(area_rectanglr())
        elif a == 3:
            print(area_circle())
        else:
            print(choice_area_Rock_Paper_Scissors())

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

print(choice_area_Rock_Paper_Scissors())