''' Faça um programa que realize a soma de duas matrizes, com mesmas dimensões. Seu programa deve
ter 2 matrizes A e B de números inteiros. A terceira matriz deve ser a soma de A com B'''

import random

linha = int(input("Digite o número de linhas das matrizes: "))
coluna = int(input("Digite o número de colunas das matrizes: "))

matriz_a = [[0] * coluna for i in range(linha)]
matriz_b = [[0] * coluna for i in range(linha)]
matriz_soma = [[0] * coluna for i in range(linha)]

for i in range (linha):
    for j in range(coluna):
        matriz_a[i][j] = random.randint(0,10)
        matriz_b[i][j] = random.randint(0,10)
        matriz_soma[i][j] = matriz_a[i][j] + matriz_b[i][j]

print(f"Matriz A: {matriz_a}")
print(f"Matriz B: {matriz_b}")
print(f"Soma ---> {matriz_soma}")