class Conta:
    cd_bancos = {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

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

    def __autorizacao(self, valor_a_sacar):
        valor_disponivel_saque = self.__limite + self.__saldo
        return valor_disponivel_saque > valor_a_sacar
    # private method

    def saque(self, valor_saque):
        # autorizacao = valor_saque < self.__saldo + self.__limite
        if self.__autorizacao(valor_saque):
            self.__saldo -= valor_saque
        else:
            print('Saque ultrapassa o limite da conta de: R$'
                  f' {self.__limite}')

    def transferencia(self, destino, valor):
        if self.__autorizacao(valor):
            self.saque(valor)
            destino.deposito(valor)
        else:
            print('Transferência não autorizada.')

    def dados(self):
        dados = {'numero': self.__numero, 'titular': self.__titular,
                 'saldo': self.__saldo,
                 'limite': self.__limite}
        return dados

    def get_numero(self):
        return self.__numero

    """ OR (fancier):
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

    @staticmethod
    # it's the class' properties, since doesn't need an object to
    # be called: Conta.codigos_bancos() -> works
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
    # this could also be done by creating an attribute just after
    # creating the class itself, as in line 2
