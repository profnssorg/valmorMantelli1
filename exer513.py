###Titulo: Taxa de juros de uma dívida
###Função: Este programa faz cálculo de juros de uma divida
###Autor: Valmor Mantelli Jr.
###Data: 20/12/2018
###Versão: 0.0.2

# Declaração de variáve

pv = 0

i = 0

n = 0

parc = 0

# Atribuição de valor a variavel 

pv = float(input("Insira o valor da dívida R$: "))

i = float(input("Insira a taxa de juros mensal: "))

parc = float(input("Insira o valor que você deseja pagar mensalmente você deseja pagar mensalmente R$: "))

# Processamento
if parc <= (pv * (i / 100)):
	print ("O valor da parcela é inferior aos juros da dívida. Insira um valor de parcela superior ao anterior.")
else:
	saldo = pv
	jp = 0
	while saldo > parc:
		j = saldo * i / 100
		saldo = saldo + j - parc
		jp = jp + j
		print ("O saldo no mês %d é de R$%.2f" % (n , saldo)) 
		n = n + 1       
# Saída
	print ("A dívida será paga em %d parcelas, com um total de juros de R$%.2f." %  ( n , jp ))
	print ("O saldo da operação é de R$%.2f" % saldo)
