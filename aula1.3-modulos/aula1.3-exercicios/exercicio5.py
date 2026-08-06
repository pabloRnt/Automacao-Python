maiorNumero = 0
cont = 1

while cont <= 5:
    n = int(input(f"Digite o {cont}º número: "))
    if cont == 1 or n > maiorNumero:
        maiorNumero = n
    cont += 1

print(maiorNumero)