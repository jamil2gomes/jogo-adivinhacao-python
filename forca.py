def jogar():
    print("**************")
    print("Jogo da Forca")
    print("**************")
    palavra_secreta = "banana"

    enforcou = False
    ganhou = False

    while not enforcou and not ganhou:
        chute = input("Chute uma letra: ")
        chute = chute.strip()  # retira os espaços em branco

        index = 0  # posição da palavra na string
        for letra in palavra_secreta:  # busca o "chute" na palavra
            if chute.upper() == letra.upper():  # transforma todas as letras em maiusculas
                print("Encontrei a letra '{}' na posição {} ".format(letra, index))
            index += 1
        print("Jogando...")


if (__name__ == "__main__"):  # se esse for um arquivo executavel
    jogar()
