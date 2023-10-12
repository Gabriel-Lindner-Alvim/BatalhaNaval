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


    def pega_jogador_por_nome(self,nome):
        for j in self.__jogadores:
          if(j.nome == nome):
            return j
        return None
    

    def incluir_jogador(self):
        nome, data = self.__tela_jogador.atribui_dados_jogador()
        jogador = Jogador(nome, data)
        self.__jogadores.append(jogador)

    
    def alterar_jogador(self):
        nome_jogador = self.__tela_jogador.seleciona_jogador()
        jogador = self.pega_jogador_por_nome(nome_jogador)
        if(jogador is not None):
          name, date = self.__tela_jogador.reatribui_dados_jogador()
          jogador.nome = name
          jogador.nascimento = date
        else:
          self.__tela_jogador.mostra_mensagem("ATENÇÃO: JOGADOR INEXISTENTE")
    
    def lista_jogadores(self):
        if len(self.__jogadores) != 0:
            self.__tela_jogador.mostra_jogador(self.jogadores)
        else:
            self.__tela_jogador.mostra_mensagem("ATENÇÃO: NENHUM JOGADOR CADASTRADO")
    
    def excluir_jogador(self):
        nome_jogador = self.__tela_jogador.seleciona_jogador()
        jogador = self.pega_jogador_por_nome(nome_jogador)
        if(jogador is not None):
          self.__tela_jogador.mostra_mensagem("\nJOGADOR EXCLUÍDO COM SUCESSO")
          self.__jogadores.remove(jogador)
        else:
          self.__tela_jogador.mostra_mensagem("ATENÇÃO: JOGADOR INEXISTENTE")

    def retornar(self):
           self.__controlador_sistema.abre_tela()


    def abre_tela_jogador(self):
        lista_opcoes = {1: self.incluir_jogador, 2: self.alterar_jogador, 3: self.lista_jogadores, 4: self.excluir_jogador, 0: self.retornar} #adicionar ranking jogador/pontos, log in e excluir jogador.
        continua = True
        while continua:
            lista_opcoes[self.__tela_jogador.tela_opcoes()]()