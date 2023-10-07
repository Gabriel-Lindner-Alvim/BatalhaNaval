from limite.tela_principal import TelaPrincipal


class ControladorPrincipal():
    def __init__(self):
        self.__tela_principal = TelaPrincipal()
    
    def inicia(self):
        self.abre_tela()

    def abre_jogador(self):
        
    
    def abre_jogo(self):


    def encerra_sistema(self):
        exit(0)
        
    def abre_tela(self):
        lista_opcoes = {1: self.abre_jogador, 2: self.abre_jogo, 0: self.encerra_sistema}
        opcao_escolhida = self.__tela_principal.mostra_opcoes_tela()
        