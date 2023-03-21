class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.quantidade = 0
    
    def andar(self, distancia):
        consumo_medio = self.consumo / 100
        litros_consumidos = consumo_medio * distancia
        combustivel_restante = self.quantidade - litros_consumidos  
        combustivel_restante = max(0, combustivel_restante)
        return f'O carro andou um total de {distancia} KM e consumiu um total de {litros_consumidos} Litros'
    
    def obterGasolina(self):
        return f'O nivel da gasolina é de {self.consumo}'
    
    def adicionarGasolina(self, litros):
        self.quantidade += litros
        return f'Foram adicionados {litros:.2f} litros'

carro1 = Carro(12)
carro1.quantidade = 50
print(carro1.andar(100))
print(carro1.obterGasolina())
print(carro1.adicionarGasolina(30))