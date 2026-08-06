for cp in range(3):
    print(f"Produto{cp}")

    for i in range (1,11,1):
        print(i)

#ATIVIDADE 3
qtd_produtos = int(input("Digite a qtd. de produtos: "))

for i in range(qtd_produtos):
    print(f"Produto {i+1}")

    # LAÇOS ANINHADOS
    # ESTRUTURA DE REP. ENCADEADA

    for i in range (0,4):
        for j in range(0, 3, 2):
            print(f"i: {i}, j: {j}")