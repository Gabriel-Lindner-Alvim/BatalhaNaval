from limite.tela_oceano import TelaOceano
from entidade.oceano import Oceano



class ControladorOceano():
    def __init__(self, controlador_jogo):
        self.__tela_oceano = TelaOceano()
        self.__controlador_jogo = controlador_jogo
        self.__oceanos = []

    def inserir_tamanho_oceano(self):
        tamanho = self.__tela_oceano.tamanho_oceano() + 1
        matriz = [['^' for c in range(tamanho)] for l in range(tamanho)]
        lista = []
        for i in range(0, tamanho):
            lista.append(str(i))
        matriz[0] = lista
        for i in range(1, tamanho):
            matriz[i][0] = str(i)
        self.__oceanos.append(matriz)
        

    def posicao_embarcacoes(self):
        opcao = self.__tela_oceano.posicionar_embarcacoes()
        if opcao == 1:
            for i in range(1, 4):
                linha_bote, coluna_bote = self.__tela_oceano.posicionar_bote()
                for matriz in self.__oceanos:
                    if matriz[linha_bote][coluna_bote] == '^':
                        matriz[linha_bote][coluna_bote] = 'B'
        
        elif opcao == 2:
            for i in range(1, 3):
                while True:
                    linha_proa_submarino, coluna_proa_submarino, linha_popa_submarino, coluna_popa_submarino = self.__tela_oceano.posicionar_submarino()
                    for matriz in self.__oceanos:
                        if matriz[linha_proa_submarino][coluna_proa_submarino] == '^' and matriz[linha_popa_submarino][coluna_popa_submarino] == '^':
                            soma_linhas = abs(linha_proa_submarino - linha_popa_submarino)
                            soma_colunas = abs(coluna_proa_submarino - coluna_popa_submarino)
                            if (soma_linhas == 0 and soma_colunas == 1) or (soma_linhas == 1 and soma_colunas == 0):
                                matriz[linha_proa_submarino][coluna_proa_submarino] = 'S'
                                matriz[linha_popa_submarino][coluna_popa_submarino] = 'S'
                                break
                        
                        else:
                            print("Posição inválida. Tente novamente.")
                            
        elif opcao == 3:
            self.__tela_oceano.posicionar_fragata()
        
        elif opcao == 4:
            self.__tela_oceano.posicionar_porta_avioes()
        
        else:
            self.__tela_oceano.opcoes_tela()
    
    def retornar(self):
        self.__controlador_jogo.abre_tela_jogo()

    def abre_tela_oceano(self):
        opcoes = {1: self.inserir_tamanho_oceano, 2: self.posicao_embarcacoes, 0: self.retornar}
        continua = True    
        while continua:
            opcoes[self.__tela_oceano.opcoes_tela()]()
