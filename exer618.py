###Titulo: Dicionário
###Função: Programa gerador dicionário
###Autor: Valmor Mantelli Jr.
###Data: 05/01/2019
###Versão: 0.0.2

### Declaração de variáve 

dic = 0

d = {}

letra = 0


### Atribuição de valor 

dic = input("Digite uma frase: ")

### Processamento
for letra in dic:
	if letra in d:
		d[letra] = d[letra] + 1 
	else:
		d[letra] = 1

### Saída

print(d)



