###Titulo: Calculo de multa
###Função: Este programa calcula o valor da multa de acordo com a velocidade
###Autor: Valmor Mantelli Jr.
###Data: 08/12/20148
###Versão: 0.0.1

# Declaração de variável

v = 0

resultado = 0

# Atribuição de valor a variavel

v = int(input("Diga qual a velocidade do seu carro(em km/h): "))

#Processamento e saída

if v <= 80:
	print ("Você esta dentro do limite de velocidade e não foi multado.")
else:
	resultado = (v - 80) *5
	print (" Você excedeu o limite permitido de velocidade e foi multado em R$ %.2f" %resultado)
	
