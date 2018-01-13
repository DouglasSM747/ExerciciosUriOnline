#UriOnline1116 (Divisão X por Y)
div = 0
casos = int(input())
for i in range(casos):
    x,y = input().split()
    x,y = int(x),int(y)
    if (y!=0):
        div = x/y
        print("%.1f" % div)
    else:
        print("divisao impossivel")
