n1 = int(input("Digite o primeiro número: "))   #peço ao usuário digitar um numero e atribuo o numero digitado a variavel "n1"
n2 = int(input("Digite o segundo número: "))    #peço ao usuário digitar um numero e atribuo o numero digitado a variavel "n2"
if n1%2==0:                                     #verifico se o primeiro numero que o usuario digitou é par (se o resto da divisao desse numero por 2 for 0)
    print("O primeiro número (",n1,") é par")   #caso seja, imprimo a mensagem que esse numero é par
else:                                           #caso NAO seja (o resto da divisao desse numero por 2 for diferente de 0)
    print("O primeiro número (",n1,") é ímpar") #Imprimo a mensagem que esse numero é impar
if n2%2==0:                                     #faço o mesmo processo com o segundo número digitado, verifico se o segundo numero que o usuario digitou é par (se o resto da divisao desse numero por 2 for 0)
    print("O segundo número (",n2,") é par")    #caso seja, imprimo a mensagem que esse numero é par
else:                                           #caso NAO seja (o resto da divisao desse numero por 2 for diferente de 0)
    print("O segundo número (",n2,") é ímpar")  #Imprimo a mensagem que esse numero é impar