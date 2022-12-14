palavra_secreta = 'comida'.upper()
palavra = []
for i in range(len(palavra_secreta)):
    palavra.append('')

enforcou = False
acertou = False

print('୮' + '_' * len(palavra_secreta))

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

    acertando = 0
    for i in range(len(palavra)):
        if palavra[i] != '':
            acertando += 1
        if acertando == len(palavra_secreta):
            acertou = True

palavra_completa = ''
for i in range(len(palavra_secreta)):
    palavra_completa += palavra[i]

print(f'A palavra era {palavra_completa}')

print('Fim de jogo.')
