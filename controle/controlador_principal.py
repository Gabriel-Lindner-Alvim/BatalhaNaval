from limite.tela_principal import TelaPrincipal
from controle.controlador_jogador import ControladorJogador 
from controle.controlador_jogo import ControladorJogo


class ControladorPrincipal():
    def __init__(self):
        self.__tela_principal = TelaPrincipal()
        self.__controlador_jogador = ControladorJogador(self)
        self.__controlador_jogo = ControladorJogo(self)
    
    def inicia(self):
        self.abre_tela()

    def abre_jogador(self):
        self.__controlador_jogador.abre_tela_jogador()
    
    def abre_jogo(self):
        if self.__controlador_jogador.verifica_se_existe_jogador() == True:
            self.__controlador_jogo.partida()
        else:
            pass

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.abre_jogador, 2: self.abre_jogo, 0: self.encerra_sistema}
        while True:
            opcao_escolhida = self.__tela_principal.mostra_opcoes_tela()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
        