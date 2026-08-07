'''Faça um programa que exiba a mensagem “Olá, Mundo”.
▪ Essa mensagem deverá ser exibida repetidamente.
▪ Ao final de toda iteração da repetição, você deve perguntar ao usuário se ele deseja exibir a mensagem
novamente.
▪ Se sim, exiba novamente. Senão, saia do loop e exiba a mensagem “Fim”.'''

while True:
    print("Olá, Mundo")
    
    if input("Deseja repetir a mensagem? ") == "não":
        print("Fim")
        break