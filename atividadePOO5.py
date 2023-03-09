class Conta:
    def __init__(self, n_conta, nome_conta, saldo=0):
        self.n_conta = n_conta
        self.nome = nome_conta
        self.saldo = saldo
    
    def alteraNome(self, novo_nome):
        self.nome = novo_nome
    
    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
       if self.saldo >= valor:
        self.saldo -= valor
       else:
          print('Saldo insuficiente')
    
    def __str__(self):
       return f'Conta Corrente - Numero: {self.n_conta}, Nome: {self.nome}, Saldo: {self.saldo}'

conta = Conta(123456, "Vinicius", 500)
conta.deposito(150)
print(conta)
conta.saque(200)
print(conta)