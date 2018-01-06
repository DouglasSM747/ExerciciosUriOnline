#Uri1064 (Positivos e media)
valor_positivo = 0
media_positivo = 0

for i in range(6):
    numero = float(input(""))
    if (numero>=0):
        valor_positivo+=1
        media_positivo+= numero/1
        
        
print (valor_positivo,"valores positivos")
print ("{:.1f}".format(media_positivo/valor_positivo))
