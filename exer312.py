###Titulo: Cálculo tempo
###Função: Este programa calcula tempo médio de uma viagem
###Autor: Valmor Mantelli Jr.
###Data: 03/12/20148
###Versão: 0.0.1

# Declaração de variável

x = 0

y = 0

# Atribuição de valor a variavel

x = float(input("Diga a distância a ser percorrida(em Km): "))

y = float(input("Diga a velocidade média(Km/h): "))

#Processamento

tempo = x / y

# Saída

print("O tempo para realizar o percurso é de %.2f horas" %tempo) 

