'''▪ Escreva um algoritmo que recebe um número inteiro n > 0, cria um vetor de números reais com n
posições e preenche o vetor com n números aleatórios reais.
▪ Depois de preenchido o vetor, imprima na tela todos os números gerados. '''

from random import randint

n = int(input("Digite um número natural: "))

vetor = [randint(-1000,1000) for i in range(n)]
print(vetor)