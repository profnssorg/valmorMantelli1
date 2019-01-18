###Título: Função
###Descrição: Este programa calcula o maior divisor comum
###Autor: Valmor Mantelli Jr.
###Data: 15/01/2018
###Versão 0.0.1

### Declaração de variáveis



### Entrada de dados



### Processamento de dados

def mdc(a, b):
	if b == 0:
		return a
	return mdc (b,  a% b)

### Saída

print ("Maior divisor comum entre 2 e 0 é %d."  % (mdc(2, 0)))
print ("Maior divisor comum entre 9 e 4 é %d."  % (mdc(9, 4)))
