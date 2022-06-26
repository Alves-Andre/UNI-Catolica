import random

def verificar(dado):
    while True:
        nome = input(f"Digite seu {dado} ")
        if nome =="":
            print("Nome invalido")
        else: return nome

nome = verificar("nome")
cpf = verificar("cpf")

conta = random.randint(10000000,99999999)
agencia = random.randint(100,999)

print(conta, agencia)