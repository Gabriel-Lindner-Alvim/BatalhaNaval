from entidade.Jogo import Jogo
from limite.tela_jogo import TelaJogo
from controle.controlador_oceano import ControladorOceano


class ControladorJogo():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_jogo = TelaJogo()
        self.__controlador_oceano = ControladorOceano(self)
        self.__historico_partida = ["Histórico:"]

    def partida(self):
        try:
            self.__controlador_oceano.criar_oceano_jogador()
        except:
            self.__tela_jogo.mostra_mensagem("Problema na criação oceano jogador. Tente Novamente")
        try:
            self.__controlador_oceano.criar_oceano_computador()
        except IndexError:
            self.__tela_jogo.mostra_mensagem("Impossível criar oceano computador. Tente Novamente")
        self.__tela_jogo.mostra_mensagem("------PARTIDA INICIADA------")
        rodada = 0
        while True:
            rodada += 1
            self.__tela_jogo.mostra_mensagem(f"RODADA {rodada}")
            tamanho = self.__controlador_oceano.mostra_tamanho()
            linha_tiro, coluna_tiro = self.__tela_jogo.obter_posicao(tamanho)
            self.__historico_partida.append(f"{linha_tiro}/{coluna_tiro}")
            if rodada > 1:
                self.__tela_jogo.mostra_mensagem(self.__historico_partida)
            tiro = self.__controlador_oceano.atirar(linha_tiro, coluna_tiro)
            self.__tela_jogo.mostra_mensagem(tiro)
            self.__controlador_oceano.mostra_oceano_jogador()
            self.__controlador_oceano.mostra_oceano_computador()


    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela_jogo(self):
        opcoes = {1: self.partida, 0: self.retornar}
        continua = True       
        while continua:
            opcoes[self.__tela_jogo.opcoes_tela()]()