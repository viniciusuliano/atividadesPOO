class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos=1):
        self.idade += anos
        if self.idade < 21:
            self.crescer(0.5 * anos)

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura

    def __str__(self):
        return f'{self.nome}, {self.idade} anos, {self.peso:.1f} kg, {self.altura:.2f} m'

# pedir informações do usuário
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (m): "))

# criar objeto pessoa
pessoa = Pessoa(nome, idade, peso, altura)

# exemplo de uso
print(pessoa)
pessoa.envelhecer()
print(pessoa)
pessoa.envelhecer(2)
print(pessoa)
pessoa.engordar(5.0)
print(pessoa)
pessoa.emagrecer(3.0)
print(pessoa)
