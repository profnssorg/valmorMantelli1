###Titulo: Cálculo desconto
###Função: Este programa calcula "lo descontito por la manchita".
###Autor: Valmor Mantelli Jr.
###Data: 03/12/20148
###Versão: 0.0.1

# Declaração de variável

x = 0

y = 0

# Atribuição de valor a variavel

x = float(input("Diga o valor da mercadoria: "))

y = float(input("Diga o percentual de desconto: "))

#Processamento

ns = x - (x * (y/100))

# Saída

print("O valor da mercadoria é %.2f" %ns) 

