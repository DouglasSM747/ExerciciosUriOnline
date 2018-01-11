#Uri1154 (Idades)
idade = 1
soma_id = 0
cont = 0
while True:
        idade = int(input())
        if (idade>0):
            soma_id += idade
            cont+=1
        else:
            break
media_i = soma_id/cont
print("{:.2f}".format(media_i))
        
        
