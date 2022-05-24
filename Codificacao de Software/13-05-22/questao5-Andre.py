class ContaBancaria():
    def __init__(self, numero, titular, saldo, tipo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.tipo = tipo
    
conta_corrente = ContaBancaria(777, "Andre", 1000, "Corrente")
conta_poupanca = ContaBancaria(635, "Joao", 850, "Poupança")
