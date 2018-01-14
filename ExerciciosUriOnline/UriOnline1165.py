#UriOnline1165 (Número Primo)
casos = int(input())
for i in range(casos):
    num = int(input())
    cont = 0
    i = 1
    while i<=num:
        if num%i==0:
            cont+=1
        i+=1
    if cont>3:
        print(num,"nao eh primo")
    elif cont==2:
        print(num,"eh primo")
    else:
        print(num,"nao eh primo")
