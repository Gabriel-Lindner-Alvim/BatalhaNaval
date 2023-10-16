from entidade.embarcacao import Embarcacao


class Bote(Embarcacao):
    def __init__(self):
        super().__init__(1, 3)
        self.__posicao = []

    @property
    def posicao(self):
        return self.__posicao

    @posicao.setter
    def posicao(self, posicao):
        self.__posicao = posicao