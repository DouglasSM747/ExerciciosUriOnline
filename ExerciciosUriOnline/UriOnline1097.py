#UriOnline1097 (Sequencia IJ 3)
i = 1
aux = 7
cont_i=0
j = 7
while (i<=10):
    print ("I={} J={}".format(i,j))
    cont_i+=1
    j-=1
    if (cont_i>=3):
        i+=2
        cont_i = 0
        aux = aux + 2
        j = aux

