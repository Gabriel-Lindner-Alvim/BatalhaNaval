from entidade.embarcacao import Embarcacao


class PortaAviao(Embarcacao):
    def __init__(self):
        super().__init__(4, 1)
        self.__posicao = []

    @property
    def posicao(self):
        return self.__posicao

    @posicao.setter
    def posicao(self, posicao):
        self.__posicao = posicao