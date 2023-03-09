class Square:
    def __init__(self, lado):
        self.lado = lado
    
    def mudarValor(self, novo_lado):
        self.lado = novo_lado
    
    def retornaValor(self):
        return f'{self.lado}'

    def somaArea(self):
        return f'O valor da área é {2* self.lado ** 2}'

square = Square(10)
print(square.retornaValor())
print(square.somaArea())

