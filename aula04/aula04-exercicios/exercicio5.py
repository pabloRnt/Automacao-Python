#Faça um programa que receba 5 valores digitados pelo usuário e, ao final, informe qual é o maior deles.

maior = None

for i in range(1, 6):
    n = int(input(f"Digite o {i}º valor: "))
    
    if maior == None or n > maior:
        maior = n

print(f"O maior valor é {maior}")