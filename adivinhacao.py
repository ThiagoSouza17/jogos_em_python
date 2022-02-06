import random

def jogar():
    print("*********************************")
    print("Bem-vindo ao Jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_chutes = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) - Fácil, (2) - Médio, (3) - Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_chutes = 20
    elif(nivel == 2):
        total_de_chutes = 10
    else:
        total_de_chutes = 5

    for rodada in range(1, total_de_chutes + 1):
        print("Tentativa {} de {}".format(rodada, total_de_chutes))
        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou: ", chute)

        if(chute < 1 or chute >100):
            print("Você deve digitar um número entre 1 e 100!")
            continue
        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior que o número secreto!")
                if(rodada == total_de_chutes):
                    print("O número secreto era {}. Você fez {} pontos!".format(numero_secreto, pontos))
            elif(menor):
                print("Você errou! O seu chute foi menor que o número secreto!")
                if (rodada == total_de_chutes):
                    print("O número secreto era {}. Você fez {} pontos!".format(numero_secreto, pontos))
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos


    print("Fim do Jogo!")

if(__name__ == "__main__"):
    jogar()


