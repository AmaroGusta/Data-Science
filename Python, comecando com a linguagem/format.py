# o método format() serve para interpolação de strings

print('R${}'.format(1.567))
# normal

print('R${:.2f}'.format(1.567))
# duas casas depois do ponto e o f representa o valor float

print('R${:7.2f}'.format(4.5))
# de sete caracteres, dois vão depois do ponto
    # R$   4.50

print('R${:07.2f}'.format(4.5))
# o mesmo, mas com zeros na frente

print('R${:04d}'.format(4))
# d significa decimal, ou inteiro

# f-strings, novo recurso
nome = 'gustavin'
print(f'Bem vindo, {nome}')
