class bombaCombustivel:
    def __init__(self, tipo, quantidadeLitros, valorLitro):
        self.tipo = tipo	
        self.quantidadeCombustivel = quantidadeLitros
        self.valorLitro = valorLitro    
    
    def abastecerPorValor(self, valor):
        litros = valor / self.valorLitro
        self.quantidadeCombustivel -= litros
        return f'Quantidade de litros: {litros} '
    
    def abastecerPorLitro(self, quantidade):
        total_valor = quantidade * self.valorLitro
        self.quantidadeCombustivel -= quantidade
        return f'O valor do litro é de {total_valor:.2f}'
        
    def alterarValor(self, novo_valorLitro):
        self.valorLitro = novo_valorLitro
        return f'O valor do litro mudou para: {self.valorLitro}'

    def alterarCombustivel(self, novo_tipo):
        self.tipo = novo_tipo
        return f'O combustivel abastecido foi: {self.tipo} ' 
    
    def alterarQuantidade(self, nova_quantidade):
        self.quantidade = nova_quantidade
        return f'A quantidade de litros restante na bomba é {self.quantidade:.2f}'
    
    def quantidadeAbastecida(self, valor):
        litros = valor / self.valorLitro
        return f'Saiu da bomba {litros:2f} litros de {self.tipo}'
    
bomba1 = bombaCombustivel("Comum", 500, 4)

print(bomba1.abastecerPorValor(80))
print(bomba1.abastecerPorLitro(80))
print(bomba1.alterarValor(4.2))
print(bomba1.alterarCombustivel('Gasolina Aditivada'))
print(bomba1.abastecerPorLitro(15))
print(bomba1.quantidadeAbastecida(15))
print(bomba1.alterarQuantidade(400))