class Televisor():

    def __init__(self):
        self.canal = 1
        self.volume = 40
    
    def mudarCanal(self, novo_canal=0):
        self.canal = novo_canal
        return f' O canal foi alterado para o canal: {self.canal}'
    
    def aumentaVolume(self, volume=0):
        if self.volume + volume > 100:
            self.volume = 100
            print(f'O volume foi alterado para o máximo: {self.volume}')
        else:
            self.volume += volume
            print(f"O volume foi alterado para {self.volume}")

    def diminuiVolume(self, volume=0):
        if self.volume - volume < 0:
            self.volume = 0
            print(f'O volume foi alterado para o mínimo: {self.volume}')
        else:
            self.volume -= volume
            print(f'O volume foi alterado para {self.volume}')

tv = Televisor()
print(tv.mudarCanal(6)) 
tv.aumentaVolume(1)
tv.aumentaVolume(1)
tv.diminuiVolume(2)