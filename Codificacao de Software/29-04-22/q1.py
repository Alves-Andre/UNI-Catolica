matriz = []
cont=1
for i in range(10):
    linha=[]
    for j in range(10):
        linha.append(cont)
        cont+=1
    matriz.append(linha)
for x in matriz:
    print(x)
