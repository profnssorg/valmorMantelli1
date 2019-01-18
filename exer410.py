###Titulo: Conta de luz 
###Função: Este programa calcula a conta de luz de acordo com a categoria e o consumo
###Autor: Valmor Mantelli Jr.
###Data: 08/12/20148
###Versão: 0.0.3

# Declaração de variáve

k = 0

preço = 0


# Atribuição de valor a variavel

k = float(input("Informe a quantidade de energia consumida em KWh: "))

tipo = input("Informe o tipo de instalação residencia(R), industrial(I) ou comercial(C): ")

# Processamento

if tipo == "R": 
	if k <= 500:
		preço = k * 0.4
	else:
		preço = k * 0.65
elif tipo == "I":
	if k <= 5000:
		preço = k * 0.55
	else:
		preço = k * 0.6
elif tipo == "C":
	if k <= 1000:
		preço = k * 0.55
	else:
		preço = k * 0.6
else:
	
# Saída
	print("Você informou um tipo de instação incorreta, reinicie o processo")

print ("O Valor da sua conta de energia é de R$ %.2f" %preço) 

