#Escreva um programa que dado um inteiro n positivo calcula e imprime a soma de todos os números inteiros entre 1 e n
soma = 1
n = int(input("Digite um número inteiro e positivo: "))

while n <=0:
    int(input("Digite um número inteiro e positivo: "))
    
for i in range (2, n+1):
    soma += i

print(f"A soma de 1 até {n} é: {soma}")