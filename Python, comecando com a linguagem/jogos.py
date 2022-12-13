import adivinhacao


def escolher_jogo():
    escolha = ''

    while not escolha in [1, 2]:
        escolha = int(input('Escolha seu jogo \n(1) Adivinhação  (2) Forca\n'))
        if escolha == 1:
            print('adivinhação')
            adivinhacao.jogar()
        elif escolha == 2:
            print('forca')
        else:
            print('valor inválido')
            continue


if __name__ == '__main__':
    escolher_jogo()
