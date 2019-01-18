###Titulo: Contagem de cédulas e modedas
###Função: Este programa le o valor e apresenta a quantidade de cédulas para pagar com repetição
###Autor: Valmor Mantelli Jr.
###Data: 27/12/2018
###Versão: 0.0.3

# Declaração de variáve e atribuição de valor

while True:
	valor = float(input("Digite o valor a pagar: "))
	if valor == 0:
		break	
	cedulas = 0

	atual  = 50

	apagar = valor

# Processamento e Saída

	while True:
		if atual <= apagar:
			apagar -= atual
			cedulas += 1
		else:
			print ("%d cédula(s) de R$%d"  % (cedulas, atual))
			if apagar == 0:
				break
			elif atual == 50:
				atual = 20
			elif atual == 20: 
				atual = 10
			elif atual == 10:
				atual = 5
			elif atual == 5:
				atual = 1
			cedulas = 0
		
