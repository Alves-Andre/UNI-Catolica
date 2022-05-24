nome = input("Digite seu nome: ")                                       #Peço para o usuario digitar seu nome e atribui o valor que ele digitou na variavel "nome"
print("Seja bem vindo ", nome)                                          #Imprimo uma mensagem de boas vindas a ele com base no nome que ele digitou
data = input("Digite a data quem você entrou na empresa (mm/aaaa): ")   #peço para o usuario digitar a data que ele entrou, apenas  mes e o ano no formato mm/aaaa, e atribuo o valor a variavel "data"
mes = int(data[0:2])                                                    #atribuo o numero referente ao mes que ele entrou na empresa (pegando os 2 primeiros caracteres que ele digitou) a variavel "mes" convertendo esse numero para inteiro
ano = int(data[3:7])                                                    #atribuo o numero referente ao ano (pegando os ultimos 4 caracteres que ele digitou) que ele entrou na vaiavel ano convertendo para inteiro
while True:                                                             #inicio uma repeticao infinita (só sair se achar um break em algum lugar)
    salario = float(input("Digite seu salário (Apenas numeros): "))                      #Peço para o usuario digitar seu salário e atribuo o valor a variavel "salario" já convertido para float
    if salario<=0:                                                      #verifico se o salario é menor ou igual a zero
        print("Salário inválido")                                       #imprimo a mensagem de erro se o salario for menor ou igual a zero, e vai voltar ao inicio da repeticao para que o usuario digite o salario novamente
    else:                                                               #se o salario for maior que zero, o python entra no else
        break                                                           #e como o salario é maior que zero, o python lê o break sai do while
if (mes>2 and ano==2022):                                               #verifico se o mes que ele entrou na empresa é maior que 2 e o ano é igual a 2022, ou seja verifico se ele entrou depois de fevereiro de 2022
    print("Você não está elegível a receber aumento no ano que vem!")   #caso seja, imprimo a mensagem que ele nao está elegivel para receber o aumento
elif (mes<=2 and ano==2022) or ano<2022:                                #verifico se o mes que ele entroou na empresa é menor que 2 quando o ano for de 2022 ou se ele entrou em qualquer mes que o ano seja anterior a 2022, ou seja, verifico se ele entrou até o ultimo dia de fevereiro de 2022
    print("Você está elegível a receber aumento no ano que vem!!")      #caso seja, imprimo a mensagem que ele está elegível a receber aumento no ano que vem
    if salario<=7999:                                                   #verifico se o salario dele é de até R$7999
        aumento=salario*0.06                                            #caso seja verdade calculo o aumento de 6% com base no salário dele e atribuo esse valor a variavel "aumento"
        salario_2023=salario+aumento                                    #atribuo o salario que ele recebera em 2023 (salário atual mais o aumento) na variavel "salario_2023"
        print(f"Seu salário atual é de R${salario} \n Em 2023 você receberá um aumento de R${aumento} \n E seu salário passará a ser de {salario_2023}") #E imprimo o salario atual, o valor do aumento que ele receberá em 2023 e o salário que ele receberá em 2023 (salario atual mais o aumento)
    elif salario>7999:                                                  #verifico se o salario dele é maior que 7999
        aumento=359                                                     #caso seja, o valor do aumento é um valor fixo de R$359 que eu atribuo na variavel aumento
        salario_2023=salario+aumento                                    #atribuo o salario que ele recebera em 2023 (salário atual mais o aumento) na variavel "salario_2023"
        print(f"Seu salário atual é de R${salario} \n Em 2023 você receberá um aumento de R${aumento} \n E seu salário passará a ser de {salario_2023}") #E imprimo o salario atual, o valor do aumento que ele receberá em 2023 e o salário que ele receberá em 2023 (salario atual mais o aumento)