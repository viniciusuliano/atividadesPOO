class Tamagushi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def mostraNome(self, novo_nome):
        self.nome = novo_nome
        return f'{self.nome}'
    
    def mostraFome(self):
        if self.fome > 60:
            return f'O Tamagushi está com fome'
        else:
            return f'O Tamagushi está sem fome'

    def mostraSaude(self):
        if self.saude < 60:
            return f"O Tamagushi está sem saúde, precisa de remédios"
        else:
            return f"O tamagushi está com a saúde boa"

    def mostraIdade(self, nova_idade):
        self.idade = nova_idade
        if self.idade > 7:
            return f"A idade dele é {self.idade}, o tamagushi está muito velho"
        else:
            return f"O tamagushi está jovem"
            

tamagushi = Tamagushi('Dom Dom', 50, 70, 5 )
print(tamagushi.mostraNome('Jom Jom'))
print(tamagushi.mostraFome())
print(tamagushi.mostraSaude())
print(tamagushi.mostraIdade(10))
print(tamagushi.mostraHumor())