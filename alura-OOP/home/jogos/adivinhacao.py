print('******************************')
print('*    Jogo da adivinhação     *')
print('******************************')

numero_secreto = 42
pontos = 1000

nivel = int(input("Escolha o nível do jogo, de 1 a 3: "))

if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
elif nivel == 3:
    total_de_tentativas = 5
else:
    print("Nível inválido!")


for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}.".format(rodada, total_de_tentativas))
    chute = int(input("Digite o seu número: "))
    print("Você digitou: ", chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
        break
    elif (maior):
        pontos = pontos - abs(chute - numero_secreto)
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif (menor):
        pontos = pontos - abs(chute - numero_secreto)
        print("Você errou! O seu chute foi menor que o número secreto.")
    if (pontos >= 0):
        print(f"Total de pontos: {pontos}")
    else:
        break


print("Fim do jogo")