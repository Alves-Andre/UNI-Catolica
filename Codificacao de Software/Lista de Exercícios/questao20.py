num1 = int(input("Digite um número: "))
num = num1-1
primo=True
while True:
    if num==1:
        break
    elif num1%num==0:
        primo=False
        break
    else:
        num-=1
print(primo)