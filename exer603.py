###Titulo: Lista
###Função: Este programa gera uma terceira lista a partir das duas primeiras, excluindo os números repetidos
###Autor: Valmor Mantelli Jr.
###Data: 31/12/2018
###Versão: 0.0.2

### Declaração de variáve 

list1 = []

list2 = []

list3 = []

finalList = []

n = 0

x = 0

y = 0


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

finalList = list1 [:]
finalList.extend (list2)

while x < len (finalList):
	y = 0
	while y < len (list3):  #enquanto  y > tamanho da list3
		if finalList [x] == list3 [y]: #se o elemento x da finalList for = ao elemento y da list3 => parar
			break
		y += 1
	if y == len (list3): #quando y for = ao tamano da list 3
		list3.append (finalList [x]) #adicionar os elementos da finalList na list3
	x += 1
x = 0
while x < len (list3):	
	
### Saída

	print ("%d: %d" % (x, list3 [x]))
	x +=1 

