class cliente:
    def __init__(self, nome, idade, saldo):
        self.nome = nome
        self.idade = idade
        self.saldo = saldo
    #sacar dinheiro do saldo
    def sacar(self):
        saque = float(input("Quanto você quer sacar? "))
        if self.saldo > 0 and saque <= self.saldo:
            self.saldo -= saque
            print(f"Você sacou R${saque:.2f}\n Seu saldo atual é de R${self.saldo}")
        else:
            print("Saldo insuficiente para realização do saque")

    def depositar(self):
        deposito = float(input("Quanto você deseja depositar?"))
        self.saldo += deposito
        print(f'Seu saldo atual é de R${self.saldo:.2f}')

cliente1 = cliente("jao", 30, 2000)
cliente1.sacar()
cliente1.depositar()