###Título: Função
###Descrição: Este programa é uma modificação da listagem 8.5
###Autor: Valmor Mantelli Jr.
###Data: 15/01/2018
###Versão 0.0.2

### Declaração de variáveis

L = []

### Entrada de dados

L = [10, 20, 25, 30]

### Processamento de dados

def pesquise(lista, valor): #função de busca
	if valor in lista: # varre a lista	
		return lista.index(valor) # indica o valor a ser retorna
	return None  #se não estiver na lista, retorna None

### Saída

print (pesquise(L, 25)) 
print (pesquise(L, 27))
