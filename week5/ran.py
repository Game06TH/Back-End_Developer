import t1
c=0
d=0
while True:
    q=int(input("เลือกโปรแกรม 1 หรือ 2 :"))
    if q==1:
        print("โปรแกรมเรียงเลข")
        a=int(input('จาก :'))
        b=int(input('ถึง :'))
        print (t1.ef(a,b))
    elif q ==2 :
        y = int(input("ใส่เลข :"))
        c, d = t1.er(y, c, d)
        print((c, d))
