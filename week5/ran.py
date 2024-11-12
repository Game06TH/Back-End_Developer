import t1
while True:
    q=int(input("เลือกโปรแกรม 1 หรือ 2 :"))
    if q==1:
        print("โปรแกรมเรียงเลข")
        a=int(input('จาก :'))
        b=int(input('ถึง :'))
        print (t1.ef(a,b))
    elif q ==2 :
        c=0
        d=0
        while True :
            y = int(input("เลือก 1=ทำงาน 2=หยุด :"))
            if y ==1 :
                e =int(input("ใส่ตัวเลข :"))
                print (t1.er(e,c,d))
            elif y ==2 :
                break