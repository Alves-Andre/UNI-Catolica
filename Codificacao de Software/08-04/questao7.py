while True:
    nota = input("Digite um valor entre 1 e 5: ")
    if nota in "12345":
        nota = int(nota)
        if nota<=5 and nota>=1:
            print("sucesso")
            break
        else:
            print("Numero inválido, tente novamente")
            continue
    else:
        print("Numero inválido, tente novamente")
        continue
        
        