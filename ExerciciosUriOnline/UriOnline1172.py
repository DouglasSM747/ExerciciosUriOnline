#UriOnline1172 (Substituição em Vetor I)
lista = []
for i in range(10):
    x = int(input())
    lista.append(x)
for i in range(10):
    if lista[i]<=0:
        lista[i]=1
    print("X[{}] = {}".format(i,lista[i]))
