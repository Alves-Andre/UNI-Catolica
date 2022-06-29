import os
def imprimir(inicial,contador,impri=0):
    matriz_exemplo = []
    for x in range(3):
        matriz_exemplo.append([])
        for y in range(3):
            matriz_exemplo[x].append(inicial)
            inicial+=contador
    if impri==1:
        for x in matriz_exemplo:
            print(x[0],"|",x[1],"|",x[2])
    else:
        return matriz_exemplo

def imprimir_jogo(matriz):
    matriz = matriz[::-1]
    for x in matriz:
            print(x[0],"|",x[1],"|",x[2])

def jogo_atual(j=0):
    if j!=0: jogo = j
    else: return jogo

def jogar(p,player,posicoes):
    livres = []
    for x in posicoes:
        for y in x:
            if str(y) in '123456789':
                livres.append(y)
    if p not in livres:
        print("Posição inválida!")
        return 0
    n_matriz=[]
    for x in posicoes:
        n_linha=[]
        for y in x:
            if y==p:
                if player==1:
                    n_linha.append("X")
                else: n_linha.append("O")
            else: n_linha.append(y)
        n_matriz.append(n_linha)
    return n_matriz

def verificar_ganhador(jogo):
    for x in jogo:
        if x[0]==x[1] and x[1]==x[2]:
            if x[0]=='X':
                return 1
            else: return 2
    for x in range(3):
        if jogo[0][x]==jogo[1][x] and jogo[1][x]==jogo[2][x]:
            if jogo[0][x]=='X':
                return 1
            else: return 2
    if jogo[0][0]==jogo[1][1] and jogo[1][1]==jogo[2][2]:
        if jogo[0][0]=='X':
            return 1
        else: return 2
    if jogo[0][2]==jogo[1][1] and jogo[1][1]==jogo[2][0]:
        if jogo[0][2]=='X':
            return 1
        else: return 2
    return 0

def verificar_velha(posi):
    cont=0
    for x in posi:
        for y in x:
            if str(y) in '123456789':
                cont=1
                break
        if cont==1:
            break
    if cont==1: return 1
    else: return 0


posicoes = imprimir(1,1)
player=1
jogada=1
while True:
    print("\n" * os.get_terminal_size().lines)
    

    print('-'*20,"JOGO DA VELHA",'-'*20)
    print("\nVamos lá, os espaços que estão marcados com os números de 1 a 9 estão vazios e os que estão marcados com 'X' são preenchidos pelo jogador 1, e marcados com 'O' são preenchidos pelo jogador 2.")

    if jogada ==0: 
        print("\nPosição inválida!\n")

    imprimir_jogo(posicoes)
    print(f"Jogador numero {player} sua vez de jogar, escolha uma posição da matriz: ")
    p = int(input("Digite a posicao: "))
    jogada = jogar(p,player, posicoes)
    if jogada ==0: 
        continue
    posicoes = jogada
    resultado = verificar_ganhador(posicoes)
    if resultado!=0:
        if resultado==1:
            print("\nJogador 1 ganhou!")
            imprimir_jogo(posicoes)
        else: 
            print("\nJogador 2 ganhou!")
            imprimir_jogo(posicoes)
        break
    res = verificar_velha(posicoes)
    if res==0:
        print("\nDeu velha!")
        break
    if player == 1: player = 2
    else: player = 1
