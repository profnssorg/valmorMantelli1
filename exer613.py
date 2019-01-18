###Titulo: Manior e menor valor
###Função: Este programa verifica o maior e o menor valor de uma lista
###Autor: Valmor Mantelli Jr.
###Data: 02/01/2019
###Versão: 0.0.1

### Declaração de variável 

l = []

máximo = 0

mínimo = 0

e = 0 

soma= 0

### Atribuição de valor 

l = [-10, -8, 0, 1, 2, 5, -2, -4]

mínimo = l[0]

máximo = l[1]

### Processamento

for e in l:
	if e < mínimo:
		mínimo = e 
	elif e > máximo:
		máximo = e 
	soma += e 
### Saída

print ("O maior temperatura da lista é de %d graus, a menor é de %d graus e a média é %5.2f graus." % (máximo, mínimo, (soma / len(l))))

