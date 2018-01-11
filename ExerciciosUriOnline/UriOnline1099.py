#UriOnline1099 (Soma de Ímpares Consecutivos II)
quant_casos = int(input())
for i in range(quant_casos):
    n1,n2= input().split()
    n1 = int(n1)
    n2 = int(n2)
    cont_i = 0
    if (n1>n2):
            aux = n1
            n1 = n2
            n2 = aux
    for i in range(n1+1,n2):
        if (i%2!=0):
            cont_i+=i
    print(cont_i)
        
