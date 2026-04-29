# Faça um programa capaz de exibir todos os valores pares entre 2 e um valor fornecido pelo usuário.
soma = 2
n = int(input("Digite um número natural: "))

match n%2:
    case 0:
        for i in range(2, n+1, 2):
            print(soma)
            soma+=2
    case _: 
        for i in range(2,n, 2):
            print(soma)
            soma+=2