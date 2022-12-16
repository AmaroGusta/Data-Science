arquivo = open('palavras.txt', 'w')
#  w --> writing  r --> reading  a --> append
#  the default is (r)eading

arquivo.write('banana\n')

arquivo.close()

arquivo.read()
# receives all the data on it
# but if we do it again, the output will be empty
# because it's quite like the cursor
# a alternative is to get it into a for loop

arquivo = open('palavras.txt', 'r')
for linha in arquivo:
    print(linha)

# read a line each time
arquivo.readline()

# this code is made for being sure it
# wasn't read wrongly or with some error
# and then closed, making sure the data's safe
with open("palavras.txt") as arquivo:
    for linha in arquivo:
        print(linha)

arquivo.close()
# always close it
