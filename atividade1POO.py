class Ball:
    def __init__(self, cor):
        self.cor = cor

    def mudaCor(self, nova_cor):
        self.cor = nova_cor
    
    def mostraCor(self):
        return f'A cor da bola é {self.cor}'


ball1 = Ball('Vermelha')
print(ball1.mostraCor())
