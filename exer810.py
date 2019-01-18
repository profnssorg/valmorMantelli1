###Título: Função
###Descrição: Este programa apresenta a sequencia de Fibonacci sem recursão
###Autor: Valmor Mantelli Jr.
###Data: 15/01/2018
###Versão 0.0.12

### Declaração de variáveis

a = 0

b = 1

soma = 1

### Entrada de dados

fim = int(input("Quantos termos da sequencia de Fibonacci você gostaria de obter? "))

### Processamento de dados

for n in range (0, fim):

### Saída
	
	print(a)
	soma = b + a
	a = b
	b = soma
	

