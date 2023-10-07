from limite.tela_principal import TelaPrincipal


class ControladorPrincipal():
    def __init__(self):
        self.__tela_principal = TelaPrincipal()
    
    def inicia(self):
        self.abre_tela()
        
    def abre_tela(self):
        opcao_escolhida = self.__tela_principal.mostra_opcoes_tela()
        print(opcao_escolhida)