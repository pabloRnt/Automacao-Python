# Determine e mostre todos os números primos no intervalo de 2 a 2000
lista_primos = []

for i in range(2, 2000):
    eh_primo = True
    for j in range(2, (int(i**0.5) +1)):  
        if i % j == 0:
            eh_primo = False
            break           
    if eh_primo:
        lista_primos.append(i)

print(f"{', '.join(map(str, lista_primos[:-1]))} e {lista_primos[-1]} são primos")