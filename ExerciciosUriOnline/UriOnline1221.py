#Uri1221 (Primos Rapidos)
import math
casos_test = int(input())
cont = 1
aux,x = 0,0
while (cont <= casos_test):
    num = int(input())
    if (num==0 or num==1):
        x = 0
    else:
        x = 1
    aux= math.sqrt(num)
    i = 2
    while (i<=aux):
        if num%i==0:
            x = 0
            break
        i+=1
    print ("Prime" if x == 1 else "Not Prime")
    cont +=1
    
