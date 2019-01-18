###Titulo: Preço de passagem
###Função: Este programa calcula o preço de uma passagem para diferentes distâncias
###Autor: Valmor Mantelli Jr.
###Data: 08/12/20148
###Versão: 0.0.1

# Declaração de variável

dist = 0

preço = 0

valor = 0

# Atribuição de valor a variavel

dist = int(input("Diga a distância a ser percorrida: "))

#Processamento
if dist <= 200:  
	preço = 0.50
else:
	preço = 0.45

valor = dist * preço


# Saída

print("O valor da passagem é de R$%.2f" %valor) 

