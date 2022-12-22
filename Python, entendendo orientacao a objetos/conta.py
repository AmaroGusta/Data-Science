class Conta:
    def __init__(self, numero, titular, saldo, limite):
        # __init__ --> constructor, lets the class initialize the
        # object's attributes
        self.__numero = numero  # .__ = private
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        # self.limite = limite --> public

    def extrato(self):
        print(f'Extrato: {self.__saldo}')

    def deposito(self, valor_deposito):
        self.__saldo += valor_deposito

    def saque(self, valor_saque):
        autorizacao = self.__saldo + valor_saque >= self.__limite
        if autorizacao:
            print('Saque ultrapassa o limite da conta de: R$'
                  f' {self.__limite}')
        else:
            self.__saldo -= valor_saque

    def transferencia(self, destino, valor):
        self.saque(valor)
        destino.deposito(valor)

    def dados(self):
        dados = {'numero': self.__numero, 'titular': self.__titular,
                 'saldo': self.__saldo,
                 'limite': self.__limite}
        return dados

    def get_numero(self):
        return self.__numero

    """ OR:
    @property
    def numero(self):
        return self.__numero
    """
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    # it works only when it's defined as a property before
    def limite(self, novo_limite):
        self.__limite = novo_limite

    """def set_limite(self, novo_limite):
        self.__limite = novo_limite
    """
# this process of privating the attributes is called encapsulation
