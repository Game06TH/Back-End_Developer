import t1
while True:
    q=int(input("เลือกโปรแกรม 1 หรือ 2 :"))
    if q==1:
        while True :
            print("โปรแกรมเรียงเลข")
            print('พิมพ์ 0 เพื่อต้องการออก')
            a=int(input('จาก :'))
            b=int(input('ถึง :'))
            c =(t1.ef(a,b))
            if b==0 :
                break
            print(f'{c}\n')
    elif q ==2 :
        c=0
        d=0
        while True :
            print("โปรแกรมรวมค่า")
            print('พิมพ์ 0 เพื่อต้องการออก')
            y = int(input("ใส่เลข :"))
            if y == 0 :
                print(f"ผลรวมของบวก  = {c}")
                print(f'ผลรวมของบวก  = {d}')
                break
            c, d = t1.er(y, c, d)
            print(c, d)
