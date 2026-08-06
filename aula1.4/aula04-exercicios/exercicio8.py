divisores = []

n = int(input("Digite um valor natural: "))

match n % 2:
    case 0:
        for i in range(1, n + 1):
            if n % i == 0:
                divisores.append(i)
    case _:
        for i in range(1, n + 1, 2):
            if n % i == 0:
                divisores.append(i)

print(
    f"{ ', '.join(map(str, divisores[:-1]))} e {divisores[-1]}, "
    f"que são todos os divisores de {n}"
)