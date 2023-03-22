class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def mostraNome(self, novo_nome):
        self.nome = novo_nome 
        return f"FUNCIONARIO: {self.nome}"

    def mostraSalario(self, salario):
        self.salario = salario
        return f"SALÁRIO: {self.salario}"
    
    def aumentoSalario(self, percentual):
        percentual = percentual / 100.0
        aumento = percentual * self.salario
        self.salario += aumento
        return f'SALÁRIO: {self.salario}'
    
funcionario1 = Funcionario('Vinicius', 1200)
funcionario1.mostraNome('José')
funcionario1.mostraSalario(24000)
funcionario1.aumentoSalario(20)
print(funcionario1.nome)
print(funcionario1.salario)