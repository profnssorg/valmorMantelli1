###Titulo: Formação de uma terceira string
###Função: Este programa lê duas strings e gera uma terceira string com as letras comuns a duas primeiras strings
###Autor: Valmor Mantelli Jr.
###Data: 07/01/2019
###Versão: 0.0.1

### Declaração de variáve 

f = ""

s= ""

t = ""

p = ""

### Atribuição de valor 

f = "AAACTBF"

s = "CBT"

### Processamento

for p in f:
	if p in f and p in s: 
	
		t += p

### Saída

if len (t) == 0:
	print ("Não existem letras comuns nas duas listas")
else:	
	print ("As letras comuns entre as variáveis %s e %s são %s" % (f, s, t))



