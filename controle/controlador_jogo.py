from entidade.Jogo import Jogo
from limite.tela_jogo import TelaJogo
from controle.controlador_oceano import ControladorOceano


class ControladorJogo():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_jogo = TelaJogo()
        self.__controlador_oceano = ControladorOceano(self)

    def iniciar_jogo(self):
        pass
    
    def configuracoes_oceano(self):
        self.__controlador_oceano.abre_tela_oceano()
    

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela_jogo(self):
        opcoes = {1: self.iniciar_jogo, 2: self.configuracoes_oceano, 0: self.retornar}
        continua = True       
        while continua:
            opcoes[self.__tela_jogo.opcoes_tela()]()