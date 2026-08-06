'''Escreva um algoritmo que lê um número inteiro n > 0 e preenche um vetor de caracteres de n
posições.
▪ Depois de preencher o vetor, você deverá inverter o seu conteúdo, ou seja, trocar o conteúdo da
primeira posição (0) com a última (n - 1) a segunda com a penúltima e assim por diante até que o
vetor esteja invertido'''

import random
import string

n = int(input("Digite um número natural: "))
vetor = []

def gerar_alfabeto ():
    alfabeto = string.ascii_letters
    return random.choice(alfabeto)
        
for i in range(n):
    vetor.append(gerar_alfabeto())
    
print(f"Vetor original: {', '.join(vetor[:-1])} e {vetor[-1]}")    

vetor = vetor[::-1]
print(f"Vetor espelhado: {', '.join(vetor[:-1])} e {vetor[-1]}")