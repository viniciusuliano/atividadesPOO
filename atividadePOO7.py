class Tamagushi:
  def __init__(self, nome, fome, saude, idade):
    self.nome = nome
    self.fome = fome
    self.saude = saude
    self.idade = idade
    
  
  def alteraNome(self, novo_nome):
    self.nome = novo_nome
    return(f'O tamagushi se chama {self.nome}')
  
  def indicadorFome(self, fome=0):
    self.fome += fome
    if self.fome > 70:
      return('O tamagushi está com fome :(') 
    else:
      return('O tamagushi não está com fome')   
  
  def indicadorSaude(self, saude=0):
    self.saude += saude
    if self.saude < 50:
      return('A saude do tamagushi está baixa')
    else:
      return('A saude do tamagushi está boa')
    
  def indicadorIdade(self, idade):
    self.idade = idade
    return(f'A idade do tamagushi é {self.idade} anos')
  
  def indicadorHumor(self):
    if self.fome > 70 and self.saude < 50:
      return "O tamagushi está com fome e doente! Ele está triste e mal-humorado!"
    elif self.fome > 70:
      return "O tamagushi está com fome! Ele está irritado e impaciente!"
    elif self.saude < 50:
      return "O tamagushi está doente! Ele está triste e cansado!"
    else:
      return "O tamagushi está feliz e contente!"
    
tamagushi = Tamagushi('', 0, 0, 0)
print(tamagushi.alteraNome('Vinicius'))
print(tamagushi.indicadorFome(80))
print(tamagushi.indicadorSaude(40))
print(tamagushi.indicadorIdade(10))
print(tamagushi.indicadorHumor())

tamagushi2 = Tamagushi('', 0, 0, 0)
print(tamagushi2.alteraNome('Matheus'))
print(tamagushi2.indicadorFome(50))
print(tamagushi2.indicadorSaude(80))
print(tamagushi2.indicadorIdade(5))
print(tamagushi2.indicadorHumor())