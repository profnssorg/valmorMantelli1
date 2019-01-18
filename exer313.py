###Titulo: Conversor de temperatura
###Função: Este programa converte a temperatura de Celsius para Farenheit 
###Autor: Valmor Mantelli Jr.
###Data: 03/12/20148
###Versão: 0.0.1

# Declaração de variável

C = 0

# Atribuição de valor a variavel

C = int(input("Digite a temperatura em graus Celsius: "))


#Processamento

F = ((9 * C)/5 + 32)


# Saída

print("O equivalente a %d graus Celsius são %.2f graus Farenheit" %(C, F)) 

