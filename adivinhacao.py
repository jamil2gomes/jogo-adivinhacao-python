print("********************************")
print("Bem vindo ao jogo de adivinhação!")
print("********************************")

numero_secreto = 42

total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {:02d} de {:02d}".format(rodada, total_de_tentativas))  # string interpolation e formatação de string

    chute_str = input("Digite o seu número: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("Valor inválido. Números devem estar entre 1 e 100!")
        continue  # skip o laço

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Parabéns! Você acertou!")
        break  # sai do laço
    else:
        if (maior):
            print("O seu chute foi maior do que o número secreto!")
        elif (menor):
            print("O seu chute foi menor do que o número secreto!")

print("Fim do jogo")
