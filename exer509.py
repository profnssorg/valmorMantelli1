###Titulo: Divisão através de repetidas subtrações
###Função: Este programa realiza a divisão de dois números através de sucessivas subtrações e apresenta ainda apresenta o resto
###Autor: Valmor Mantelli Jr.
###Data: 14/12/2018
###Versão: 0.0.1

# Declaração de variáve

x = 0

y = 0

w = 0

z = 1

div = 0

resto = 0

# Atribuição de valor a variavel

x = int(input("Diga o primeiro número: "))

y = int(input("Diga por qual número deseja dividir: "))

div = x

# Processamento

while x >= y:
	x -= y
	w += 1 	
resta = x

# Saída

print("%d / %d = %d e sobra %d" %(div, y, w, resta))

	
