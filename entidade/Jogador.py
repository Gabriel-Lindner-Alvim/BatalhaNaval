


class Jogador:
    def __init__(self, nome: str, nascimento: str):
        self.__nome = nome
        self.__nascimento =nascimento

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def nascimento(self):
        return self.__nascimento
    
    @nascimento.setter
    def nascimento(self, nascimento):
        self.__nascimento = nascimento
    