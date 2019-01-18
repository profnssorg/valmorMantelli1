###Titulo: Conversor
###Função: Este programa converte número de dias, horas minutos e segundos em segundos
###Autor: Valmor Mantelli Jr.
###Data: 30/11/20148
###Versão: 0.0.2

# Declaração de variável

x = 0

y = 0

z = 0

w = 0

convD = 0

convH = 0

convM = 0

soma = 0


# Atribuição de valor a variavel

x = int(input("Diga a quantidade de dias que deseja converter em segundos: "))

y = int(input("Diga a quantidade de horas que deseja converter em segundos: "))

z = int(input("Diga a quantidade de minutos que deseja converter em segundos: "))

w = int(input("Diga a quantidade de segundos: "))

#Processamento

convD = x * 24 * 60 * 60

convH = y * 60 * 60

convM = z * 60

soma = convD + convH + convM + w
 
# Saída

print("%d dias, %d horas, %d minutos e %d segundos correspondem a %d segundos." %(x, y, z, w, soma))

