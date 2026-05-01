'''EXERCÍCIO 1: Escreva um algoritmo que recebe um número inteiro n > 0, cria um vetor de números reais com n
posições e preenche o vetor com n números aleatórios reais.'''

import random

n = int(input("Digite um número natural: "))

random_vector = []

for i in range(n):
    random_n = random.randint(1,100)
    random_vector.append(random_n)
    
print(f"{', '.join(map(str, random_vector[:-1]))} e {random_vector[-1]} são todos os números gerados!")