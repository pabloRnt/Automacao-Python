#Faça um programa que receba um número n

n = int(input("Digite um número inteiro: "))

for i in range(0,26):
    print(f"{i} X {n} = {i*n}")
    