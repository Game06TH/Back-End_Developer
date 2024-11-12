def ef(a,b):
    result = []
    for i in range(a, b + 1):
        if i % 3 != 0:
            result.append(i)
    return result
            
    
def er(a,b,c):
    while True:
        if(a > 0) :
            b +=a
        elif(a<0):
            c+=a
        elif(a==0):
            break
        return (b,c)
        

        

