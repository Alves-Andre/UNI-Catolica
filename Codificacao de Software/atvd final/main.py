# saldo nao começa com os valores da execucao anterior do programa
import random
import sqlite3
from datetime import datetime
from time import process_time_ns
import getpass
from tkinter.font import nametofont

class Conecta():
    def __init__(self, db_name):
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
        except:
            print('Erro ao se conectar com o banco de dados')

    def commit_db(self):
        if self.conn:
            self.conn.commit()

    def close_db(self):
        if self.conn:
            pass
        self.conn.close()

class ContaBancaria():
    def __init__(self, nome, cpf, nacionalidade, cidade, estado, endereco, celular, renda, nome_mae, nome_pai, senha, numero, agencia, saldo = 0, limite =0):
        self.nome = nome
        self.cpf = cpf
        self.nacionalidade = nacionalidade
        self.cidade = cidade
        self.estado = estado
        self.endereco = endereco
        self.celular = celular
        self.renda = renda
        self.nome_mae = nome_mae
        self.nome_pai = nome_pai
        self.__senha = senha
        self.numero = numero
        self.agencia = agencia

        #vaiaveis nao fornecidas
        self.saldo = saldo
        self.limite = limite
        self.useratual = ""
        self.ativadesativa = True

        #Banco de dados
        self.credenciais = Conecta('credenciais.db')
        self.dados = Conecta('dados.db')

        self.credenciais.cursor.execute("""
            CREATE TABLE IF NOT EXISTS logins (
            cpf VARCHAR(11) NOT NULL PRIMARY KEY,
            conta varchar(8) NOT NULL,
            agencia varchar(3) NOT NULL,
            senha VARCHAR(18) NOT NULL
            );
            """)

        self.dados.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf VARCHAR(11) NOT NULL UNIQUE,
            nacionalidade TEXT NOT NULL,
            cidade TEXT NOT NULL,
            estado TEXT NOT NULL,
            endereco TEXT,
            celular TEXT,
            renda_mensal FLOAT,
            nome_mae TEXT NOT NULL,
            nome_pai TEXT,
            saldo FLOAT,
            limite FLOAT
            );
            """)
        
        self.dados.cursor.execute("""
            CREATE TABLE IF NOT EXISTS extrato (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            cpf INT,
            cpf_destino INT,
            tipo TEXT,
            descricao TEXT,
            data TEXT
            );
        """)

        self.credenciais.commit_db()
        self.dados.commit_db()


    def __str__(self):
                return F'Titular: {self.nome} \nCPF: {self.cpf}\nNacionalidade: {self.nacionalidade}\nCidade: {self.cidade}\nEstado: {self.estado} \nEndereço: {self.endereco} \nCelular: {self.celular} \nRenda Mensal: {self.renda} \nNome da mãe: {self.nome_mae} \nNome do pai: {self.nome_pai} \nSaldo: {self.saldo} \nNº da conta: {self.numero} \nNº da agência: {self.agencia}'
    
    def inserirnodb(self):
        self.dados.cursor.execute("""
            INSERT INTO clientes (nome, cpf, nacionalidade, cidade, estado, endereco, celular, renda_mensal, nome_mae, nome_pai, saldo, limite)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?);
            """, (self.nome, self.cpf, self.nacionalidade, self.cidade, self.estado, self.endereco, self.celular, self.renda, self.nome_mae, self.nome_pai, self.saldo, self.limite))
        
        self.credenciais.cursor.execute("""
            INSERT INTO logins (cpf, conta, agencia, senha)
            VALUES (?,?,?,?);
        """, (self.cpf, self.numero, self.agencia, self.__senha))

        #Executando os inserts acima
        self.dados.commit_db()
        self.credenciais.commit_db()

    def status(self):
        if self.ativadesativa==True:
            print("Sua conta está ativa e pronta para realizar operações")

    def acessarConta(self, user):
        self.useratual = user
        print(f"Bem vindo a sua conta {self.useratual.nome}")

    def imprimirExtrato(self):
        dados = Conecta("dados.db")
        dados.cursor.execute("""
            SELECT * FROM extrato WHERE cpf=?
        """, (self.cpf, ))
        extrato = dados.cursor.fetchall()
        print(f"\nTitular: {self.nome} \nNº da conta: {self.numero} \nNº da agência: {self.agencia}\n")
        print(f"Tipo..........................Descrição.............................................................Data.........................")
        for x in extrato:
            calc1 = 30 - len(str(x[3]))
            calc2 = 70 - len(str(x[4]))
            print(str(x[3])+"."*calc1+ str(x[4]) +"."*calc2+ str(x[5]))

    def liberarLimite(self):
        connec = Conecta("dados.db")
        connec.cursor.execute("""
            SELECT COUNT(*) FROM extrato WHERE cpf=?
        """,(self.cpf,))
        qtd = connec.cursor.fetchone()[0]
        if qtd >= 5:
            self.limite = 200
            print(f"Seu limite foi desbloqueado \nSeu limite inicial é de R${self.limite}")

        else:
            print("você precisa ter ao menos 5 movimentações na conta para liberar seu limite")

    def aumentarLimite(self):
        if self.limite==0:
            print("Você não pode pedir aumento pois seu limite está bloqueado")
        else:
            aumento = float(input(f"Seu limtie atual é de {self.limite} \nDigite quantos reia você deseja aumentar: "))
            percento = aumento/self.limite*100
            if percento<30:
                self.limite += aumento
                self.dados.cursor.execute(""" 
                    UPDATE clientes SET limite = ? WHERE cpf = ?;
                    """,(self.limite, self.cpf))
                self.dados.commit_db()
                print(f"Aumento concedido, parabéns seu novo limite é de R${self.limite}")
            elif percento<60:
                sorte = random.randint(1,10)
                if sorte >=5:
                    self.limite += aumento
                    print(f"Aumento concedido, parabéns seu novo limite é de R${self.limite}")
                else:
                    print(f"Aumento rejeitado, seu limite continua em R${self.limite}")
            else:
                sorte = random.randint(1,10)
                if sorte >=8:
                    self.limite += aumento
                    print(f"Aumento concedido, parabéns seu novo limite é de R${self.limite}")
                else:
                    print(f"Aumento rejeitado, seu limite continua em R${self.limite}")
    
    def sacar(self):
        valor = float(input("Digite o valor que você deseja sacar: "))
        if self.saldo>=valor:
            self.saldo -= valor
            print(f"Saque realizado com sucesso! \nSeu saldo atual é de R${self.saldo}")
            self.dados.cursor.execute("""
                INSERT INTO extrato(cpf,cpf_destino,tipo,descricao,data)
                VALUES (?,?,?,?,?);
                """, (self.cpf, self.cpf, "Saque","Saque realizado no valor de R$"+str(valor), datetime.now()))
            self.dados.cursor.execute(""" 
                UPDATE clientes SET saldo = ? WHERE cpf = ?;
                """,(self.saldo, self.cpf))
            self.dados.commit_db()
        else:
            print("Você não tem saldo suficiente para essa transação")
        
    def depositar(self):
        valor = float(input("Digite o valor que você deseja depositar: "))
        self.saldo+=valor
        print(f"Depósito realizado com sucesso! \nSeu saldo atual é de R${self.saldo}")
        self.dados.cursor.execute("""
            INSERT INTO extrato(cpf,cpf_destino,tipo,descricao,data)
            VALUES (?,?,?,?,?);
            """, (self.cpf, self.cpf, "Depósito","Depósito realizado no valor de R$"+str(valor), datetime.now()))
        self.dados.cursor.execute(""" 
            UPDATE clientes SET saldo = ? WHERE cpf = ?;
            """,(self.saldo, str(self.cpf)))

        self.dados.commit_db()
    
    def transferir(self):
        nconta = input("Digite o numero da conta para quem você deseja realizar a transferência: ")
        nagencia = input("Digite o numero da agencia para quem você deseja realizar a transferência: ")
        destinatario = procurarConta(nconta, nagencia)
        if destinatario == False:
            print("Destinatário não encontrado, verifique o numero de conta e agencia e tente novamente")
            return False
        else:
            print("Destinatário localizado!")
            valor = float(input("Digite o valor da transferência: "))
            if self.saldo<valor:
                print("Saldo insuficiente")
                return False
            else:
                self.saldo -= valor
                destinatario.saldo += valor

                dep1 = f"Transferência realizada para o usuário {str(destinatario.nome)} no valor de R$ {str(valor)}"
                dep2 = f"Transferência recebida do usuário {self.nome} no valor de R${str(valor)}"
                self.dados.cursor.execute("""
                    INSERT INTO extrato(cpf,cpf_destino,tipo,descricao,data)
                    VALUES (?,?,?,?,?);
                    """, (self.cpf, destinatario.cpf, "Transferência",dep1, datetime.now()))
                self.dados.cursor.execute("""
                    INSERT INTO extrato(cpf,cpf_destino,tipo,descricao,data)
                    VALUES (?,?,?,?,?);
                    """, (destinatario.cpf, self.cpf, "Transferência", dep2, datetime.now()))
                self.dados.cursor.execute(""" 
                    UPDATE clientes SET saldo = ? WHERE cpf = ?;
                """,(self.saldo, self.cpf))

                self.dados.cursor.execute(""" 
                    UPDATE clientes SET saldo = ? WHERE cpf = ?;
                """,(destinatario.saldo, destinatario.cpf))
                
                self.dados.commit_db()

                print("Transferência realizada com sucesso! ")
                return True

    def interface(self):
        while True:
            print(f"""
            OLá {self.nome} seja bem vindo, escolha sua ação:
            1- Status da Conta
            2- Verificar Saldo
            3- Verificar extrato
            4- Verificar limite
            5- Pedir liberação de limite
            6- Pedir aumento de limite
            7- Sacar
            8- Depositar
            9- Transferir
            10- Sair
            """)
            escolha = int(input("Digite sua escolha: "))
            if escolha==1:
                print(self)
                self.status()
            elif escolha==2:
                print(f"Senhor(a) seu saldo atual é de R${self.saldo}")
            elif escolha==3:
                self.imprimirExtrato()
            elif escolha==4:
                if self.limite == 0:
                    print("Senhor(a) você não tem nenhum limite")
                else:
                    print(f"Senhor(a) seu limite atual é de R${self.limite}")
            elif escolha==5:
                self.liberarLimite()
            elif escolha==6:
                self.aumentarLimite()
            elif escolha==7:
                self.sacar()
            elif escolha==8:
                self.depositar()
            elif escolha==9:
                self.transferir()
            elif escolha==10:
                print("Sessão encerrada.")
                break

def gerarConta():
    numero = random.randint(1,99999999)
    numero = str(numero)
    qtd = len(numero)
    if qtd < 8:
        numero = '0'*(8-qtd) + numero
    return numero

def gerarAgencia():
    numero = random.randint(1,999)
    numero = str(numero)
    qtd = len(numero)
    if qtd < 8:
        numero = '0'*(3-qtd) + numero
    return numero

def verificarSenha(senha):
    especial = 0
    minuscula = 0
    maiuscula = 0
    numero = 0
    for x in senha:
        if x in 'abcdefghijklmnopqrstuvwxyz':
            minuscula+=1
        if x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            maiuscula+=1
        if x in '0123456789':
            numero+=1
        if x in '!@#$%¨&*()_-+=§´`[{]}º^~/?°;:.,><ª\|"':
            especial+=1
        if x in "'":
            especial+=1
    if especial+minuscula+maiuscula+numero<8:
        return "A senha precisa conter pelo menos 8 caracteres"
    elif especial<1:
        return "A senha precisa conter pelo menos 1 caracter especial"
    elif maiuscula<1:
        return "A senha precisa conter pelo menos 1 letra maiuscula"
    elif minuscula<1:
        return "A senha precisa conter pelo menos 1 letra minuscula"
    elif numero<1:
        return "A senha precisa conter pelo menos 1 número"
    else:
        return True
    

def criarSenha():
    while True: 
        pass1 = getpass.getpass(prompt='Digite sua senha: (Para sua segurança nada será exibido no terminal) \n OBS: deve conter letras maiusculas e minúsculas, números e caracteres especiais \n')
        pass2 = getpass.getpass(prompt="Repita sua senha: \n")
        if pass1!=pass2:
            print("As senhas não conferem")
            continue
        resultado = verificarSenha(pass1)
        if resultado==True:
            return pass1
        else:
            print(resultado)
            continue

def listarContas(contas):
    cont=1
    for x in contas:
        print(f" {cont} - {x.nome}")

def procurarConta(nconta,nagencia):
    for x in usuarios:
        if x.numero == nconta and x.agencia == nagencia:
            return x
    return False

def dig_nome(verificacao = ""):
    while True:
        if verificacao =="":
            nome = input(f"Digite seu nome complemento: ")
        else:
            nome = input(f"Digite o nome da sua mãe: ")
        if nome=="":
            print("\nNome inválido, tente novamente\n")
        elif len(nome.split(" ")) <2:
            print("\nDigite o nome e sobrenome por favor\n")
        else: return nome

def dig_cpf():
    while True:
        cpf = input("Digite seu cpf: ")
        try:
            teste = int(cpf)
        except:
            print("\nDigite apenas números\n")
            continue
        if len(cpf) != 11:
            print("\nCPF inválido, tente novamente\n")
            continue
        else:
            return cpf

def dig_string(tipo):
    while True:
        if tipo =="nacionalidade" or tipo=="cidade":
            string = input(f"Digite sua {tipo}: ")
        else:
            string = input(f"Digite seu {tipo}: ")
        if string=="":
            print("\nCampo obrigatório, tente novamente\n")
            continue
        else:
            return string

def dig_renda():
    while True:
        renda = input("Digite sua renda: ")
        try:
            renda = float(renda)
        except:
            print("Digite apenas números. Campo obrigatório.")
        else:
            return renda

def dig_cll():
    while True:
        cll = input("Digite seu numero de telefone celular: ")
        if cll=="": return cll
        try:
            teste = int(cll)
        except:
            print("\nCaso deseje informar seu telefone digite apenas os números\n")
        else:
            return cll

def dig_pai():
    while True:
        nome = input("Digite o nome do seu pai: ")
        if nome=="":
            return nome
        elif len(nome.split(" "))<2:
            print("Caso deseje informa o nome do seu pai digite o nome e sobrenome")
            continue
        else:
            return nome

def criando_conta():
    n_conta = gerarConta()
    n_agencia = gerarAgencia()
    nome = dig_nome()
    cpf = dig_cpf()
    nacionalidade = dig_string("nacionalidade")
    cidade = dig_string("cidade")
    estado = dig_string("estado")
    endereco = dig_string("endereco")
    celular = dig_cll()
    renda = dig_renda()
    nome_mae = dig_nome("mae")
    nome_pai = dig_pai()
    senha = criarSenha()
    user = ContaBancaria(nome, cpf, nacionalidade, cidade, estado, endereco, celular, renda, nome_mae, nome_pai, senha, n_conta, n_agencia)
    #user = ContaBancaria("Andre", "07233781184", "Altamira", "Palmas", "Tocantins", "Rua 6 QI16B LT 17", "981081632", 1050, "Francisca", "José", "Senha123!", "12345678", "123")
    user.inserirnodb()
    usuarios.append(user)
    print("\n\n\n")
    print("Conta criada com sucesso")
    print(user)


def recuperar_usuarios():
    try:
        backup1 = Conecta('credenciais.db')
        backup2 = Conecta('dados.db')
        backup1.cursor.execute("""
            SELECT * FROM logins;
        """)
        backup2.cursor.execute("""
            SELECT * FROM clientes;
        """)

        logins = backup1.cursor.fetchall()
        dados = backup2.cursor.fetchall()

        log = []
        dado = []
        for linhas in logins:
            log.append([linhas[0], linhas[1], linhas[2], linhas[3]])
        
        for linhas in dados:
            dado.append([linhas[1], linhas[2], linhas[3], linhas[4], linhas[5], linhas[6], linhas[7], linhas[8], linhas[9], linhas[10], linhas[11],linhas[12]])

        for x in range (len(dado)):
            user = ContaBancaria(dado[x][0], dado[x][1], dado[x][2], dado[x][3], dado[x][4], dado[x][5], dado[x][6], dado[x][7], dado[x][8], dado[x][9], log[x][3], log[x][1], log[x][2], dado[x][10], dado[x][11])
            usuarios.append(user)
    except:
        pass

def password(nconta,nagencia,usuario):
    senha = getpass.getpass(prompt='Digite sua senha: (Para sua segurança nada será exibido no terminal) \n')
    consulta = Conecta("credenciais.db")
    consulta.cursor.execute("""
        SELECT senha FROM logins WHERE cpf=? and agencia=? and conta=?;
        """, (usuario.cpf, nagencia, nconta))
    senhadb = consulta.cursor.fetchone()[0]
    if senha==senhadb:
        return True
    else:
        print("Senha incorreta")
        return False

#Variáveis
global usuarios
global usuario
usuarios = []
recuperar_usuarios()
#teste = usuarios[0]
#teste.interface()
# interface 

while True:
    print("""
    1. Criar conta bancária
    2. Acessar conta bancária
    3. Sair do programa
    """)
    opcao = int(input("Digite a opção desejada: "))
    if opcao==1:
        criando_conta()

    elif opcao==2:
        nconta = input("Digite o número da sua conta: ")
        nagencia = input("Digite o número da sua agencia: ")
        achou = procurarConta(nconta,nagencia)
        if achou == False:
            print("Conta e/ou agencia não encontrada.")
        else:
            usuario = achou
            verificar_senha = password(nconta,nagencia,usuario)
            if verificar_senha == True:
                usuario.interface()
            else:
                continue
    elif opcao ==3:
        print(f"Até a próxima :)")
        break
    else:
        print("Opção inválida \nTente novamente \n")