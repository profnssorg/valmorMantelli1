###Titulo: Contagem de cédulas e modedas
###Função: Este programa modifica a listagem 5.14 para incluir também moedas de R$ 0,001
###Autor: Valmor Mantelli Jr.
###Data: 26/12/2018
###Versão: 0.0.1

# Declaração de variáve e atribuição de valor

valor = float(input("Digite o valor a pagar: "))

cedulas = 0

atual  = 100

apagar = valor

# Processamento e Saída

while True:
	if atual <= apagar:
		apagar -= atual
		cedulas += 1
	else:
		if atual >= 1: 
			print ("%d cédula(s) de R$%d"  % (cedulas, atual))
		else:
			print ("%d moeda(s) de R$%0.3f" % (cedulas, atual))
		if apagar < 0.001:
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
		elif atual == 1:
			atual = 0.5
		elif atual == 0.5:
			atual = 0.10
		elif atual == 0.10:
			atual = 0.05
		elif atual == 0.05:
			atual = 0.02
		elif atual == 0.02:
			atual = 0.01
		elif atual == 0.01:
			atual = 0.005
		elif atual == 0.005:
			atual = 0.002
		elif atual == 0.002:
			atual = 0.001 
		cedulas = 0
		
