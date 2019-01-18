###Titulo: Lista
###Função: Este programa modifica a listagem 6.6 para ler 7 notas ao invés de 5
###Autor: Valmor Mantelli Jr.
###Data: 27/12/2018
###Versão: 0.0.2

### Declaração de variáve 

notas = [0, 0, 0, 0, 0, 0, 0, 0]

soma = 0

x = 0 

### Atribuição de valor e processamento

while x < 7:
	notas [x] = float(input ("Nota %d: " % x))
	soma = soma + notas [x]
	x += 1
x = 0
while x < 7:
	
### Saída

	print("Nota %d: %6.2f" % (x, notas [x]))
	x +=1

print("Média: %6.2f" % (soma / x))

