# tupla é uma lista que não se pode mudar e são feitas com parenteses, em vez das listas que são feitas com colchetes []

import random


def jogar_forca():

    imprime_ma()

    palavraSecreta = carrega_palavra_secreta()

    letrasAcertadas = inicializa_letras_acertadas(palavraSecreta)
    print(letrasAcertadas)

    Enforcou = False
    Acertou = False
    erros = 0


    # enquanto(True) continue executando
    while not Enforcou and not Acertou:
        # find = função em que podemos procurar algo dentro da string, ele fala a PRIMEIRA OCORRÊNCIA do texto que estamos procurando, se n existe ele retorna -1

        chute = pede_chute()

        if chute in palavraSecreta:

            marca_chute_correto(chute, letrasAcertadas, palavraSecreta)

        else:
            erros += 1
            desenha_forca(erros)

        Enforcou == erros == 7
        Acertou = "_" not in letrasAcertadas
        print(letrasAcertadas)

    if Acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavraSecreta)


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


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavraSecreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavraSecreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def marca_chute_correto(chute, letrasAcertadas, palavraSecreta):
    index = 0
    for letra in palavraSecreta:
        if chute == letra:
            letrasAcertadas[index] = letra
        index += 1


def pede_chute():
        chute = input("Qual letra? ")
        chute = chute.strip().upper()
        return chute


def imprime_ma():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavraSecreta = palavras[numero].upper()
    return palavraSecreta


def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

if __name__ == "__main__":
    jogar_forca()