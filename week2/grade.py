score =int(input("ใส้คะแนน  :"))
if  score < 0 or score > 100:
    print ('ใส่เลข 0 - 100')
elif score >= 80:
    print ("เกรด4")
elif score >= 70:
    print ('เกรด3')
elif score >= 60:
    print ('เกรด2')
elif score >= 50:
    print ('เกรด1')
else:
    print ("เกรด0")