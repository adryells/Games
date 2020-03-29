from random import randint
salvo = open("dados.txt","a")
#DEFINICAO DE PONTOS E DIFICULDADE
p1 = 0
p2 = 0
#operador = [*,+,-,/]
modo_operacao = input("Adicao,Subtracao,Multiplicacao,Divisao: [+,-,*,/]\n")
#modo_qtdSinais = int(input("1,2 ou 3: "))
modo_dificuldade = int(input("modo:\n1 para facil\n2 para medio\n3 para dificil: "))

#USUARIO A
for a in range(5):
	if modo_dificuldade == 1:
		n = randint(0,10)
		m = randint(0,10)
		if modo_operacao == "+":
			questao = n + m
			print(f"{n} + {m}: ")
		elif modo_operacao == "-":
			questao = n-m
			print(f"{n}-{m}")
		elif modo_operacao == "*":
			questao = n*m
			print(f"{n}*{m}")
		elif modo_operacao == "/":
			questao = float(n/m)
			print(f"{n}/{m}")
	elif modo_dificuldade == 2:
		n = randint(0,50)
		m = randint(0,50)
		if modo_operacao == "+":
			questao = n + m + m
			print(f"{n} + {m} + {m}")
		elif modo_operacao == "-":
			questao = n-m+n
		elif modo_operacao == "*":
			questao = n*m*n
		elif modo_operacao == "/":
			questao = float(n/m/n)
	elif modo_dificuldade == 3:
		n = randint(0,100)
		m = randint(0,100)
		if modo_operacao == "+":
			questao = n + m + n + m + m
		elif modo_operacao == "-":
			questao = n-m-n-n-n
		elif modo_operacao == "*":
			questao = n*m*m*m
		elif modo_operacao == "/":
			questao = float(m/n/m/m)
	else:
		modo_dificuldade = int(input("invalido!\ndigite novamente: "))
	#print(f"{n} * {m}: ")
	#questao = n * m 
	resp1 = float(input("Resposta p1: "))
	if resp1 == questao:
		print("acertou!")
		p1 += 1
	else:
		print("errou!")
		
		
#USUARIO B
for b in range(5):
	if modo_dificuldade == 1:
		n = randint(0,10)
		m = randint(0,10)
		if modo_operacao == "+":
			questao = n + m
			print(f"{n} + {m}: ")
		elif modo_operacao == "-":
			questao = n-m
			print(f"{n}-{m}: ")
		elif modo_operacao == "*":
			questao = n*m
			print(f"{n}*{m}: ")
		elif modo_operacao == "/":
			questao = float(n/m)
			print(f"{n}/{m}: ")
	elif modo_dificuldade == 2:
		n = randint(0,50)
		m = randint(0,50)
		if modo_operacao == "+":
			questao = n + m + m
			print(f"{n} + {m} +{m}: ")
		elif modo_operacao == "-":
			questao = n-m+n
			print(f"{n}-{m}+{n}: ")
		elif modo_operacao == "*":
			questao = n*m*n
			print(f"{n}*{m}*{n}: ")
		elif modo_operacao == "/":
			questao = float(n/m/n)
			print(f"{n}/{m}/{n} : ")
	elif modo_dificuldade == 3:
		n = randint(0,100)
		m = randint(0,100)
		if modo_operacao == "+":
			questao = n + m + n + m + m
			print(f"{n}+{m}+{n}: ")
		elif modo_operacao == "-":
			questao = n - m - n - n - n
			print(f"{n}-{m}-{n}-{n}-{n}")
		elif modo_operacao == "*":
			questao = n*m*m*m
			print(f"{n} * {m} * {m} * {m} ")
		elif modo_operacao == "/":
			questao = float(m/n/m/m)
			print(f"{m}/{n}/{m}/{m}")
	#print(f"{n} * {m}: ")
	#questao = n * m
	resp2 = float(input("Resposta p2:"))
	if resp2 == questao:
		print("acertou!")
		p2+=1
	else:
		print("errou!")
		
#DEFINICAO DE VENCEDOR
if p1 > p2:
	print("P1 vence!")
elif p2>p1: 
	print("P2 vence!")
else:
	print("empate")
print(f"Resultado: p1 {p1} x {p2} p2")
