#UriOnline1175 (Troca em Vetor I)
lista = []
for i in range(20):
    x = int(input())
    lista.append(x)
aux = 0
j = 1
for i in range(len(lista)):
    aux = lista[i]
    lista[i] = lista[-j]
    lista[-j] = aux
    j+=1
    if i == 9:
        break
for i in range(len(lista)):
    print("N[{}] = {}".format(i,lista[i]))
