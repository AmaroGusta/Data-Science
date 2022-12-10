""" help(print)
    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.
"""

print('Hello,', 'World', '!', sep=' ')  # default
# returns: Hello, World !  --> sep, means the separator between the values

print('Hello,', 'World', '!', sep='-')
# returns: Hello,-World-!

print('Hello,', 'World!', end='\n')  # default
# returns: Hello, World! --> n the continuation in the next line

print('Hello,', 'World!', end='')
# returns: Hello, World!>>> --> since there's nothing after the end of the values

# Exercício:
# Para representar uma data, temos as variáveis dia, mes e ano:
# dia = 15    mes = 10    ano = 2015
# Sem alterar as variáveis e sem passar nenhuma string adicional à função print(),
# como faríamos para ter como resultado da impressão, uma data formatada:
# 15/10/2015
# Resposta: print(dia, mes, ano, sep='/')
