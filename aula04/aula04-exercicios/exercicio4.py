# Faça um programa que receba 5 valores digitados pelo usuário e, ao final, informe qual é a soma deles.

soma = 0

for i in range(1,6):
    n = float(input(f"Digite o {i}º valor: "))
    soma+=n

print(f"A soma dos 5 valores digitados é igual a {soma}")