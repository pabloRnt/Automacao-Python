'''▪ Escreva um algoritmo que lê um número inteiro n > 0 e preenche um vetor de caracteres de n
posições.
▪ Depois de preencher o vetor, você deverá inverter o seu conteúdo, ou seja, trocar o conteúdo da
primeira posição (0) com a última (n − 1) a segunda com a penúltima e assim por diante até que o
vetor esteja invertido.'''

import random
import string

caracteres = string.ascii_letters

n = int(input("Digite um número natural: "))

vetor = random.choices(caracteres, k=8)

for i in range (n):
    vetor.insert(i, vetor[-1])
    vetor.pop(-1)

string = "".join(vetor)

print(string)
