###Titulo: Cálculo de  preço
###Função: Este programa calcula o preço do aluguél de um carro
###Autor: Valmor Mantelli Jr.
###Data: 05/12/20148
###Versão: 0.0.2

# Declaração de variável

d = 0

k = 0

# Atribuição de valor a variavel

d = int(input("Diga o número de dias que o carro será alugado: "))

k = int(input("Diga a quantidade de KM percorridos: "))


#Processamento

valor = d*60 + k*0.15


# Saída

print("O valor a ser pago é de R$ %.2f" %valor) 

