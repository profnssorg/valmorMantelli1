###Titulo: Cálculo de multiplos
###Função: Este programa exibe todos os primeiros 10 múltiplos de qualquer número
###Autor: Valmor Mantelli Jr.
###Data: 11/12/20148
###Versão: 0.0.5

# Declaração de variáve

x = 1

y = 0

# Atribuição de valor a variavel

y = int(input("Diga o número que você quer saber os 10 primeiros múltiplos: "))

# Processamento

while x <= 10:

# Saída

	print("%d X %d = %d" % (y, x, x*y))
	x = x + 1
