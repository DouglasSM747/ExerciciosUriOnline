#Uri1150 (Ultrapassando Z)
x = int(input())
z = 0
soma = x
aux = 1
while True:
        z = int(input())
        if(z>x):
            break
while(soma < z):
        soma += x + aux
        aux+=1
print(aux)
