class Funcionario():
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

class Porteiro(Funcionario):
    def __init__(self, nome, cpf, salario, codigo_porteiro):
        super().__init__(nome, cpf, salario)
        self.codigo_porteiro = codigo_porteiro

    def abrir_porta(self):
        print(f"A porta foi aberta pelo porteiro {self.nome}")

    def fechar_porta(self):
        print(f"A porta foi fechada pelo porteiro {self.nome}")

class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, codigo_gerente):
        super().__init__(nome,cpf,salario)
        self.codigo_gerente = codigo_gerente

    def gerenciar(self):
        print(f"O gerente {self.nome} está gerenciando.")

    def desgerenciar(self):
        print(f"O gerente {self.nome} não está mais gerenciando.")

porteiro1 = Porteiro("Andre", "123.456.789-10", 2000, "123")
porteiro1.abrir_porta()
porteiro1.fechar_porta()

gerente1 = Gerente("Joao", "987.654.321-10", 4500, "456")
gerente1.gerenciar()
gerente1.desgerenciar()
