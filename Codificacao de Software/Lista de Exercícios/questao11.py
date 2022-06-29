while True:
    nome = input("Digite seu nome: ")
    if len(nome)<=3:
        print("o nome precisa ter mais de 3 caracteres!")
        continue

    idade = int(input("Digite sua idade: "))
    if idade<=0 or idade>=150:
        print("A idade precisa estar entre 0 e 150!")
        continue

    salario = float(input("Digite seu salário: "))
    if salario<=0:
        print("O salario precisa ser maior que 0!")
        continue

    sexo = input("Digite seu sexo m/f: ")
    if sexo!='m' and sexo!='f':
        print("O sexo precisa ser 'm' or 'f' ")
        continue
    
    est_civil = input("Digite seu estado civil s/c/d/v: ")
    if est_civil!='s' and est_civil!='c' and est_civil!='d' and est_civil!='v':
        print("O estado civil precisa ser 's' ou 'c' ou 'd' ou 'v'!")
        continue
    break
print("Sucesso!")