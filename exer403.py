###Titulo: Maior valor
###Função: Este programa pergunta tres números e exibe o de maior valor
###Autor: Valmor Mantelli Jr.
###Data: 08/12/20148
###Versão: 0.0.3

# Declaração de variável

a = 0

b = 0

c = 0

maior = 0

menor = 0

# Atribuição de valor a variavel

a = int(input("Diga o primeiro número inteiro: "))

b = int(input("Diga o segundo número inteiro: "))

c = int(input("Diga o terceiro número inteiro: "))

#Processamento

if a > b and a > c:	
	maior = a
if b > a and b > c:
	maior = b
if c > a and c> b:
	maior = c	
if a < b and a < c:
	menor = a
if b < a and b < c:
 	menor  = b
if c < a and c < b:
	menor = c

# Saída

print("O maior dos números informados é o %d e o menor é o %d." %(maior, menor)) 

