from entidade.embarcacao import Embarcacao


class Fragata(Embarcacao):
    def __init__(self):
        super().__init__(3, 2)
        self.__posicao = []

    @property
    def posicao(self):
        return self.__posicao

    @posicao.setter
    def posicao(self, posicao):
        self.__posicao = posicao