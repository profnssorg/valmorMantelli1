###Titulo: Validando número em lista
###Função: Este programa identifica se dois números estão na lista e qual foi achado primeiro
###Autor: Valmor Mantelli Jr.
###Data: 01/01/2019
###Versão: 0.0.6

### Declaração de variáve 

list = [15, 7, 27, 39]

n = 0

s = 0

x = 0

fn = False

fs = False

find = 0

### Atribuição de valor

n = int(input("Digite o primeiro número que procura na lista: "))

s = int(input("Digite o segundo número que procura na lista: "))

### Processamento 

while x  <  len(list):
	if list[x] == n:
		fn = True
		if not fs:
			find = 1
	if list[x] == s:
		fs = True
		if not fn:
			find = 2
	x += 1

### Saída

if fn:
	print ("O número %d foi achado na lista." %n)
else:
	print ("O número %d não consta na lista." %n)
if fs:
	print ("O número %d foi achado na lista." %s)
else:
	print ("O número %d não consta na lista." %s)
if find == 1:
	print ("%d foi achado primeiro" % n)
elif find == 2:
	print ("%d foi achado primeiro." % s,)
else:
	print ("Nenhum dos números foi achado na lista.")

