import math

def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Agora percorre de 2 até 2000 e testa cada número
for num in range(2, 2001):
    if eh_primo(num):
        print(num, end=", ")   # mostra todos os primos na mesma linha