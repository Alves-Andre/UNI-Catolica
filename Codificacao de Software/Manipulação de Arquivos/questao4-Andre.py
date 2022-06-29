import random
arquivo = open("arquivo_numeros_aleatorios.txt","w",encoding='UTF-8')
for i in range(0,100):
    numero = random.randint(0, 1000)
    arquivo.write(str(numero)+"\n")	
