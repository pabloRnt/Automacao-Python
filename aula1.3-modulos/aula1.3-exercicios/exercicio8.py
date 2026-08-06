#Exercício 8
n = int(input("Digite um número inteiro e positivo: "))
numero_de_Divisores = 0
ordem_Divisor = 0
texto_Divisores = "1"

for divisor in range(2,n+1):
    if n%divisor == 0:
        numero_de_Divisores+=1
    else:
        continue

for divisor in range(2,n+1):
    if n%divisor == 0 and ordem_Divisor < numero_de_Divisores-1:
        texto_Divisores += ", " + str(divisor)
        ordem_Divisor += 1
    elif n%divisor == 0 and ordem_Divisor == numero_de_Divisores-1:
        texto_Divisores += " e " + str(divisor)
        ordem_Divisor += 1
    else:
        continue
print(f"{texto_Divisores} são todos os divisores de {n}")