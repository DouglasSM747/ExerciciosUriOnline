#UriOnline1159 (Soma de Pares Consecutivos)
x = 1 
while x!=0:
    x = int(input())
    cont = 0
    soma = 0
    if (x!=0):
        while cont<=4:
            if x%2==0:
                cont+=1
                soma+=x
            x+=1
        print(soma)
