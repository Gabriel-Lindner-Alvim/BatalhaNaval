from entidade.Jogador import Jogador
from entidade.oceano import Oceano

class Jogo:
    def __init__(self, jogador: Jogador, oceano_jogador: Oceano, oceano_computador: Oceano):
        self.__jogador = jogador
        self.__oceano_jogador = oceano_jogador
        self.__oceano_computador = oceano_computador

    @property
    def jogador(self):
        return self.__jogador
        
    @jogador.setter
    def jogador(self, jogador):
        self.__jogador = jogador

    @property
    def oceano_jogador(self):
        return self.__oceano_jogador
        
    @oceano_jogador.setter
    def oceano_jogador(self, oceano_jogador):
        self.__oceano_jogador = oceano_jogador
        
    @property
    def oceano_computador(self):
        return self.__oceano_computador
    
    @oceano_computador.setter
    def oceano_computador(self, oceano_computador):
        self.__oceano_computador = oceano_computador