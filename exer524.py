###Titulo: Números primos
###Função: Este programa pergunta um número "n" e informa os "n" primeiros números primos 
###Autor: Valmor Mantelli Jr.
###Data: 27/12/2018
###Versão: 0.0.3

### Declaração de variáve 

n = 0

p = 1

y = 3

x = 3

### Atribuição de valor, processamento e saída
n = int(input("Diga quanto números primos você gostaria que fossem exibidos: "))
if n < 0:
	print ("Número primos menores que 0? Ta de sacanagem né? ")
else:
	if n >= 1:
		print ("2")
		while p < n:
			while x < y:
				if y % x == 0:
					break
				x = x + 2
			if x == y:
				print (x)
				p = p + 1 	
			y = y + 2

