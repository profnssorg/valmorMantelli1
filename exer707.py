###Título: Programa jogo da forca.py
###Descrição: Este programa repete a listagem 7.45 e insere ao final das tentativas a palavra secreta
###Autor: Valmor Mantelli Jr.
###Data: 09/01/2018
###Versão 0.0.1

# Declaração de variáveis

palavra = ""

digitadas = []

acertos = []

erros = []

senha = ""

letra = 0

x = 0

tentativa = ""

erros = 0

linha2 = ""

linha3 = ""

#Entrada de dados

palavra = input("Digite a palavra secreta: ") .lower() . strip()

#Processamento dos dados e saída

for x in range(100):
	print()
while True:
	senha = ""
	for letra in palavra:
		senha += letra if letra in acertos else "."
	print (senha)
	if senha == palavra:
		print ("Você acertou!!!")
		break
	tentativa = input ("\nDigite uma letra: ").lower().strip()
	if tentativa in digitadas:
		print("Voçe ja tentou essa letra!")
		continue
	else:
		digitadas += tentativa
		if tentativa in palavra:
			acertos += tentativa
		else:
			erros += 1
			print ("Você errou!!!")
	print ("X==:==\nX  :  ")
	print ("X  0  " if erros >= 1 else "x")
	linha2 = ""
	if erros ==2:
		linha2 = "  |  "
	elif erros == 3:
		linha2 = " \|  "
	elif erros >= 4:
		linha2 = " \|/ "
	print ("X%s" %linha2)
	linha3 = ""
	if erros == 5:
		linha3 += " /  "
	elif erros >= 6:
		linha3 += " / \ "
	print ("X%s" % linha3)
	print ("X\n==========")
	if erros == 6:
		print ("Enforcado!")
		print ("A palavra a correta é %s." % palavra)
		break
