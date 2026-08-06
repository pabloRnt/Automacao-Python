'''Escreva um algoritmo que recebe uma lista de nomes e imprime os nomes na ordem inversa a da
leitura.
▪ A lista termina quando o usuário aperta o Enter sem que nenhum nome tenha sido digitado'''

lista_nomes = []
nome = str

while nome != "":
    nome = input("Digite um nome: ")
    lista_nomes.append(nome)
lista_nomes.pop(-1)

for i in range(1, len(lista_nomes)+1):
    print(lista_nomes[0-i])