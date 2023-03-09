class Rectangle:
    def __init__(self, base, heigth):
        self.base = base
        self.heigth = heigth
    
    def mudaValor(self, new_base, new_heigth):
        self.base = new_base
        self.heigth = new_heigth
    
    def retornaValor(self):
        return f'O valor da base é {self.base} o valor da altura é {self.heigth}'

    def calculaArea(self):
        return self.base * self.heigth
    
    def calculaPerimetro(self):
        return 2*(self.base + self.heigth)

base = float(input("Digite o valor da base do retângulo: "))
heigth = float(input("Digite o valor da altura do retângulo: "))
rectangle = Rectangle(base, heigth)
print(rectangle.retornaValor())
print(rectangle.calculaArea())
print(rectangle.calculaPerimetro())