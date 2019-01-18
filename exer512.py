###Titulo: Taxa de juros
###Função: Este programa faz cálculo de juros
###Autor: Valmor Mantelli Jr.
###Data: 19/12/2018
###Versão: 0.0.6

# Declaração de variáve

pv = 0

i = 0

n = 1

v = 0

# Atribuição de valor a variavel 

pv = float(input("Insira o valor depositado R$: "))

i = float(input("Insira a taxa de juros:  "))

v = float(input("Insira o aporte mensal que deseja fazer R$: "))

fv = pv

# Processamento

while n <= 24:
	fv = fv + v + (fv * (i / 100)) 
	print ("O valor referente ao mes %d é de R$%.2f" % (n , fv))
	n = n + 1 	
# Saída

print ("O valor acumulado em juros foi de R$%.2f" % (fv - pv))

	
