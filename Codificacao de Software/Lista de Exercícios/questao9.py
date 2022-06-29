while True:
    username = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    if senha!=username: break
    else: 
        print("A senha precisa ser diferente do numero de usuario")
        continue
print("sucesso")