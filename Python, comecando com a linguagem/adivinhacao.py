from random import randint  # conhecimento prévio

i = False

while not i:
    dificuldade = int(input('Dificuldades:\n(1) Fácil  (2) Médio  (3) Difícil\n'))
    if dificuldade == 1:
        n = randint(1, 10)
        tentativas = 3
        print('Você tem {} tentativas'.format(tentativas))
        i = True
    elif dificuldade == 2:
        n = randint(1, 50)
        tentativas = 5
        print('Você tem {} tentativas'.format(tentativas))
        i = True
    elif dificuldade == 3:
        n = randint(1, 100)
        tentativas = 10
        print('Você tem {} tentativas'.format(tentativas))
        i = True
    else:
        print('Valor inválido')
        continue

while tentativas != 0:
    chute = int(input('Jogue: '))

    if dificuldade == 1:
        if chute > 10 or chute < 0:
            print('O valor jogado deve estar entre 1 e 10!')
            continue  # volta à iteração inicial, ignorando os comandos posteriores
    elif dificuldade == 2:
        if chute > 50 or chute < 0:
            print('O valor jogado deve estar entre 1 e 50!')
            continue  # volta à iteração inicial, ignorando os comandos posteriores
    else:
        if chute > 100 or chute < 0:
            print('O valor jogado deve estar entre 1 e 100!')
            continue  # volta à iteração inicial, ignorando os comandos posteriores

    tentativas -= 1
    maior = chute > n
    menor = chute < n
    diferente = chute != n

    if diferente:
        if maior:
            print('Um número mais baixo', '\n{} tentativas'.format(tentativas))
            # .format() string placeholder
        else:
            print('Um número mais alto', '\n{} tentativas'.format(tentativas))
    else:
        print('acertou!')
        break
