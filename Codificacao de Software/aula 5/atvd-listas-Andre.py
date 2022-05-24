import random
print("Como percorrer os itens de uma lista? como adicionar itens numa lista? como remover itens? ")
print('\nVocê pode percorer os itens de uma lista usando o laço de repetição "for" ')
print("Sua sintaxe é assim:")
print("for x in lista:")
print("Onde x é uma variável que o seu valor vai ser atribuído a cada item da lista")
print('Na primeira vez o "x" vai receber o valor do elemento que está no índice 0 da lista "lista" e assim sucessivamente')
print('Você também pode buscar o elemento pelo seu índice, exemplo:')
print('print(lista[0])')
print('será imprimido na tela o elemento que está no indice 0 da lista')

print('Exemplo na prática: (olhar código)')

lista=[0,1,2,3,4]
for x in lista:
    print(x)
print(lista[2])

print('\nVocê pode adicionar itens em uma lista com o método ".append()"')
print("Sua sintaxe é assim:")
print("lista.append(valor)")
print('Onde "lista" é a lista, "append()" é o método e "valor" é o elemento a ser adicionado na lista.')
print("Com o append o elemento é adicionado no fim da lista")
print('Exemplo na prática: (olhar código)')
print(lista)
lista.append(5)
print(lista)

print('\nVocê também pode adicionar em uma lista o método ".insert()"')
print("Sua sintaxe é assim:")
print("lista.insert(0,valor)")
print('Onde "lista" é a lista, "insert" é o método, "0" é o indice em que o elemento vai ser adicionado e "valor" é o elementoo a ser adicionado na lista.')
print('Exemplo na prática: (olhar código)')
print(lista)
lista.insert(0,-1)
print(lista)

print('\nPara remover podemos usar o método ".pop()"')
print("Sua sintaxe é assim:")
print("lista.pop(indice)")
print('Onde "lista" é a lista, "pop()" é o método e "indice" é o indice do elemento a ser removido na lista, se não for especificado é removido o último elemento')
print('Exemplo na prática: (olhar código)')
print(lista)
lista.pop(0)
print(lista)


print('\nTambém temos o método "remove()" para remover')
print("Sua sintaxe é assim:")
print("lista.remove(valor)")
print('Onde "lista" é a lista, "remove()" é o método e "valor" é o elemento a ser removido na lista.')
print('Exemplo na prática: (olhar código)')
print(lista)
lista.remove(5)
print(lista)

print("\nUm exemplo da utilização de listas é guardar os nomes ou algum outro dado dos vencedores de um determinado sorteio ou promoção")
participantes = ['Andre Alves','Afonso Dglan','João Vitor','Maria Clara','Pedro Henrique']
sorteados = []
numero1 = random.randint(0,4)
numero2 = random.randint(0,4)
sorteados.append(participantes[numero1])
sorteados.append(participantes[numero2])
print("Os vencedores do sorteio são:",sorteados)


#--------------------EXPLICAÇÃO COMENTADA--------------------

#Como percorrer os itens de uma lista? como adicionar itens numa lista? como remover itens?
#Você pode percorer os itens de uma lista usando o laço de repetição "for" 
#Sua sintaxe é assim:
#for x in lista:
#Onde x é uma variável que o seu valor vai ser atribuído a cada item da lista
#Na primeira vez o "x" vai receber o valor do elemento que está no índice 0 da lista "lista" e assim sucessivamente
#Você também pode buscar o elemento pelo seu índice, exemplo:
#print(lista[0])
#será imprimido na tela o elemento que está no indice 0 da lista


#Você pode adicionar itens em uma lista com o método ".append()"
#Sua sintaxe é assim:
#lista.append(valor)
#Onde "lista" é a lista, "append()" é o método e "valor" é o elemento a ser adicionado na lista.
#Com o append o elemento é adicionado no fim da lista

#Você também pode adicionar em uma lista o método ".insert()"
#Sua sintaxe é assim:
#lista.insert(0,valor)
#Onde "lista" é a lista, "insert" é o método, "0" é o indice em que o elemento vai ser adicionado e "valor" é o elementoo a ser adicionado na lista.

#Para remover podemos usar o método ".pop()"
#Sua sintaxe é assim:
#lista.pop(indice)
#Onde "lista" é a lista, "pop()" é o método e "indice" é o indice do elemento a ser removido na lista, se não for especificado é removido o último elemento

#Também temos o método "remove()" para remover
#Sua sintaxe é assim:
#lista.remove(valor)
#Onde "lista" é a lista, "remove()" é o método e "valor" é o elemento a ser removido na lista.