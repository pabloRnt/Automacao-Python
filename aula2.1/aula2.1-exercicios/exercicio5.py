'''Determine e mostre todos os números primos no intervalo de 2 a 2000.
Dicas:
▪ Para resolver esse problema, primeiro faça um algoritmo que verifica se um número inteiro qualquer é
primo ou não.
▪ A seguir, com esse código em mãos, faça os ajustes necessários para mostrar todos os números primos
no intervalo solicitado.
▪ Você precisará colocar uma estrutura de repetição dentro da outra.'''

primos = []

def eh_primo():
    for i in range(2,2001):
        possui_divisores = False
        
        for j in range(2, int(i**(1/2))+1):
            
            if not(i%j):
                possui_divisores = True
                break
        
        if not possui_divisores:
            primos.append(i)
                    
    return primos
    
print(eh_primo())