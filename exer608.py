###Titulo: Validando número em lista
###Função: Este programa identifica se um deteminado número esta na lista e qual sua posição
###Autor: Valmor Mantelli Jr.
###Data: 01/01/2019
###Versão: 0.0.3

### Declaração de variáve 

list = [15, 7, 27, 39]

n = 0

x = 0

### Atribuição de valor

n = int(input("Digite o número que procura na lista: "))


### Processamento 

while x  <  len(list):
	if list[x] == n:
		break
	x += 1
if x < len(list):

### Saída

	print ("O número %d esta na posição %d da lista." % (n, x ))
else:
	print ("O número %d não consta na lista." %n )
