###Título: Função
###Descrição: Este pergunta uma letra e verifica se ela consta na lista
###Autor: Valmor Mantelli Jr.
###Data: 15/01/2018
###Versão 0.0.5

### Declaração de variáveis

l = []

p = ""

### Entrada de dados

p =  input("Diga uma letra para consultar se ela consta na lista: ")

### Processamento de dados

def search (p,lista):
    return p in lista

l = ["x", "y", "w", "z", "r", "s" ]


### Saída

print(search(p, l))
	
