from limite.tela_jogador import TelaJogador
from entidade.Jogador import Jogador

class ControladorJogador():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_jogador = TelaJogador()
        self.__jogadores = []

    
    @property
    def jogadores(self):
        return self.__jogadores
    
    @jogadores.setter
    def jogadores(self, jogadores):
        self.__jogadores = jogadores

    def incluir_jogador(self):
        dados_jogador = self.__tela_jogador.atribui_dados_jogador()
        jogador = Jogador(dados_jogador["jogador"], dados_jogador["data"])
        self.__jogadores.append(jogador)

    
    def alterar_jogador(self):
        
    
    def lista_jogadores(self):
        self.__tela_jogador.mostra_jogador()
    
    
    def excluir_jogador(self):
        


    def abre_tela_jogador(self):
        lista_opcoes = {1: self.incluir_jogador, 2: self.alterar_jogador, 3: self.lista_jogadores, 4: self.excluir_jogador, 0: self.retornar} #adicionar ranking jogador/pontos e log in.
