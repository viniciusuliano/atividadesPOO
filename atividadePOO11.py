class contaInvestimento:

    def __init__(self, capitalInicial, taxa):
        self.capital = capitalInicial
        self.juros = taxa
    
    def taxaJuros(self):
        juros = self.capital * self.juros   
        self.capital += juros
        return f'TAXA DE JUROS: {self.juros}'
    

    def saldo(self):
        return self.capital 
    
minha_conta = contaInvestimento(1000, 0.1)
print(minha_conta.taxaJuros())
minha_conta.taxaJuros()
minha_conta.taxaJuros()
minha_conta.taxaJuros()
minha_conta.taxaJuros()


print(minha_conta.saldo())