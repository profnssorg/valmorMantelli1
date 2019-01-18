###Titulo: Contagem de cédulas
###Função: Este programa modifica a listagem 5.14 para trabalhar também com notas de R$ 100
###Autor: Valmor Mantelli Jr.
###Data: 26/12/2018
###Versão: 0.0.3

# Declaração de variáve e atribuição de valor

valor = int(input("Digite o valor a pagar: "))

cedulas = 0

atual  = 100

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
		elif atual == 100:
			atual = 50
		elif atual == 50:
			atual = 20
		elif atual == 20: 
			atual = 10
		elif atual == 10:
			atual = 5
		elif atual == 5:
			atual = 1
		cedulas = 0
		
