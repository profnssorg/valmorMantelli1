###Titulo: Validando número em lista
###Função: Este programa identifica se um deteminados números estão na lista e qual foi achado primeiro e sua posição na lista
###Autor: Valmor Mantelli Jr.
###Data: 01/01/2019
###Versão: 0.0.3

### Declaração de variáve 

list = [15, 7, 27, 39]

p = 0

v = 0

x = 0

fn = False

fs = False

find = 0

findp = -1

findv = -1

### Atribuição de valor

p = int(input("Digite o primeiro número que procura na lista: "))

v = int(input("Digite o segundo número que procura na lista: "))

### Processamento 

while x  <  len(list):
	if list[x] == p:
		fn = True
		findp = x
		if not fs:
			find = 1
	if list[x] == v:
		fs = True
		findv = x
		if not fn:
			find = 2
	x += 1

### Saída

if findp != -1:
	print ("O número %d foi achado na lista, na posição %d." % (p, findp))
else:
	print ("O número %d não consta na lista." %p)
if findv != -1:
	print ("O número %d foi achado na lista, na posição %d." % (v, findv))
else:
	print ("O número %d não consta na lista." %v)
if find == 1:
	print ("%d foi achado primeiro" % p)
elif find == 2:
	print ("%d foi achado primeiro." % v)
else:
	print ("Nenhum dos números foi achado na lista.")

