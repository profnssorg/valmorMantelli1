###Título: Função
###Descrição: Este pergunta uma letra e verifica se ela consta na lista
###Autor: Valmor Mantelli Jr.
###Data: 16/01/2018
###Versão 0.0.5

### Declaração de variáveis

import random

n = 0

chances = 0

### Entrada processamento de dados e saída de dados

n = random.randint(1, 6)

while chances < 3:
        x = int(input("Escolha um número entre 1 e 6:"))
        if x == n:
                print("Você acertou!")
                break
        else:
                print("Você errou.")
        chances += 1

