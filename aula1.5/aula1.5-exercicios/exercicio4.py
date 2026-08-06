'''Escreva um algoritmo que lê um número inteiro n, cria um vetor de inteiros de tamanho n, faz a leitura
de um conjunto de n números inteiros armazenando-os no vetor e depois calcula a somatória dos
números contidos no vetor.
▪ Dica: note que a somatória deverá ser feita após o vetor estar preenchido.
'''

n = int(input("Digite um número natural: "))
soma = 0
vetor = []

for i in range(1, n+1):
    elemento = int(input(f"Digite o {i}º número inteiro: "))
    vetor.append(elemento)

for elemento in vetor:
    soma += elemento

print(f"A soma dos {n} inteiros é {soma}")