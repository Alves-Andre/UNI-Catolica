print('Como percorrer os itens de uma tuplas? como adicionar itens numa tuplas? como remover tuplas?')

print('\nA tupla é diferente da lista pois seus valores são imutáveis, ou seja, não tem como adicionar ou remover elementos de uma tupla')

print('\nEntretanto, ainda assim é possível percorrer entre os elementos de uma tupla')
print('Você pode percorer os itens de uma tupla usando o laço de repetição "for" ')
print('Sua sintaxe é assim:')
print('for x in tupla:')
print('Onde x é uma variável que o seu valor vai ser atribuído a cada item da tupla')
print('Na primeira vez o "x" vai receber o valor do elemento que está no índice 0 da tupla "tupla" e assim sucessivamente')
print('\nVocê também pode buscar o elemento pelo seu índice, exemplo:')
print('print(tupla[0])')
print('será imprimido na tela o elemento que está no indice 0 da tupla')
print('Exemplo na prática: (olhar código)')

tupla = (1,2,3,4)
for x in tupla:
    print(x)
print("")
print(3)

print("\nUm exemplo da utilização de tuplas é guardar o dias da semana, pois nenhum dia da semana pode ser alterado, adicionado ou removido da tupla")
semana = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
print(semana)
#--------------------EXPLICAÇÃO COMENTADA--------------------

#como percorrer os itens de uma tuplas? como adicionar itens numa tuplas? como remover tuplas?
#A tupla é diferente da lista pois seus valores são imutáveis, ou seja, não tem como adicionar ou remover elementos de uma tupla
#Entretanto, ainda assim é possível percorrer entre os elementos de uma tupla
#Você pode percorer os itens de uma tupla usando o laço de repetição "for"
#Sua sintaxe é assim:
#for x in tupla:
#Onde x é uma variável que o seu valor vai ser atribuído a cada item da tupla
#Na primeira vez o "x" vai receber o valor do elemento que está no índice 0 da tupla "tupla" e assim sucessivamente
#Você também pode buscar o elemento pelo seu índice, exemplo:
#print(tupla[0])
#será imprimido na tela o elemento que está no indice 0 da tupla