jogar = "SIM"

while jogar.lower == "sim":
    print("Repete ou inicia o programa")
    jogar = input("Deseja jogar novamente? ")

i = 0

while i < 10:
    i += 1

    if i == 3 or i == 5:
        continue
    if i == 7:
        break

    print(f"Produto {i}")