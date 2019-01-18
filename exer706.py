###Titulo: Leitor de string
###Função: Este programa lê três strings e substitui na primeira os caracteres da segunda e terceira
###Autor: Valmor Mantelli Jr.
###Data: 08/01/2019
###Versão: 0.0.13


# Declaração de variáveis

f = ""

s = ""

t = ""

x = ""

p = ""

y = 0

#Entrada de dados

f = input("Digite a primeira sequência de letras: ")

s = input("Digite a segunda sequência de letras: ")

t = input("Digit a terceira sequencia de letras: ")


#Processamento dos dados e saída

if len (s) == len(t): # Verifica se o tamanho da segunda e terceira strings são iguais
	x = ""
	for p in f:
		y =s.find(p)
		if y != -1:
			x += t[y]
		else:
			x += p
	if x == "":
		print("Não sobraram caracteres para serem retirados.")
	else:
		print("Os caracteres %s foram trocados por %s em %s gerando uma nova sequência %s."  % (s, t, p, x))
else:
	print ("A segunda e terceira sequência de caracteres precisam ter o mesmo tamanho")
