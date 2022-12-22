class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property
    # turn the method into a property
    # it's a GET without the get name
    def nome(self):
        return self.__nome.title()
    # in the console, keeps the syntax:
    # cliente.nome

    @nome.setter
    # setting without the SET name
    def nome(self, nome):
        print('setting')
        self.__nome = nome
