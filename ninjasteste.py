from random import shuffle, choice
file = open("listaninjas.txt", "r")
ninjas = [e for e in file.readlines()]
file.close()
voce = ["a"]
def criaOuEscolhe_personagem(op):
    personagem = None
    #op = int(input())
    if op == 1:
        sub = choice(ninjas)
        personagem = sub.replace(sub,input("nome do personagem: "))
        voce[0].replace(voce[0],personagem)
        print(f"vc é {personagem}!")
        salvar()
    elif op == 2:
        for posicao, ninja in enumerate(ninjas):
            print(f"{posicao} - {ninja}\n")
        print("Escolha seu personagem:")
        personagem = ninjas[int(input())]
        print(f"vc é {personagem}!")
        voce[0].replace(voce[0],personagem)
        salvar()
    elif op == 3:
        personagem = choice(ninjas)
        voce[0].replace(voce[0],personagem)
        print(f"vc é {personagem}!")
        salvar()
print("deseja criar, escolher ou\nreceber um personagem aleatorio?")
def salvar():
    personagem = voce[0]
    with open(input("nome_save: ") + ".txt","w+") as file:
        file.write(personagem)
    print("está salvo")
me = criaOuEscolhe_personagem(int(input(": ")))       
    
    