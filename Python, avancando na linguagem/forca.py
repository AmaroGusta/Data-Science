from random import randint

# turns palavras.txt as default document, but allows using others
def definir_palavra_secreta(arquivo='palavras.txt'):
    arquivo = open(arquivo, 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    palavra_secreta = palavras[randint(0, len(palavras))].upper()
    return palavra_secreta


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


palavra_secreta = definir_palavra_secreta()

palavra = []
for i in range(len(palavra_secreta)):
    palavra.append('')

# teacher used
# palavra = ['_' for letra in palavra_secreta]
# and it worked there, but got a error here

enforcou = False
acertou = False
erros = 0

print('୮' + '_ ' * len(palavra_secreta))

while not acertou and not enforcou:
    chute = input('Chute uma letra: ').upper().strip()
    index = 0
    for letra in palavra_secreta:
        if letra == chute:
            print(f'Tem {letra} na posição {index}')
            palavra[index] = letra
            print(palavra)


        index += 1

    if palavra_secreta.find(chute) == -1:
        print('Não há essa letra na palavra')
        erros += 1
        desenha_forca(erros)
        if erros == 7:
            enforcou = True
            print('Você foi enforcado! (X_X)')

    acertando = 0
    for i in range(len(palavra)):
        if palavra[i] != '':
            acertando += 1
        if acertando == len(palavra_secreta):
            acertou = True

palavra_completa = ''
for i in range(len(palavra_secreta)):
    palavra_completa += palavra[i]

print(f'A palavra era {palavra_secreta}')

print('Fim de jogo.')
