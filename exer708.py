###Título: Programa palavra secreta.py
###Descrição: Este programa insere uma lista de palavras através de um indice
###Autor: Valmor Mantelli Jr.
###Data: 09/01/2018
###Versão 0.0.17

# Declaração de variáveis

lista_de_palavras = ""

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

num = 0

indice = ""

#Entrada de dados

lista_de_palavras = ["onibus", "mesa", "casa", "paralelepipedo", "biscoito", "arvore", "lua", "ferias", "maça", "pera", "laranja", "banana", "Steelers"]

num = int(input("Digite um numero:"))

indice = lista_de_palavras [(num * 776) % len(lista_de_palavras)]

#Processamento dos dados e saída


for x in range(100):
	print()
while True:
	senha = ""
	for letra in indice:
		senha += letra if letra in acertos else "."
	print (senha)
	if senha == indice:
		print ("Bingo, você acertou!!!")
		break
	tentativa = input ("\nDigite uma letra: ").lower().strip()
	if tentativa in digitadas:
		print("VocÇe ja tentou essa letra!")
		continue
	else:
		digitadas += tentativa
		if tentativa in indice:
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
		print ("A palavra a correta é %s" % indice)
		break
