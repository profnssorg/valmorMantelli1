###Titulo: Aprovação de emprestimo
###Função: Este programa avalia se libera credito dada a renda
###Autor: Valmor Mantelli Jr.
###Data: 08/12/20148
###Versão: 0.0.4

# Declaração de variáve

val = 0

sal = 0

tempo = 0

prestação = 0


# Atribuição de valor a variavel

sal = float(input("Informe o salário: "))

val = float(input("Informe o valor do imóvel: "))

tempo = int(input("Informe o prazo para pagamento(em anos): "))

# Processamento

prestação = val / (tempo * 12)

if prestação >= sal * 0.3:
	
# Saída
	print ("Nas atuais condições você não teve o empreéstimo aprovado, tente alongar o prazo ou reduzir o valor do imóvel.")
else:
	print ("Seu financiamento foi aprovado, o valor da prestação será de R$ %.2f" %prestação) 

