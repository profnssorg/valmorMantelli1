###Titulo: Palindromo
###Função: Este programa identifica se determinado número é um palíndromo
###Autor: Valmor Mantelli Jr.
###Data: 27/12/2018
###Versão: 0.0.2

### Declaração de variáve 

p = 0

u = 0

n = 0


### Atribuição de valor

n = input ("Digite o número que deseja verificar: ")

### Processamento

u = len(n)-1 
while u  >= p and n[p] == n[u]:
	u = u - 1
	p = p + 1
	
### Saída
if n[p] == n[u]:
	print("%s é palíndromo" % n)

else:
	print("%s não é palíndromo" % n)

