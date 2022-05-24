num1 = int(input("Digite o 1° numero: "))
num2 = int(input("Digite o 2° numero: "))
num3 = int(input("Digite o 3° numero: "))
num4 = int(input("Digite o 4° numero: "))
num5 = int(input("Digite o 5° numero: "))
num6 = int(input("Digite o 6° numero: "))
num7 = int(input("Digite o 7° numero: "))
num8 = int(input("Digite o 8° numero: "))
num9 = int(input("Digite o 9° numero: "))
num10 = int(input("Digite o 10° numero: "))
lista=[num1,num2,num3,num4,num5,num6,num7,num8,num9,num10]
pares=[]
impares=[]
for x in lista:
    if x%2==0:
        pares.append(x)
    else:
        impares.append(x)
print("Lista de pares: ",pares)
print("Lista de impares: ",impares)
