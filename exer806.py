###Título: Função
###Descrição: Este programa é uma modificação da listagem 8.8
###Autor: Valmor Mantelli Jr.
###Data: 15/01/2018
###Versão 0.0.

### Declaração de variáveis

L = []

total = 0

x = 0

### Entrada de dados

L=[1,7,2,9,15]

### Processamento de dados

def soma(L):
	total = 0
	for x in L:
		total += x
	return total

### Saída

print(soma(L))
print(soma([7,9,12,3,100,20,4]))
