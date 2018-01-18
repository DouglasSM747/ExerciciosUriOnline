#Urionline1177 (Preenchimento de Vetor II)
lista = []
num = int(input())
cont = 0
while cont != 1000:
    for i in range(num):
        lista.append(i)
    cont +=1
for i in range(1000):
    print("N[{}] = {}".format(i,lista[i]))
