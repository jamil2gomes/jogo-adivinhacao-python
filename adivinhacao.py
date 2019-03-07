import random


def jogar():
    print("********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("********************************")

    numero_secreto = random.randrange(1, 101)  # gera número aleatório entre 1 a 100

    total_de_tentativas = 0
    pontos = 1000

    print("Escolha um nível: (1) Fácil  (2) Médio  (3) Difícil")
    escolha = int(input("Escolha o nível: "))

    if escolha == 1:
        total_de_tentativas = 20
    elif escolha == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print(
            "Tentativa {:02d} de {:02d}".format(rodada,
                                                total_de_tentativas))  # string interpolation e formatação de string

        chute = int(input("Digite o seu número: "))
        print("Você digitou ", chute)

        if chute < 1 or chute > 100:
            print("Valor inválido. Números devem estar entre 1 e 100!")
            continue  # skip o laço

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Parabéns! Você acertou!")
            break  # sai do laço
        else:
            if maior:
                print("O seu chute foi maior do que o número secreto!")
            elif menor:
                print("O seu chute foi menor do que o número secreto!")

            pontos -= abs(numero_secreto - chute)

    print("Fim do jogo!")
    print("Sua pontuação foi: {}".format(pontos))


if (__name__ == "__main__"): #se esse for um arquivo executavel
    jogar()
