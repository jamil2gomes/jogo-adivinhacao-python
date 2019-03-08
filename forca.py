import random


def gera_palavra_secreta_aleatoria():

    with open("palavras.txt") as arquivo:
        palavras = [palavra.strip() for palavra in arquivo]

    index = random.randrange(0, len(palavras))
    palavra_secreta = palavras[index]
    return palavra_secreta

def exibe_palavra_secreta(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def adiciona_palavra_no_arquivo(palavra):
    arquivo = open("palavras.txt", "a")
    arquivo.write(palavra+"\n")
    arquivo.close()

def grava_nova_palavra_no_arquivo():
    while (input("Você deseja adicionar palavras no arquivo? (S)im - (N)ão") == "s"):
        palavra = input("Digite a palavra que queira gravar no arquivo: ")
        adiciona_palavra_no_arquivo(palavra)
    else:
        exit(0)

def cabecalho():
    print("****************************")
    print("*Bem vindo ao Jogo da Forca*")
    print("****************************\n\n")

def busca_chute_na_palavra_secreta(chute, palavra_secreta, palavra_acertada):
    index = 0
    for letra in palavra_secreta:  # percorre a palavra secreta
        if letra.lower() == chute:  # e compara se o chute é igual a alguma das letras da palavra
            palavra_acertada[index] = chute  # se sim então adiciona na lista
        index += 1

def chute_digitado_pelo_usuario():
    chute = input("\nChute uma letra: ")
    chute = chute.strip().lower()  # pega a letra digitada retira os espaços em branco e coloca em minuscula
    return chute

def mensagem_vencedor():
    print("Parabéns, você descobriu a palavra secreta!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       \n\n")

def mensagem_perdedor(palavra_secreta):
    print("Que pena! Você perdeu. A palavra secreta era '{}' ".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \\       ")
    print("  /                 \\      ")
    print("//                   \\/\\  ")
    print("\\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \\__      XXX      __/     ")
    print("   |\\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \\_             _/       ")
    print("     \\_         _/         ")
    print("       \\_______/           \n\n")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogo_da_forca():
    cabecalho()
    palavra_secreta = gera_palavra_secreta_aleatoria()
    letras_secretas =  exibe_palavra_secreta(palavra_secreta)
    print(letras_secretas)

    erros = 0
    enforcou = False
    ganhou = False

    while not enforcou and not ganhou:

        chute = chute_digitado_pelo_usuario()

        if chute in palavra_secreta:
            busca_chute_na_palavra_secreta(chute, palavra_secreta, letras_secretas)
        else:
            erros += 1
            desenha_forca(erros)

        print(letras_secretas)

        if letras_secretas.count('_') == 0:  # se não houver mais espaços vazios = palavra completada
            mensagem_vencedor()
            ganhou = True

        elif erros == 7:
            mensagem_perdedor(palavra_secreta)
            enforcou = True

    grava_nova_palavra_no_arquivo()


def jogar():
    jogo_da_forca()


if (__name__ == "__main__"):  # se esse for um arquivo executavel
    jogar()
