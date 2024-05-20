class Pessoa():
  def __init__(self, nome, peso, idade):
    self.nome=nome
    self.peso=peso
    self.idade=idade
    self.estado="parado"

  def parar(self):
    if self.estado=="parado":
      print(self.nome,"já está parado")
    else:
      self.estado="parado"
      print(self.nome,"parou")

  def comer(self,comida):
    if self.estado=="parado":
      self.estado="comendo"
      print(f"{self.nome} está comendo {comida}")
    elif self.estado=="comendo":
      print(self.nome,"já está comendo")
    else:
      print(self.nome,"não pode comer agora")

  def andar(self):
    if self.estado=="parado":
      self.estado="andando"
      print(self.nome,"está andando")
    elif self.estado=="andando":
      print(self.nome,"já está andando")
    else:
      print(self.nome,"não pode andar agora")

  def falar(self):
    if self.estado=="parado":
      self.estado="falando"
      print(self.nome,"está falando")
    elif self.estado=="falando":
      print(self.nome,"já está falando")
    else:
      print(self.nome,"não pode falar agora")
