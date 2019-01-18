###Titulo: Numeros e operações
###Função: Este programa pergunta dois números e a operação a ser realizada com eles
###Autor: Valmor Mantelli Jr.
###Data: 08/12/20148
###Versão: 0.0.1

# Declaração de variável

a = 0

b = 0

op = 0

res = 0

# Atribuição de valor a variavel

a = int(input("Diga o primeiro número: "))

b = int(input("Diga o segundo número: "))

op = input("Insira o simbolo da operação que deseja realiza com os números: ")

#Processamento
if op == "+":
	res = a + b
elif op == "-":
	res = a - b
elif op == "*":
	res = a * b
elif op == "/":
	res = a / b
else:

# Saída
	print ("Você digitou um operador inválido, tente novamente")
if res % 1 == 0:
	print ("O resultado da operação é %d" %res) 
else:
	print ("O resultado da operação é %0.2f" %res) 

