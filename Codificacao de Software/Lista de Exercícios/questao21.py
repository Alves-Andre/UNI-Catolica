from audioop import avg, minmax


lista=[]
while True:
    num = int(input('Vai digitando vários números ou digite "-1" para parar: '))
    if num==-1: break
    else:
        lista.append(num)

soma = sum(lista)
minimo = min(lista)
maximo = max(lista)
media = sum(lista)/len(lista)
print(f"O menor valor é: {minimo}")
print(f"O maior valor é: {maximo}")
print(f"A soma é: {soma}")
print(f"A média é: {media}")
