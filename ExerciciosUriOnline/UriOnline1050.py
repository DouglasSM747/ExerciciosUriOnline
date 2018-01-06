#UriOnline1050 (DDD)
#Emulando um Case
destinado = ""
def destino(DDD):
    return {
    61:lambda:"Brasilia",
    71:lambda: "Salvador",
    11:lambda:"Sao Paulo",
    21:lambda:"Rio de Janeiro",
    32:lambda:"Juiz de Fora",
    19:lambda:"Campinas",
    27:lambda:"Vitoria",
    31:lambda:"Belo Horizonte",
    }.get(DDD,lambda:"DDD nao cadastrado")()
DDD = int(input())
print(destino(DDD))
