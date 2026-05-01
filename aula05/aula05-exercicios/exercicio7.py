'''▪ Crie um programa com uma matriz 3x4
▪ 3 linhas
▪ 4 colunas
▪ Atribua valores aleatórios à todas posições da matriz.
▪ Exiba essa matriz.'''

import random

matriz = [[0] * 4 for i in range(3)]

for i in range(3):
    for j in range(4):
        matriz[i][j] = (random.randint(1,100))

print(matriz)