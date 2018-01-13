#UriOnline1118 (Varias notas com validação)
valid = "1"
while valid=="1":
    cont,media,x= 0,0,0
    while cont < 2:
        nota = float(input())
        if 0<=nota<=10:
            media+= nota
            cont+=1
        else:
            print("nota invalida")
    media = media/2
    print("media = {:.2f}".format(media))
    while (x!=1 and  x!=2):
        x = float(input("novo calculo (1-sim 2-nao)\n"))
        if (x==1):
            valid = "1"
        elif (x==2):
            valid = "2"           

            
