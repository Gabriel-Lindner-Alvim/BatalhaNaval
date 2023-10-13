from limite.tela_oceano import TelaOceano
from entidade.oceano import Oceano



class ControladorOceano():
    def __init__(self, controlador_jogo):
        self.__tela_oceano = TelaOceano()
        self.__controlador_jogo = controlador_jogo

    def inserir_tamanho_oceano(self):
        tamanho = self.__tela_oceano.tamanho_oceano() + 1
        matriz = [['^' for c in range(tamanho)] for l in range(tamanho)]
        oceano = Oceano(tamanho, matriz)
        lista = []
        for i in range(0, tamanho):
            lista.append(str(i))
        matriz[0] = lista
        for i in range(1, tamanho):
            matriz[i][0] = str(i)
        for i in range( tamanho):
            matriz[i] = '[' + ' '.join(matriz[i]) + ']'

    def posicionar_embarcacoes(self):
        self.__tela_oceano.posicionar_embarcacoes()
    
    def retornar(self):
        self.__controlador_jogo.abre_tela_jogo()

    def abre_tela_oceano(self):
        opcoes = {1: self.inserir_tamanho_oceano, 2: self.posicionar_embarcacoes, 0: self.retornar}
        continua = True    
        while continua:
            opcoes[self.__tela_oceano.opcoes_tela()]()
