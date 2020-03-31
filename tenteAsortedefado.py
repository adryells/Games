import random as r
print(" neste jogo voce tem 5 opcoes e voce joga ate zerar a pontuacao,\nvoce comeca com 10 pontos, se pontuat abaixo ou = a 0 voce perde! \n\nmensagem batata: voce so erra\nmensagem azar: perde 5 pontos\nmensagel sorte: Recebe 5 pontos\n\n")

pontuacao = 5
tentativas = 0
c = 0
while tentativas < 10:
    Sorte = r.randint(0,100)
    Azar = r.randint(0,100)
    Azar1 = r.randint(0,100)
    erro = r.randint(0,100)
    erro1 = r.randint(0,100)
    opcoes = [Sorte,Azar,Azar1,erro,erro1]
    c+=1
    tentativas+=1
    r.shuffle(opcoes)
    print(opcoes)
    print(f"{c}° tentativa")
    tentativa = int(input("tente:"))
    for e in opcoes:
        if tentativa == e:
            if e == Sorte:
                pontuacao+=5
            elif e == Azar:
                pontuacao-=5
            elif e == Azar1:
                pontuacao-=5
            elif e == erro:
                print("batata")
            elif e == erro1:
                print("batata")
        else:
            pass
print(f"voce terminou com {pontuacao}")
            
           