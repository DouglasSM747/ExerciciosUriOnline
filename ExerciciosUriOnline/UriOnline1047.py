i = 1
J = 7
cont_i=0
while (i<=10):
    cont_i+=1
    print ("I={} J={}".format(i,J))
    J-=1
    if (cont_i>=3):
        i+=2
        cont_i=0
        J=7
    
