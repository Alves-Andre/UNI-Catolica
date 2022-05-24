nomes = [] #crio uma lista vazia de nome "nomes"
while True: #inicio um laço de repetição infinito (só sair se achar um break em algum lugar)
    nome = input("Digite o nome de um dos integrantes da família ou digite  'sair' para sair: ") #peço para o usuario digitar o nome de um dos integrantes da família ou digitar 'sair' para sair do laço
    if nome == 'sair': break #caso tenha digitado sair eu saio do laço
    nomes.append(nome) #a cada vez que ele nao digitar sair eu adiciono o que ele digitou na lista "nomes", isso vai se repetir até ele digitar "sair"
print("Sua família é composta por ",len(nomes)," pessoas") #Imprimo a quantidade de integrantes da familia dele com base na quantidade de nomes que ele digitou, contando quantos elementos tem na lista "nomes" com a funcao len()