#Escreva um programa que dadas duas notas de 0 a 10 calcula a média aritmética entre elas.

def validar_nota(nota):
    nota_temp = nota
    while nota < 0 or nota > 10:
        print("A nota deve estar ente 0 e 10")
        nota_temp = float(input("Digite a primeira nota: "))
    return nota_temp

notaA = float(input("Digite a primeira nota: "))
notaA = validar_nota(notaA)

notaB = float(input("Digite a primeira nota: "))
notaB = validar_nota(notaB)