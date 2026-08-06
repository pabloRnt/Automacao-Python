#Exercício 6
n = int(input("Digite um número: "))
soma = 2

if n%2 == 0 and n>4:
    while soma < n-2:
        soma+=2
        print(soma)
elif n<=4: 
    print(f"Nenhum número par ente 2 e {n}")
else:
    while soma < (n-1):
        soma+=2
        print(soma)

"""Código sugerido pelo Perplexity:
n = int(input("Digite um número: "))

if n <= 3:
    print(f"Nenhum número par entre 2 e {n}")
else:
    for par in range(4, n, 2):   # começa em 4 (primeiro par > 2), pula de 2 em 2
        print(par)
"""