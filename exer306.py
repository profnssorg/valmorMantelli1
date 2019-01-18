###Titulo: Aprovado ou reprovado
###Função: Esse programa informa se o aluno foi aprovado ou reprovado 
###Autor: Valmor Mantelli Jr.
###Data: 24/11/20148
###Versão: 0.0.1

# Declaração de variável

nota1 = 0

nota2 = 0

nota3 = 0 

# Atribuição de valor a variavel

nota1 = int(input("Digite a primeira nota: "))

nota2 = int(input("Digite a segunda nota: "))

nota3 = int(input("Digite a terceira nota: "))

#Processamento

if nota1 > 7 and nota2 > 7 and nota3 > 7:
	print("Você foi aprovado.")
else:
	print("Você foi reprovado sua besta.")

