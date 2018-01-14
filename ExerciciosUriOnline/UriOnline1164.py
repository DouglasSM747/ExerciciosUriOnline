#UriOnline1164(Número Perfeito)
casos = int(input())
for i in range(casos):
        num = int(input())
        cont = 1
        soma = 0
        while cont<num:
            if num%cont==0:
                soma+=cont
            cont+=1
        if soma==num:
            print(num,"eh perfeito")
        else:
            print(num,"nao eh perfeito")        
