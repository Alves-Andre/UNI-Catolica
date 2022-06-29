num = input("Digite um numero: ")
resultado = ""
lista=[]
for x in num:
    lista.append(x)
cont = len(lista)-1
for x in lista:
    resultado = resultado + str(lista[cont])
    cont-=1
print(resultado)