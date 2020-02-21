from random import shuffle,choice
from time import sleep
acoes = ["soca", "chuta", "cabeceia", "especial", "principal"]
arq = open("ninjas.txt", "r")


peganinjas = []
for n in arq:
    peganinjas.append(n)
ninjas = [e.replace("\n","") for e in peganinjas]
shuffle(ninjas)

for i in range(3):
    shuffle(ninjas)
lutas = [(ninjas[0],ninjas[1]),
        (ninjas[2],ninjas[3]),
        (ninjas[4],ninjas[5]),
        (ninjas[6],ninjas[7]),
        (ninjas[8],ninjas[9]),
        (ninjas[10],ninjas[11]),
        (ninjas[12],ninjas[13]),
        (ninjas[14],ninjas[15])]

for luta in lutas:
    print("#####" * 5)
    print(f"{luta[0]} x {luta[1]}")
    print("está para começar...")
    sleep(5)
    for i in range(5):
        sleep(5)
        p = [luta[0],luta[1]]
        print(f"{choice(p)} {choice(acoes)} o adversario") 
arq.close()    