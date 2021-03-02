import random  # em c o import é igual a include


def jogarAdvinhação():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numeroSecreto = random.randrange(1, 101)  # gera um número entre 1 e 100
    totalTentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil : (2) Médio : (3) Difícil")

    nivel = int(input("Defina um nível: "))

    if nivel == 1:
        totalTentativas = 20
    elif nivel == 2:
        totalTentativas = 10
    else:
        totalTentativas = 5

    # enquanto ainda há tentativas, executa o código
    for rodada in range(1, totalTentativas + 1):  # mais 1, pois ele não inclui o último número normalmente

        # range(start, stop, [step]) - o step é opcional, serve para pularmos a contagem. ex: 3 em 4

        print("Tentativa {} de {}".format(rodada, totalTentativas))  # string interpolation
        # print("Tentativa {} de {}").format(3, 10)) - normalmente ele imprime o primeiro parametro no primeiro colchetes, o segundo parametro no segundo colchetes, etc. mas eu posso mudar essa ordem, colocando o índice do (...)
        # (...) parametro no colchetes que eu quero, ex: print("Tentativa {1} de {0}").format(3, 10))
        # >>> print("R$ {:f}".format(1.59)) - isso para determirmos os números dps do ponto - {:.2f} para dois caracteres, etc - {:07.2f} para sete caracteres antes do ponto e dois depois do ponto - usamos o "f" para determinar que é float e d pra inteiro

        chute = int(input("Digite o seu número entre 1 e 100: "))
        print("Você digitou", chute)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue;

        acertou = chute == numeroSecreto
        maior = chute > numeroSecreto
        menor = chute < numeroSecreto

        if acertou:
            print("Você acertou e fez {} pontos!".format(pontos))
            break;

        else:  # else não recebe condição!!!!
            if maior:
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif menor:
                print("Você errou! O seu chute foi menor do que o número secreto.")
                pontosPerdidos = abs(numeroSecreto - chute)  # número absoluto, sem sinais
            pontos = pontos - pontosPerdidos

    print("Fim do jogo!")


if __name__ == "__main__":  # para executar o arquivo se abrirmos ele diretamente
    jogarAdvinhação()
