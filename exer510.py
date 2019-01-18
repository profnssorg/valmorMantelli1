###Titulo: Contagem de questões
###Função: Este programa realiza a contagem de acertos de questões de uma prova
###Autor: Valmor Mantelli Jr.
###Data: 14/12/2018
###Versão: 0.0.1

# Declaração de variáve

pontos = 0

questão = 1

resposta = 0

# Atribuição de valor a variavel e processamento

while questão <= 3:
	resposta = input("Resposta da questão %d: "  %questão)
	if questão == 1 and (resposta == "b" or resposta == "B"):
		pontos  = pontos +1
	if questão == 2 and (resposta == "a" or resposta == "A"):
		pontos = pontos + 1
	if questão == 3 and (resposta == "d" or resposta == "D"):
		pontos = pontos + 1
	questão += 1 	
# Saída

print("O aluno fez %d ponto(s) na prova" %pontos)

	
