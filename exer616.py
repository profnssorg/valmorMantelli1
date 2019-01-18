###Titulo: Altera a listagem 6.44
###Função: Este programa altera a listagem 6.44 e ordena listas do maior para o menor valor
###Autor: Valmor Mantelli Jr.
###Data: 05/01/2019
###Versão: 0.0.1

### Declaração de variáve 

l = [1, 2, 3, 4, 5]

fim = len(l)  #1  Marca a quantidade de elementos

### Atribuição de valor 

### Processamento

while fim > 1:  #2  Verifica se o fim>1
	trocou = False  #3  Indica que não ocorreu nenhuma troca
	x = 0  #4  Variável X iniciada no programa		
	while x < (fim -1):  #5  Condição de saída: X seja anterior ao último elemento
		if l[x] < l[x+1]:  #6	Comparação do elemento atual da lista com o próximo. Desejamos que o próximo seja maior que o atual. Como a comparação é sempre entre dois números precisamos visitar a lista várias vezes. Se a condição for verdadeira, os elementos estão fora de ordem
			trocou = True  #7  Marcamos que efetuamos a troca
			temp = l[x]  #8  Variável temporária auxiliar que recebe os números
			l[x] = l[x+1]
			l[x+1] = temp
		x += 1
	if not trocou:  #9 Verifica se algo foi trocado na repetição anterior. Se não foi o programa para.
		break
	fim -= 1  #10 Caso contrario, como a última posição esta correta, diminuiremos o tamanho de fim , para que não precesimos verificar novamente
for e in l:

### Saída

	print (e)



