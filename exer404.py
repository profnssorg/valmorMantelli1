###Titulo: Aumento de salário
###Função: Este programa calcula o aumento para diferente faixas salarias
###Autor: Valmor Mantelli Jr.
###Data: 08/12/20148
###Versão: 0.0.1

# Declaração de variável

sal = 0

var = 0

# Atribuição de valor a variavel

sal = int(input("Diga o salário: "))

#Processamento

if sal <= 1250:  
	var = 0.10
else:
	var = 0.15

aum = sal * var


# Saída

print("O aumento será de R$%.2f" %aum) 

