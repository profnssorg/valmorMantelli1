###Titulo: Testador
###Função: Este programa testa se uma sequencia de parenteses esta na ordem correta 
###Autor: Valmor Mantelli Jr.
###Data: 01/01/2019
###Versão: 0.0.2

### Declaração de variáve 

seq = 0

conj = [] 

x = 0

### Atribuição de valor

seq = str(input("Digite a sequencia de parênteses que você deseja testar: "))


### Processamento 
while x  <  len(seq):
	if seq[x] == "(":
		conj.append("(")
	if seq[x] == ")":
		if len(conj) > 0:
			cima = conj.pop(-1)
		else:
			conj.appen ("(")
			break
	x+=1
if len(conj) == 0:

### Saída
	print ("Os parênteses estão ordenados de forma correta")
else:
	print ("Erro, existe uma inconsistência na ordenação dos parênteses")
