from random import choice
import time
pergunta = [1,2,3,4]
Choice = choice(pergunta)
#acerto = False
dur = 60
if Choice == 4:
	#time.sleep(60)
	inicio = time.time()
	print("Assinale a opção que completa a seqüência:\n 2 – 3 – 4 – 11 – 12 – 13 – 17 – 18 – ( ) \na) 24 \nb) 20\nc) 23\nd) 19\ne) 25\n")
	resposta = input("Resposta: ")
	fim = time.time()
	
	#ses
	if resposta in "Aa":
		print("Incorreta,A seqüência é formada pela série de três números consecutivos, portanto o próximo é o 19. Portanto, D.")
	if resposta in "Bb":
		print("Incorreta,A seqüência é formada pela série de três números consecutivos, portanto o próximo é o 19. Portanto, D.")
	if resposta in "Cc":
		print("Incorreta,A seqüência é formada pela série de três números consecutivos, portanto o próximo é o 19. Portanto, D.")
	if resposta in "Dd":
		print("Correta!!!\nA seqüência é formada pela série de três números consecutivos, portanto o próximo é o 19. Portanto, D.")
		#acertos.append(choice)
		dur+=10
		#mpo = fim - inicio
		#print(tempo)
elif Choice == 3:
	inicio = time.time()
	print("A negação de “hoje é segunda-feira e amanhã não choverá” é: \n a) hoje não é segunda-feira e amanhã não choverá\n b) hoje não é segunda-feira ou amanhã choverá\n c) hoje não é segunda-feira então amanhã choverá\n d) hoje não é segunda-feira nem amanhã choverá\n e) hoje é segunda-feira ou amanhã choverá\n")
	resposta = input("resposta:")
	fim = time.time()
	if resposta in "aA":
		print('Incorreto,a negação da frase completa será: “hoje não é segunda-feira ou amanhã choverá” o que nos remete à alternativa B.')
	if resposta in "bB":
		print("Correta!\n a negação da frase completa será: 'hoje não é segunda feira ou amanhã nao choverá', o que nos remete à alternativa B")
		dur+=10
	if resposta in "cC":
		print("incorreta!\n a negação da frase completa será: 'hoje não é segunda feira ou amanhã nao choverá', o que nos remete à alternativa B")
	if resposta in "Dd":
		print("incorreta!\n a negação da frase completa será: 'hoje não é segunda feira ou amanhã nao choverá', o que nos remete à alternativa B")
	if resposta in "Ee":
		print("incorreta!\n a negação da frase completa será: 'hoje não é segunda feira ou amanhã nao choverá', o que nos remete à alternativa B")
elif Choice == 2:
	inicio = time.time()
	print('Adão tem três primas que moram em outra cidade, Ana, Beatriz e Carla, mas nunca lembra de seus nomes.\nEle sabe que uma é loira, uma é ruiva e uma é morena.\nCada uma delas é filha de um de seus tios, José, Jaime e Jairo.\nA mãe de Adão deixou o seguinte bilhete para ajudá-lo:\n"A loira não é filha de Jaime nem de Jairo.\nA morena não é Ana nem Beatriz.\nAna não é ruiva.\nA ruiva não é filha de Jaime."\nA)Ana é loira e filha de José.\nB) Carla é morena e filha de Jairo.\nC)Ana é ruiva e filha de José.\nD)Beatriz é loira e filha de Jairo.\nE)Carla é morena e filha de José.')
	resposta = input("Resposta: ")
	fim = time.time()
	if resposta in "aA":
		print("Correta!!!,Sabemos que Ana não é ruiva, e que nem Ana e nem Beatriz são morenas. Portanto, só Ana pode ser loira.\nComo a Loira não é filha de Jaime e nem de Jairo, sabemos que Ana só pode ser filha de José:\nAna: loira // José\nBeatriz: ruiva ou morena // Jaime ou Jairo\nCarla: ruiva ou morena //Jaime ou Jairo\nCom isso em mãos verifica-se que a resposta correta é A")
		dur+=10
	if resposta in "eEiIoOuU":
		print("Incorreta!!!\nSabemos que Ana não é ruiva, e que nem Ana e nem Beatriz são morenas. Portanto, só Ana pode ser loira.\nComo a Loira não é filha de Jaime e nem de Jairo, sabemos que Ana só pode ser filha de José:\nAna: loira // José\nBeatriz: ruiva ou morena // Jaime ou Jairo\nCarla: ruiva ou morena //Jaime ou Jairo\nCom isso em mãos verifica-se que a resposta correta é A")

elif Choice == 1:
	inicio = time.time()
	print("Selecione a opção correta que preenche a lacuna da série:\n MCD, NEF, OGH,____, QKL\na) CMN\nb) UJI\nc) PIJ\nd) IJT")
	resposta = input("Resposta:")
	fim = time.time()
	if resposta in "Aa":
		print(" Resposta: c\nExistem duas séries alfabéticas.\nA primeira série está baseada na primeira letra : MNOPQ.\nA segunda série envolve as duas letras seguintes: CD, EF, GH, IJ, KL.")
	if resposta in "Bb":
		print(" Resposta: c\nExistem duas séries alfabéticas.\nA primeira série está baseada na primeira letra : MNOPQ.\nA segunda série envolve as duas letras seguintes: CD, EF, GH, IJ, KL.")
	if resposta in "Cc":
		print(" Correto!!!,\nExistem duas séries alfabéticas.\nA primeira série está baseada na primeira letra : MNOPQ.\nA segunda série envolve as duas letras seguintes: CD, EF, GH, IJ, KL.")
		dur+=10
	if resposta in "dD":
		print(" Resposta: c\nExistem duas séries alfabéticas.\nA primeira série está baseada na primeira letra : MNOPQ.\nA segunda série envolve as duas letras seguintes: CD, EF, GH, IJ, KL.")
#print(Choice)
tempo = (fim - inicio)
pontuacao = dur - tempo
print(f"Voce demorou {tempo:.2f} segundos para responder e recebeu +{pontuacao:.2f} pontos de logica")