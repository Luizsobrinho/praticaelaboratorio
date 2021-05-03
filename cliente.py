
class Cliente:
    def __init__(self,nome,telefone):
        self.__nome = nome
        self.__telefone = telefone

    #Getter
    @property
    def nome(self):
        return self.__nome
    @property
    def telefone(self):
        return self.__telefone

    #Setter
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @telefone.setter
    def telefone(self,telefone):
        self.__telefone = telefone
