cont=0
lista=[]
while 1:
    letra = input("Digite letras ou -1 para parar: ")
    if letra=='-1': break
    else: lista.append(letra)

for x in lista:
    if x=='a': cont+=1
print(lista)
print("A lista tem ",cont," letras 'a'.")