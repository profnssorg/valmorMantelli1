###Titulo: Calculo de aumento
###Função: Este programa calcula o aumento de salário
###Autor: Valmor Mantelli Jr.
###Data: 30/11/20148
###Versão: 0.0.2

# Declaração de variável

x = 0

y = 0

# Atribuição de valor a variavel

x = int(input("Diga o salário: "))

y = float(input("Diga o percentual de aumento: "))

#Processamento

ns = x * (y/100) + x

# Saída

print("O novo salário é de %.2f" %ns) 

