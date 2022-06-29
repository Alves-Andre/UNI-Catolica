num1 = int(input("Digite o 1° numero: "))
num2 = int(input("Digite o 2° numero: "))
num3 = int(input("Digite o 3° numero: "))
num4 = int(input("Digite o 4° numero: "))
num5 = int(input("Digite o 5° numero: "))
lista=[num1,num2,num3,num4,num5]
valor=0
for x in lista:
    if x>valor:
        valor=x
print(valor)