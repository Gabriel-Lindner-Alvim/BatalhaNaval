from limite.tela_oceano import TelaOceano
from entidade.oceano import Oceano
from entidade.embarcacao import Embarcacao
from entidade.bote import Bote
from entidade.submarino import Submarino
from entidade.fragata import Fragata
from entidade.porta_avioes import PortaAviao
import random


class ControladorOceano():
    def __init__(self, controlador_jogo):
        self.__tela_oceano = TelaOceano()
        self.__oceanos_jogador = []
        self.__oceanos_computador = []
        self.__tamanho = None
        self.__pontos = 0
        self.__pontos_comp = 0
        self.__embarcacoes = []
        self.__embarcacoes_comp = []

    def criar_oceano_jogador(self):
        tamanho = self.__tela_oceano.tamanho_oceano() + 1
        self.__tamanho = tamanho
        matriz = [['^' for c in range(tamanho)] for l in range(tamanho)]
        lista = []
        for i in range(0, tamanho):
            lista.append(str(i))
        matriz[0] = lista
        for i in range(1, tamanho):
            matriz[i][0] = str(i)
        self.__oceanos_jogador.append(matriz)
        
        for i in range(1, 4):
            while True:
                aux4 = 0
                linha_bote, coluna_bote = self.__tela_oceano.posicionar_bote()
                for matriz in self.__oceanos_jogador:
                    if matriz[linha_bote][coluna_bote] == '^':
                        matriz[linha_bote][coluna_bote] = 'B'
                        self.mostra_oceano_jogador()
                        bote = Bote()
                        bote.posicao = [[linha_bote, coluna_bote]]
                        self.__embarcacoes.append(bote)
                        aux4 = 1
                    else:
                        self.__tela_oceano.mostra_mensagem("Posição inválida. Tente novamente: ")
                if aux4 == 1:
                    break
    
        for i in range(1, 3):
            while True:
                aux = 0
                linha_proa_submarino, coluna_proa_submarino, linha_popa_submarino, coluna_popa_submarino = self.__tela_oceano.posicionar_submarino()
                for matriz in self.__oceanos_jogador:
                    if matriz[linha_proa_submarino][coluna_proa_submarino] == '^' and matriz[linha_popa_submarino][coluna_popa_submarino] == '^':
                        soma_linhas = abs(linha_proa_submarino - linha_popa_submarino)
                        soma_colunas = abs(coluna_proa_submarino - coluna_popa_submarino)
                        if (soma_linhas == 0 and soma_colunas == 1) or (soma_linhas == 1 and soma_colunas == 0):
                            matriz[linha_proa_submarino][coluna_proa_submarino] = 'S'
                            matriz[linha_popa_submarino][coluna_popa_submarino] = 'S'
                            submarino = Submarino()
                            submarino.posicao = [[linha_proa_submarino, coluna_proa_submarino],
                                                 [linha_popa_submarino, coluna_popa_submarino]]
                            self.__embarcacoes.append(submarino)
                            aux = 1
                            self.mostra_oceano_jogador()
                            self.__tela_oceano.mostra_mensagem("")
                        else:
                            self.__tela_oceano.mostra_mensagem("As posições inseridas não são vizinhas. Tente novamente.")
                    else:
                        self.__tela_oceano.mostra_mensagem("Alguma(s) posição(ões) inválida(s). Tente novamente.")
                if aux == 1:
                    break
                        
    
        for i in range(1,3):
            while True:
                aux2 = 0
                linha_proa_fragata, coluna_proa_fragata, linha_popa_fragata, coluna_popa_fragata = self.__tela_oceano.posicionar_fragata()
                for matriz in self.__oceanos_jogador:
                    if matriz[linha_proa_fragata][coluna_proa_fragata] == '^' and matriz[linha_popa_fragata][coluna_popa_fragata] == '^':
                        if linha_proa_fragata == linha_popa_fragata:
                            subtrai_coluna_inicial_final = abs(coluna_proa_fragata - coluna_popa_fragata)
                            if subtrai_coluna_inicial_final == 2:
                                if coluna_proa_fragata>coluna_popa_fragata:
                                    maior = coluna_proa_fragata
                                else:
                                    maior = coluna_popa_fragata
                                if matriz[linha_proa_fragata][maior-1] == '^':
                                    matriz[linha_proa_fragata][coluna_proa_fragata] = 'F'
                                    matriz[linha_proa_fragata][maior-1] = 'F'
                                    matriz[linha_popa_fragata][coluna_popa_fragata] = 'F'
                                    fragata = Fragata()
                                    fragata.posicao = [[linha_proa_fragata, coluna_proa_fragata],
                                                       [linha_proa_fragata, maior-1],
                                                       [linha_popa_fragata, coluna_popa_fragata]]
                                    self.__embarcacoes.append(fragata)
                                    self.mostra_oceano_jogador()
                                    self.__tela_oceano.mostra_mensagem("")
                                    aux2 = 1 
                        else:
                            subtrai_linha_inicial_final = abs(linha_proa_fragata-linha_popa_fragata)
                            if subtrai_linha_inicial_final == 2:
                                if linha_proa_fragata>linha_popa_fragata:
                                    maior = linha_proa_fragata
                                else:
                                    maior = linha_popa_fragata
                                if matriz[maior-1][coluna_proa_fragata] == '^':
                                    matriz[linha_proa_fragata][coluna_proa_fragata] = 'F'
                                    matriz[maior-1][coluna_proa_fragata] = 'F'
                                    matriz[linha_popa_fragata][coluna_popa_fragata] = 'F'
                                    fragata = Fragata()
                                    fragata.posicao = [[linha_proa_fragata, coluna_proa_fragata],
                                                       [maior-1, coluna_proa_fragata],
                                                       [linha_popa_fragata, coluna_popa_fragata]]
                                    self.__embarcacoes.append(fragata)
                                    self.mostra_oceano_jogador()
                                    self.__tela_oceano.mostra_mensagem("")
                                    aux2 = 1
                    else:
                        self.__tela_oceano.mostra_mensagem("Posição inicial, final ou ambas indisponíveis. Tente novamente: ")
                if aux2 == 1:
                    break

    
        for i in range(1,2):
            while True:
                aux3 = 0
                linha_proa_porta_avioes, coluna_proa_porta_avioes, linha_popa_porta_avioes, coluna_popa_porta_avioes = self.__tela_oceano.posicionar_porta_avioes()
                for matriz in self.__oceanos_jogador:
                    if matriz[linha_proa_porta_avioes][coluna_proa_porta_avioes] == '^' and matriz[linha_popa_porta_avioes][coluna_popa_porta_avioes] == '^':
                        if linha_proa_porta_avioes == linha_popa_porta_avioes:
                            subtrai_coluna_inicial_f = abs(coluna_proa_porta_avioes - coluna_popa_porta_avioes)
                            if subtrai_coluna_inicial_f == 3:
                                if coluna_proa_porta_avioes > coluna_popa_porta_avioes:
                                    maiorzao = coluna_proa_porta_avioes
                                else:
                                    maiorzao = coluna_popa_porta_avioes
                                if matriz[linha_proa_porta_avioes][maiorzao-1] == '^' and matriz[linha_proa_porta_avioes][maiorzao-2] == '^':
                                    matriz[linha_proa_porta_avioes][coluna_proa_porta_avioes] = 'A'
                                    matriz[linha_proa_porta_avioes][maiorzao-1] = 'A'
                                    matriz[linha_proa_porta_avioes][maiorzao-2] = 'A'
                                    matriz[linha_popa_porta_avioes][coluna_popa_porta_avioes] = 'A'
                                    porta_aviao = PortaAviao()
                                    porta_aviao.posicao = [[linha_proa_porta_avioes, coluna_proa_porta_avioes],
                                                            [linha_proa_porta_avioes, maiorzao-1],
                                                            [linha_proa_porta_avioes, maiorzao-2],
                                                            [linha_popa_porta_avioes, coluna_popa_porta_avioes]]
                                    self.__embarcacoes.append(porta_aviao)
                                    self.mostra_oceano_jogador()
                                    self.__tela_oceano.mostra_mensagem("")
                                    aux3 = 1
                        else:
                            subtrai_linha_inicial_f = abs(linha_proa_porta_avioes - linha_popa_porta_avioes)
                            if subtrai_linha_inicial_f == 3:
                                if linha_proa_porta_avioes > linha_popa_porta_avioes:
                                    maiorzao = linha_proa_porta_avioes
                                else:
                                    maiorzao = linha_popa_porta_avioes
                                if matriz[maiorzao-1][coluna_proa_porta_avioes] == '^' and matriz[maiorzao-2][coluna_proa_porta_avioes] == '^':
                                    matriz[linha_proa_porta_avioes][coluna_proa_porta_avioes] = 'A'
                                    matriz[maiorzao-1][coluna_proa_porta_avioes] = 'A'
                                    matriz[maiorzao-2][coluna_proa_porta_avioes] = 'A'
                                    matriz[linha_popa_porta_avioes][coluna_popa_porta_avioes] = 'A'
                                    porta_aviao = PortaAviao()
                                    porta_aviao.posicao = [[linha_proa_porta_avioes, coluna_proa_porta_avioes],
                                                            [maiorzao-1, coluna_proa_porta_avioes],
                                                            [maiorzao-2, coluna_proa_porta_avioes],
                                                            [linha_popa_porta_avioes, coluna_popa_porta_avioes]]
                                    self.__embarcacoes.append(porta_aviao)
                                    self.mostra_oceano_jogador()
                                    self.__tela_oceano.mostra_mensagem("")
                                    aux3 = 1
                    else:
                        self.__tela_oceano.mostra_mensagem("Posição inicial, final ou ambas indisponíveis. Tente novamente: ")
                if aux3 == 1:
                    break
        oceano = Oceano(tamanho, matriz)
    
    def criar_oceano_computador(self):
        matriz_comp = [['^' for c in range(self.__tamanho)] for l in range(self.__tamanho)]
        lista = []
        for i in range(0, self.__tamanho):
            lista.append(str(i))
        matriz_comp[0] = lista
        for i in range(1, self.__tamanho):
            matriz_comp[i][0] = str(i)
        self.__oceanos_computador.append(matriz_comp)
        for i in range(1, 4): #Bote
            aux_comp1 = 0
            while True:
                num_lb = self.numero_aleatorio_bote()
                num_cb = self.numero_aleatorio_bote()
                if matriz_comp[num_lb][num_cb] == '^':
                    matriz_comp[num_lb][num_cb] = 'B'
                    bote_comp = Bote()
                    bote_comp.posicao = [[num_lb, num_cb]]
                    self.__embarcacoes_comp.append(bote_comp)
                    aux_comp1 = 1
                if aux_comp1 == 1:
                    break

        for i in range(1,3): #Submarino
            aux_comp2 = 0
            while True:
                listax = []
                num_ls = self.numero_aleatorio_submarino_linha()
                num_cs = self.numero_aleatorio_submarino_coluna()
                if matriz_comp[num_ls][num_cs] == '^':
                    if matriz_comp[num_ls][num_cs + 1] == '^':
                        listax.append(1)
                    if matriz_comp[num_ls - 1][num_cs] == '^':
                        listax.append(2)
                    escolha = random.choice(listax)
                    if escolha == 1:
                        matriz_comp[num_ls][num_cs] = 'S'
                        matriz_comp[num_ls][num_cs + 1] = 'S'
                        submarino_comp = Submarino()
                        submarino_comp.posicao = [[num_ls, num_cs],[num_ls, num_cs +1]]
                        self.__embarcacoes_comp.append(submarino_comp)
                        aux_comp2 = 1
                    elif escolha == 2:
                        matriz_comp[num_ls][num_cs] = 'S'
                        matriz_comp[num_ls - 1][num_cs] = 'S'
                        submarino_comp = Submarino()
                        submarino_comp.posicao = [[num_ls, num_cs],[num_ls - 1, num_cs]]
                        self.__embarcacoes_comp.append(submarino_comp)
                        aux_comp2 = 1
                if aux_comp2 == 1:
                    break
        
        for i in range(1,3): #Fragata
            while True:
                aux_comp3 = 0
                listaf = []
                num_lf = self.numero_aleatorio_fragata_linha()
                num_cf = self.numero_aleatorio_fragata_coluna()
                if matriz_comp[num_lf][num_cf] == '^':
                    if matriz_comp[num_lf][num_cf + 1] == '^' and matriz_comp[num_lf][num_cf + 2] == '^':
                        listaf.append(1)
                    if matriz_comp[num_lf - 1][num_cf] == '^' and  matriz_comp[num_lf - 2][num_cf] == '^':
                        listaf.append(2)
                    escolha = random.choice(listaf)
                    if escolha == 1:
                        matriz_comp[num_lf][num_cf] = 'F'
                        matriz_comp[num_lf][num_cf + 1] = 'F'
                        matriz_comp[num_lf][num_cf + 2] = 'F'
                        fragata_comp = Fragata()
                        fragata_comp.posicao = [[num_lf, num_cf],[num_lf, num_cf + 1],[num_lf, num_cf + 2]]
                        self.__embarcacoes_comp.append(fragata_comp)
                        aux_comp3 = 1
                    elif escolha == 2:
                        matriz_comp[num_lf][num_cf] = 'F'
                        matriz_comp[num_lf - 1][num_cf] = 'F'
                        matriz_comp[num_lf - 2][num_cf] = 'F'
                        fragata_comp = Fragata()
                        fragata_comp.posicao = [[num_lf, num_cf],[num_lf - 1, num_cf],[num_lf - 2, num_cf]]
                        self.__embarcacoes_comp.append(fragata_comp)
                        aux_comp3 = 1
                if aux_comp3 == 1:
                    break
        
        for i in range(1,2): #Porta-Aviões            
            while True:
                aux_comp4 = 0
                listap = []
                num_lp = self.numero_aleatorio_porta_aviao_linha()
                num_cp = self.numero_aleatorio_porta_aviao_coluna()
                if matriz_comp[num_lp][num_cp] == '^':
                    if matriz_comp[num_lp][num_cp + 1] == '^' and matriz_comp[num_lp][num_cp + 2] == '^' and matriz_comp[num_lp][num_cp + 3] == '^':
                        listap.append(1)
                    if matriz_comp[num_lp - 1][num_cp] == '^' and  matriz_comp[num_lp - 2][num_cp] == '^' and matriz_comp[num_lp - 3][num_cp] == '^':
                        listap.append(2)
                    escolha = random.choice(listap)
                    if escolha == 1:
                        matriz_comp[num_lp][num_cp] = 'A'
                        matriz_comp[num_lp][num_cp + 1] = 'A'
                        matriz_comp[num_lp][num_cp + 2] = 'A'
                        matriz_comp[num_lp][num_cp + 3] = 'A'
                        porta_aviao_comp = PortaAviao()
                        porta_aviao_comp.posicao = [[num_lp, num_cp],
                                                    [num_lp, num_cp + 1],
                                                    [num_lp, num_cp + 2],
                                                    [num_lp, num_cp + 3]]
                        self.__embarcacoes_comp.append(porta_aviao_comp)
                        aux_comp4 = 1
                    elif escolha == 2:
                        matriz_comp[num_lp][num_cp] = 'A'
                        matriz_comp[num_lp - 1][num_cp] = 'A'
                        matriz_comp[num_lp - 2][num_cp] = 'A'
                        matriz_comp[num_lp - 3][num_cp] = 'A'
                        porta_aviao_comp = PortaAviao()
                        porta_aviao_comp.posicao = [[num_lp, num_cp],
                                                    [num_lp - 1, num_cp],
                                                    [num_lp - 2, num_cp],
                                                    [num_lp - 3, num_cp]]
                        self.__embarcacoes_comp.append(porta_aviao_comp)
                        aux_comp4 = 1
                if aux_comp4 == 1:
                    break
        oceano_comp = Oceano(self.__tamanho, matriz_comp)

    def numero_aleatorio_bote(self):
        numero_aleatorio = random.randint(1, self.__tamanho - 1)
        return numero_aleatorio

    def numero_aleatorio_submarino_linha(self):
        numero_aleatorio = random.randint(1, self.__tamanho - 1)
        return numero_aleatorio

    def numero_aleatorio_submarino_coluna(self):
        numero_aleatorio = random.randint(1, self.__tamanho - 2)
        return numero_aleatorio


    def numero_aleatorio_fragata_linha(self):
        numero_aleatorio = random.randint(2, self.__tamanho - 1)
        return numero_aleatorio

    def numero_aleatorio_fragata_coluna(self):
        numero_aleatorio = random.randint(1, self.__tamanho - 3)
        return numero_aleatorio


    def numero_aleatorio_porta_aviao_linha(self):
        numero_aleatorio = random.randint(3,self.__tamanho - 1)
        return numero_aleatorio

    def numero_aleatorio_porta_aviao_coluna(self):
        numero_aleatorio = random.randint(1, self.__tamanho - 4)
        return numero_aleatorio

    def mostra_oceano_jogador(self):
        for matriz in self.__oceanos_jogador:
            self.__tela_oceano.mostra_oceano(matriz)

    def mostra_oceano_computador(self):
        for matriz in self.__oceanos_computador:
            self.__tela_oceano.mostra_oceano(matriz)

    def mostra_tamanho(self):
        return self.__tamanho
    
    def atirar(self, linha_tiro, coluna_tiro):
        lista_posicoes = [linha_tiro, coluna_tiro]
        for matriz in self.__oceanos_computador:
            for embarcacao in self.__embarcacoes_comp:
                for pos in embarcacao.posicao:
                    if lista_posicoes == pos and matriz[linha_tiro][coluna_tiro] == 'B':
                        matriz[linha_tiro][coluna_tiro] = 'X'
                        embarcacao.posicao.remove(pos)
                        self.__pontos += 4
                        return "Você afundou um Bote! (+4 pontos)"

                    elif lista_posicoes == pos and matriz[linha_tiro][coluna_tiro] == 'S':
                        matriz[linha_tiro][coluna_tiro] = 'X'
                        if len(embarcacao.posicao) == 1:
                            embarcacao.posicao.remove(pos)
                            self.__pontos += 4
                            return "Você afundou um Submarino! (+4 pontos)"
                        else:
                            embarcacao.posicao.remove(pos)
                            self.__pontos += 1
                            return "Você atingiu um Submarino! (+1 ponto)"

                    elif lista_posicoes == pos and matriz[linha_tiro][coluna_tiro] == 'F':
                        matriz[linha_tiro][coluna_tiro] = 'X'
                        if len(embarcacao.posicao) == 1:
                            embarcacao.posicao.remove(pos)
                            self.__pontos += 4
                            return "Você afundou uma Fragata! (+4 pontos)"
                        else:
                            embarcacao.posicao.remove(pos)
                            self.__pontos += 1
                            return "Você atingiu uma Fragata! (+1 ponto)"

                    elif lista_posicoes == pos and matriz[linha_tiro][coluna_tiro] == 'A':
                        matriz[linha_tiro][coluna_tiro] = 'X'
                        if len(embarcacao.posicao) == 1:
                            embarcacao.posicao.remove(pos)
                            self.__pontos += 4
                            return "Você afundou um Porta-Aviões! (+4 pontos)"
                        else:
                            embarcacao.posicao.remove(pos)
                            self.__pontos += 1
                            return "Você atingiu um Porta-Aviões! (+1 ponto)"

            matriz[linha_tiro][coluna_tiro] = 'X'
            return "Você não acertou embarcações!"


    def atirar_computador(self):
        linha_tiro = random.randint(1, self.__tamanho - 1)
        coluna_tiro = random.randint(1, self.__tamanho - 1)
        lista_posicoes_comp = [linha_tiro, coluna_tiro]
        for matriz in self.__oceanos_jogador:
            for embarcacao in self.__embarcacoes_comp:
                for pos in embarcacao.posicao:
                    if lista_posicoes_comp == pos and matriz[linha_tiro][coluna_tiro] == 'B':
                        matriz[linha_tiro][coluna_tiro] = 'X'
                        embarcacao.posicao.remove(pos)
                        self.__pontos_comp += 4
                        return "O computador afundou um Bote! (+4 pontos)"

                    elif lista_posicoes_comp == pos and matriz[linha_tiro][coluna_tiro] == 'S':
                        matriz[linha_tiro][coluna_tiro] = 'X'
                        if len(embarcacao.posicao) == 1:
                            embarcacao.posicao.remove(pos)
                            self.__pontos_comp += 4
                            return "O computador afundou um Submarino! (+4 pontos)"
                        else:
                            embarcacao.posicao.remove(pos)
                            self.__pontos_comp += 1
                            return "O computador atingiu um Submarino! (+1 ponto)"

                    elif lista_posicoes_comp == pos and matriz[linha_tiro][coluna_tiro] == 'F':
                        matriz[linha_tiro][coluna_tiro] = 'X'
                        if len(embarcacao.posicao) == 1:
                            embarcacao.posicao.remove(pos)
                            self.__pontos_comp += 4
                            return "O computador afundou uma Fragata! (+4 pontos)"
                        else:
                            embarcacao.posicao.remove(pos)
                            self.__pontos_comp += 1
                            return "O computador atingiu uma Fragata! (+1 ponto)"

                    elif lista_posicoes_comp == pos and matriz[linha_tiro][coluna_tiro] == 'A':
                        matriz[linha_tiro][coluna_tiro] = 'X'
                        if len(embarcacao.posicao) == 1:
                            embarcacao.posicao.remove(pos)
                            self.__pontos_comp += 4
                            return "O computador afundou um Porta-Aviões! (+4 pontos)"
                        else:
                            embarcacao.posicao.remove(pos)
                            self.__pontos_comp += 1
                            return "O computador atingiu um Porta-Aviões! (+1 ponto)"

            matriz[linha_tiro][coluna_tiro] = 'X'
            return "O computador não acertou embarcações!"
        
    def deletar_oceano_computador(self):
        self.__oceanos_computador.pop(0)
    
    def deletar_oceano_jogador(self):
        self.__oceanos_jogador.pop(0)
            
    def verificar_vitoria_jogador(self):
        for matriz in self.__oceanos_computador:
            for linha in matriz:
                for coluna in linha:
                    if coluna == 'B' or coluna == 'S' or coluna == 'F' or coluna == 'A':
                        return False
            return True

    def verificar_vitoria_computador(self):
        for matriz in self.__oceanos_jogador:
            for linha in matriz:
                for coluna in linha:
                    if coluna == 'B' or coluna == 'S' or coluna == 'F' or coluna == 'A':
                        return False
            return True