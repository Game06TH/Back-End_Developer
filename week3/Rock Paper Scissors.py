import random
print ("ดปรแกรมเป่ายิงฉุบ")
while True:
    a= random.choice(["ค้อน","กรรไกร","กระดาษ"])
    b=input("เลือก ค้อน กรรไกร กระดาษ:")
    if a == b :
        print ("เสมอ")
    elif (a == "ค้อน" and  b == "กระดาษ") or (a == "กรรไกร" and  b == "ค้อน") or (a == "กระดาษ" and  b == "กรรไกร") :
        print ("ชนะ")
    else :
        print ("แพ้")