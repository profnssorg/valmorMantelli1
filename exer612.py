###Titulo: Altera a listagem 6.33 
###Função: Este programa altera a listagem 6.33 para imprimir o menor valor da lista
###Data: 01/01/2019
###Versão: 0.0.2

### Declaração de variável

l = []

mínimo = 0

e = 0 

### Atribuição de valor 

l = [1, 7, 2, 4]

mínimo = l[0]

### Processamento

for e in l:
	if e < mínimo:
		mínimo = e 

### Saída

print (mínimo)

