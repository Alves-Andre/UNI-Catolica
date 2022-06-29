enesimo = int(input("Digite o enésimo numero da sequencia de Fibonacci: "))
cont=2
lista=[1,1]
if enesimo==1 or enesimo==2:
    print("O resultado é: 1")
while True:
    valor = lista[-1]+lista[-2]
    lista.append(valor)
    cont+=1
    if cont==enesimo: break
print("O resultado é: ",valor)
