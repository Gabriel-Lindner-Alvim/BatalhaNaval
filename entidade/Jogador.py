

class Jogador:
    def __init__(self, nome: str, nascimento: str, pontos,)
        self.__nome = nome
        self.__nascimento =nascimento
        self.__pontos = pontos

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
    
    @property
    def pontos(self):
        return self.__pontos
    
    @pontos.setter
    def pontos(self, pontos):
        self.__pontos = pontos