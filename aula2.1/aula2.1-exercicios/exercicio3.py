'''Escreva um programa que dado um inteiro n positivo calcula e imprime a soma de todos os números
inteiros entre 1 e n.
▪ Valide a entrada do usuário, só aceite números positivos!!
▪ Dica: use while para a validação e for para a soma.
▪ Por exemplo, se n = 10 então deverá ser calculado:
▪ 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
▪ E a impressão final seria:
▪ A soma de 1 até 10 é: 55'''

try: 
    n = int(input("Digite o número inteiro: "))

except ValueError:
    print(f"Você digitou um texto. Digite um número!")
    
else:
    while n <= 0:
        
        print("Só são aceitos números positivos!")
        n = int(input("Digite o número inteiro: "))
        
    somatoria = lambda n: int((1+n)*n/2)

    print(f"A soma de 1 até 10 é {somatoria(n)}")