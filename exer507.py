###Titulo: Cálculo de multiplos
###Função: Este programa exibe todos os primeiros os múltiplos de qualquer número que o usuário desejar
###Autor: Valmor Mantelli Jr.
###Data: 11/12/20148
###Versão: 0.0.5

# Declaração de variáve

x = 0

y = 0

beg = 0

end = 0



# Atribuição de valor a variavel

y = int(input("Diga um número: "))

beg = int(input("Diga o primeiro múltiplo que você deseja saber: "))

end = int(input("Diga qual o último múltiplo que você deseja saber: ")) 

# Processamento

x = beg

while x <= end:

# Saída

	print("%d X %d = %d" % (y, x, x*y))
	x = x + 1
	
