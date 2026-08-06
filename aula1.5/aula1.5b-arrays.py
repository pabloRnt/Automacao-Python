lista_frutas = ["Banana", "Maçã", "Morango"]

#lista_frutas[0] = "Banana"
#lista_frutas[1] = "Maçã"
#lista_frutas[2] = "Morando"


print(lista_frutas)

print("Adição de elemento na lista")
lista_frutas.append("Pera")
print(lista_frutas)

print("Exibição formatada da lista")
print(f"{', '.join(lista_frutas[:-1])} e {lista_frutas[-1]}")

print("Quantidade de elementos na lista")
qtd_frutas = len(lista_frutas)
print(qtd_frutas)

# FOR indexado para PERCORRER lista

print("FOR indexado para PERCORRER lista")
for i in range(qtd_frutas):
    print(lista_frutas[i])

# FOR indexado para PERCORRER lista

for fruta in lista_frutas:
    print(f"Fruta: {fruta}")