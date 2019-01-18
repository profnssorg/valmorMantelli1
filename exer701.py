###Titulo: Procura de strings
###Função: Este programa procura uma string dentro de outra
###Autor: Valmor Mantelli Jr.
###Data: 07/01/2019
###Versão: 0.0.1

### Declaração de variáve 

f = ""

s= ""

p = ""

### Atribuição de valor 

f = "AABBEFAATT"

s = "BE"

p = f.find(s)

### Processamento e saída

if p < 0: 
	print ("%s não foi encontrado em %s" % (s, f))
else:	
	print ("%s foi encontrado na posição %d" % (s, p))


