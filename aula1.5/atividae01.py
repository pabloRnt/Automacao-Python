nomes = ["Pablo", "Lucas", "Matheus", "Pedro"]
for nome in range(len(nomes)):
    for i in range(nome+1, len(nomes)):
        print(nomes[nome], nomes[i])