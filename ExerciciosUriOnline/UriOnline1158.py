#UriOnline1158 (Soma de Ímpares Consecutivos III)
casos = int(input())
for i in range(casos):
    x,y = input().split()
    x,y = int(x),int(y)
    cont = 0
    soma = 0
    while(cont<y):
        if (x%2!=0):
            soma+= x
            cont+=1
        x+=1
    print(soma)
