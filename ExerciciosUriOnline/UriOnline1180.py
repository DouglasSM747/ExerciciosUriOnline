#UriOnline1180 (Menor e Posição)
tam = int(input())
lista = []
a = list(map(int,input().split()))
for i in range(tam):
    lista.insert(i,a[i])
print("Menor valor:",min(lista))
for i in range(tam):
    if lista [i] == min(lista):
        pos = i
print("Posicao:",pos)
