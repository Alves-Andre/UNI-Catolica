from io import open_code


arquivo = open('nomes.txt', 'r', encoding='utf-8')
leitura = arquivo.read()
arquivo.close()
nomes = leitura.split('\n')
arquivo2 = open('nomes iniciados com A.txt', 'w', encoding='utf-8')
for x in nomes:
    if x[0].lower() == 'a':
        arquivo2.write(x+'\n')
arquivo2.close()