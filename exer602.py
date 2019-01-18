###Titulo: Lista
###Função: Este programa forma uma terceira lista a partir das duas primeiras
###Autor: Valmor Mantelli Jr.
###Data: 31/12/2018
###Versão: 0.0.2

### Declaração de variáve 

list1 = []

list2 = []

list3 = []

n = 0

x = 0


### Atribuição de valor

while True:
	n = int(input("Digite os valores da lista 1 (ou 0 para sair): "))
	if n == 0:
		break
	list1.append (n)
while True:
	n = int(input("Digite os valores da lista 2 (ou 0 para sair): "))
	if n == 0:
		break
	list2.append (n)

### Processamento

list3 = list1 [:]
list3.extend (list2)

while x < len(list3):
	
### Saída

	print ("%d: %d" % (x, list3 [x]))
	x +=1 

