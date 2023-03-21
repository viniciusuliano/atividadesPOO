class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []    

    def comer(self, alimento):
        self.bucho.append(alimento)
    
    def verBucho(self):
        print(f'O {self.nome} tem no bucho: {self.bucho}')
    
    def digerir(self):
        self.bucho = []
        print(f'O {self.nome} digeriu tudo e ficou com o bucho vazio')
    

macaco1 = Macaco('Donkey Kong')
macaco2 = Macaco('Monga')

alimentos = ["banana", "morango", "laranja"]

for alimento in alimentos:
    macaco1.comer(alimentos)
    macaco2.comer(alimentos)

    macaco1.verBucho()
    macaco2.verBucho()

    macaco1.digerir()
    macaco1.comer(macaco2)