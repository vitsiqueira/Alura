import FORCA
import advinhação


def escolherJogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    if jogo == 1:
        print("Jogando forca")
        print(":" * 33)
        FORCA.jogar_forca()
    elif jogo == 2:
        print("Jogando adivinhação")
        print(":" * 33)
        advinhação.jogar_advinhação()


if __name__ == "__main__":
    escolherJogo()
