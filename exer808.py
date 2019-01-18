###Título: Função
###Descrição: Este programa calcula o minimo multiplo comum
###Autor: Valmor Mantelli Jr.
###Data: 15/01/2018
###Versão 0.0.3

### Declaração de variáveis



### Entrada de dados



### Processamento de dados

def mdc (a, b):
	if b == 0:
		return a
	return mdc (b,  a% b)
def mmc (a, b):
	return abs(a*b) / mdc (a, b)

### Saída

print ("Mínimo múltiplo comum entre 6 e 8 é %d."  % (mmc(6, 8)))
print ("Mínimo múltiplo comum entre 36 e 8 é %d."  % (mmc(36, 8)))
