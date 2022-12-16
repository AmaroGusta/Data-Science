from random import randint

arquivo = open('palavras.txt', 'r')
palavras = []

for linha in arquivo:
    linha = linha.strip()
    palavras.append(linha)

palavra_secreta = palavras[randint(0, len(palavras))].upper()
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
        if erros == 6:
            enforcou = True

    acertando = 0
    for i in range(len(palavra)):
        if palavra[i] != '':
            acertando += 1
        if acertando == len(palavra_secreta):
            acertou = True

palavra_completa = ''
for i in range(len(palavra_secreta)):
    palavra_completa += palavra[i]

print(f'A palavra era {palavra_secreta}\n {erros} erros')

print('Fim de jogo.')
