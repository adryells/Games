from random import randint
#d = 0
save = open("salvar.txt","a")
tentativas = []
c = ''
def main():
    print("acerte o numero!")
    print("palpite:")
    global tentativas
    #tentativas = []
    palpite = escolha()
    pc = numero()
    jogando = True
    while jogando:
        if palpite != pc:
            c = input('deseja continuar?[s/n]').lower()
            if c == 's':
                if palpite < pc:
                    print("é maior")
                    palpite = int(input(':'))
                    tentativas.append(palpite)
                elif palpite > pc:
                    print("é menor")
                    palpite = int(input(":"))
                    tentativas.append(palpite)
            else:
                print("jogo salvo,retorne mais tarde!")
                salvar()
                break
        else:
            print("voce venceu!")
            break
            
def numero():
    #global d
    d = randint(1,10)
    return d
def escolha():
    e = int(input(":"))
    return e
def salvar():
    save.write(str(numero()))
    return save
#criar funcao para carregar jogo dps
main()
