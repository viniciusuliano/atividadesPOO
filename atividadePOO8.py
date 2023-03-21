class Ponto: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimiValor(self):
        return f'PONTO X: {self.x}  PONTO Y: {self.y}'    

class Retangulo:
    def __init__(self, largura, altura, ponto):
        self.largura = largura
        self.altura = altura
        self.ponto = ponto

    def centro(self):
        x_centro = self.ponto.x + self.altura  / 2
        y_centro = self.ponto.y + self.largura / 2
        return Ponto(x_centro, y_centro)
    
    def imprimir(self):
        return f'LARGURA: {self.largura} ALTURA: {self.altura}'

altura = float(input('1- Defina o valor da Altura:  '))
largura = float(input('2- Defina o valor da Largura: '))

ponto1 = Ponto(10, 20)
retangulo1 = Retangulo(altura, largura, ponto1)

print(ponto1.imprimiValor())
print(retangulo1.imprimir())
print(retangulo1.centro().imprimiValor())
