#UriOnline1178 (Preenchimento de Vetor III)
lista = []
valor = 0
for i in range(100):
    if i==0:
        num = float(input())
        lista.append(num)
        valor = num
    else:
        valor/=2
        lista.append(valor)
for i in range(100):
    print("N[{}] = {:.4f}".format(i,lista[i]))
    
