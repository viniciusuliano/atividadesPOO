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
        x = self.ponto + {self.altura} / 2
        y = self.ponto + {self.largura} / 2
        return Ponto(x, y)
    
    


