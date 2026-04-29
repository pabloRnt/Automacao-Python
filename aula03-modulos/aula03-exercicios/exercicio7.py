#Exercício 7
soma = 0
n = int(input("Digite um número inteiro: "))

while n <= 0:
    n = int(input("Digite um número inteiro e POSITIVO: "))
    
for i in range (1,n+1):
    soma+=i
print(f"A soma de 1 até {n} é: {soma}")