#UriOnline1173 (Preenchimento de Vetor I)
lista = [0]*10
x = int(input())
for i in range(10):
    lista[i] = x
    x*=2
for i in range(10):
    print("N[{}] = {}".format(i,lista[i]))
