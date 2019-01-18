###Titulo: Formação de uma terceira string
###Função: Este programa le duas strings e gera uma terceira com as letras de apenas uma delas
###Autor: Valmor Mantelli Jr.
###Data: 07/01/2019
###Versão: 0.0.1

### Declaração de variáve 

f = ""

s= ""

t = ""

q= ""

p = ""

### Atribuição de valor 

f = "CTA"

s = "ABC"

t = "BT"

### Processamento

for p in f:
	if p in f and p in s:
		q += p
for p in s:
	if p in f and p in t:
		q += p
for p in t:
	if p in s and p in t:
		q += p
### Saída

if len (t) == 0:
	print ("Não existem letras comuns nas duas listas")
else:	
	print ("As letras que aparecem em ao menos duas listas são:  %s" % q)



