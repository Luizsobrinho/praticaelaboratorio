from cliente import Cliente
class Conta:

    def __init__(self, numero,saldo,cliente):
        self.__numero = numero
        self.__saldo = saldo
        self.__limite = 1000
        self.__extrato = []
        self.__cliente = cliente

    @property
    def cliente(self):
        return self.__cliente

    # Setter
    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def extrato(self):
        return self.__extrato;

    def depositar(self,valor):
        if valor > 0:
            self.__saldo += valor
            extrato = Extrato('DEPOSITO', valor)
            self.__extrato.append(extrato)

    def sacar(self,valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            extrato = Extrato('SAQUE',valor)
            self.__extrato.append(extrato)
        if self.__saldo + self.__limite >= valor:
            self.__saldo -= valor
            extrato = Extrato('SAQUE', valor)
            self.__extrato.append(extrato)
        else:
            print(f'Saldo da conta: {self.__numero}  insuficiente, seu saldo é : {self.__saldo}')

    def listarExtrato(self):
        print(f'EXTRATO CC NO. : {self.__numero} do cliente {self.__cliente.nome}')
        print()
        for lista in self.__extrato:
            print(f'{lista.tipo} : {lista.valor}')
        print()
        print(f'SALDO: {self.__saldo}')
        print()
        print(f'LIMITE: {self.__limite}')
        print()
        print(f'DISPONIVEL: {self.__limite + self.__saldo}')

class Extrato:
    def __init__(self,tipo,valor):
        self.__tipo = tipo
        self.__valor = valor

    #Getter
    @property
    def tipo(self):
        return self.__tipo;

    @property
    def valor(self):
        return self.__valor;

    #Setter
    @tipo.setter
    def nome(self, tipo):
        self.__tipo = tipo

    @valor.setter
    def telefone(self,valor):
        self.__valor = valor