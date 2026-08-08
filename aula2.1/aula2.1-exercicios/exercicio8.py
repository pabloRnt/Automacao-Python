'''Faça um programa que realize a soma de duas matrizes, com mesmas dimensões. Seu programa deve
ter 2 matrizes A e B de números inteiros. A terceira matriz deve ser a soma de A com B.'''

from random import randint

linhas = randint(1,5)
colunas = randint(1,5)

matriz_a  = [[randint(-5,5) for coluna in range(colunas)] for linha in range(linhas)]
matriz_b  = [[randint(-5,5) for coluna in range(colunas)] for linha in range(linhas)]

matriz_soma = []

matriz_soma  = [
    [matriz_a[linha][coluna] + matriz_b[linha][coluna] for coluna in range(colunas)] for linha in range(linhas)]

print(matriz_a, "+", matriz_b, "=")
print(matriz_soma)