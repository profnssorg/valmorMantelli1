###Título: Programa palavra secreta.py
###Descrição: Este programa utiliza strings para fazer o desenhpo da lista 7.45
###Autor: Valmor Mantelli Jr.
###Data: 11/01/2018
###Versão 0.0.5

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

l = []

num = 0

indice = ""

y = [] 

z = () 

#Entrada de dados

lista_de_palavras = ["onibus", "mesa", "casa", "paralelepipedo", "biscoito", "arvore", "lua", "ferias", "maça", "pera", "laranja", "banana", "Steelers"]

num = int(input("Digite um numero:"))

indice = lista_de_palavras [(num * 776) % len(lista_de_palavras)]

fig = """
X==:==
X  :
X     
X     
X     
X     
X     
=====

"""

#Processamento dos dados e saída

for x in range(100):
	print()
for y in fig.splitlines():
	l.append(list(y))
while True:
	senha = ""
	for letra in indice:
		senha += letra if letra in acertos else "."
	print (senha)
	if senha == indice:
		print ("Você acertou!!!")
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
			if erros == 1:
				l[3][3] = "0"
			elif erros == 2:
				l[4][3] = "|"
			elif erros == 3:
				l[4][2] = "/"
			elif erros == 4:
				l[4][4] = "\\"
			elif erros == 5:
				l[5][2] = "/"
			elif erros == 6:
				l[5][4] = "\\"
	for z in l:
		print ("".join(z))
	if erros == 6:
		print ("Você perdeu.")
		print ("A palavra a correta é %s" % indice)
		break
