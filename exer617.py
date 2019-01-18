###Titulo: Lista de compras
###Função: Este programa verifica se o produto existe e em caso positivo, baixa o estoque
###Autor: Valmor Mantelli Jr.
###Data: 05/01/2019
###Versão: 0.0.5

### Declaração de variáve 

estoque = {}
venda = []
total = 0
operação = 0
preço = 0
custo = 0


### Atribuição de valor 

estoque = {"tomate" : [1000, 2.30], "alface" : [500, 0.45], "batata" : [2001, 1.20], "feijão" : [100, 1.50]}
venda = [["tomate", 5], ["batata", 10], ["alface", 5]]
print ("Vendas:\n")

### Processamento
while True:
	produto = input("Nome do produto (ou fim para sair): ")
	if produto == "fim":
		break
	if produto in estoque:
		quantidade = int(input("Quantidade: "))
		if quantidade <= estoque[produto] [0]:
			preço = estoque[produto] [1]
			custo = preço * quantidade
			print ("%12s: %3d x %6.2f = %6.2f" % (produto, quantidade, preço, custo))
			estoque [produto] [0] -= quantidade
			total += custo
		else:
			print ("A quantidade solicitada não esta disponível no estoque.")
	else:
		print ("Nome do produto inválido")	
print ("Custo total: %21.2f\n" %total)
print ("Estoque:\n")
for chave, dados in estoque.items():

### Saída

	print ("Descrição: ", chave)
	print("Quantidade: ", dados[0])
	print("Preço: %6.2f\n" % dados[1])



