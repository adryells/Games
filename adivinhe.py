#A game for my Sister Gabi
#from random import shuffle
class Jogador:
    def __init__(self,nome):
        self.nome = nome
        self.pontuacoes = []
        self.recorde = max(self.pontuacoes)
    def adivinha(self,opcao):
        pass
class Maquina:
    def __init__(self):
        self.recordes = []
        self.opcoes = ["maçã", "banana", "melão", "melancia", "abacaxi", "cereja"]
        self.tentativas = []
    def Embaralha_opcoes(self):
        shuffle(self.opcoes)
class Jogo:
    def __init__(self,jogador):
        self.jogador = jogador
    def definicao(self):
        if a == procura:
            print("acertou")
            return
        print("errou,tente novamente")
        self.Executa()
    def Executa(self):
        print("{j1.nome} tente adivinhar...")
        procura = m1.opcoes[3]
        print("Em qual opcão está {shuffle(m1.opcoes[3])}?")
        print(range(1,6))
        m1.Embaralha_opcoes()
        a = j1.adivinha(int(input("tente: ")))
        self.definicao()
j1 = Jogador("Adryell")
m1 = Maquina()
partida = Jogo(j1)       