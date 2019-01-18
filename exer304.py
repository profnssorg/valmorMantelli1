###Titulo: Condicionantes (True and False)
###Função: utilização de condicionantes
###Autor: Valmor Mantelli Jr.
###Data: 24/11/20148
###Versão: 0.0.1

# Declaração de variável
salario = 0
# Atribuição de valor a variavel
salario = int(input("Digite seu salário R$: "))

#Processamento

if salario <= 1200:
	print("Você não precisa pagar imposto.")
else:
	print("Você deve pagar imposto.")

