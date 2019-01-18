###Titulo: raiz quadrada
###Função: Este programa calcula a raiz quadrada pelo método de Newton
###Autor: Valmor Mantelli Jr.
###Data: 27/12/2018
###Versão: 0.0.3

### Declaração de variáve 

n = 0

b = 2

p = 0


### Atribuição de valor
while True:
	n = float(input("Diga o número que deseja encontrar a raiz quadrada(ou 0 para sair): "))
	if n == 0:
		break
### Processamento
	if n < 0:
		print ("Números positivos né meu querido")
	else:	
		while abs(n - (b * b)) > 0.00001:
			p =  (b + (n / b)) / 2
			b = p
### Saída
		print ("A raiz quadrada de %.4f é aproximadamente %5.4f" % (n, p))


