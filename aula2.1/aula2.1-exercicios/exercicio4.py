'''Escreva um algoritmo que recebe um inteiro positivo n e imprime todos os divisores positivos de n.
▪ Utilize o laço for.
▪ Exemplo:
Suponha que n = 28, nessa situação devemos imprimir os números
1, 2, 4, 7, 14 e 28, que são todos os divisores do 28.
▪ Dica: para o número ser divisor de n, a divisão precisa ter resto nulo.
'''

n = int(input("Digite um número natural: "))

divisores = [i for i in range(1,int((n/2))+1) if not(n%i)]
divisores.append(n)
divisores_string = list(map(lambda x: str(x), divisores))

print(f"{', '.join(divisores_string[:-1])} e {divisores_string[-1]} são todos os divisores de {n}")