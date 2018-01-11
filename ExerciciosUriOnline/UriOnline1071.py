#Uri1071 (Soma de Impares Consecutivos I)		
soma_impar = 0		
aux = 0		
num1 = int(input(""))		
num2 = int(input(""))				
if (num2 < num1):		
        aux = num1		
        num1 = num2		
        num2 = aux		
for i in range(num1+1,num2):		
    if (i%2!=0):		
        soma_impar += i		
        		
print (soma_impar)
