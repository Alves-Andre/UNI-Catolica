from importlib.metadata import entry_points


num = int(input("Digite um numero: "))
cont=0
total=1
for x in range(num-1):
    total=total*num
    num-=1
print(total)