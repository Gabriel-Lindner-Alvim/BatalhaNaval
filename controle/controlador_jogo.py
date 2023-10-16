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
        while True:
            try:
                self.__controlador_oceano.criar_oceano_jogador()
                break
            except:
                self.__tela_jogo.mostra_mensagem('')
                self.__tela_jogo.mostra_mensagem("Problema na criação oceano jogador. Tente Novamente")
                pass
        while True:
            try:
                self.__controlador_oceano.criar_oceano_computador()
                break
            except IndexError:
                self.__tela_jogo.mostra_mensagem("Impossível criar oceano computador. Tentando Novamente...")
                self.__controlador_oceano.deletar_oceano_computador()
                pass
        self.__tela_jogo.mostra_mensagem("------PARTIDA INICIADA------")
        rodada = 0
        while True:
            if self.__controlador_oceano.verificar_vitoria_jogador():
                self.__tela_jogo.mostra_mensagem("------VOCÊ VENCEU!------")
                break
            elif self.__controlador_oceano.verificar_vitoria_computador():
                self.__tela_jogo.mostra_mensagem("------VOCÊ PERDEU!------")
                break
            else:
                rodada += 1
                self.__tela_jogo.mostra_mensagem(f"RODADA {rodada}")
                tamanho = self.__controlador_oceano.mostra_tamanho()
                linha_tiro, coluna_tiro = self.__tela_jogo.obter_posicao(tamanho)
                self.__historico_partida.append(f"{linha_tiro}/{coluna_tiro}")
                if rodada > 1:
                    self.__tela_jogo.mostra_mensagem(self.__historico_partida)
                tiro = self.__controlador_oceano.atirar(linha_tiro, coluna_tiro)
                self.__tela_jogo.mostra_mensagem(tiro)
                tiro_computador = self.__controlador_oceano.atirar_computador()
                self.__tela_jogo.mostra_mensagem(tiro_computador)
                self.__controlador_oceano.mostra_oceano_jogador()
                self.__controlador_oceano.mostra_oceano_computador()
