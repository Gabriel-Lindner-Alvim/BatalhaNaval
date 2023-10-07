class TelaPrincipal():
    def mostra_opcoes_tela(self):
        print("="*6 + " BEM-VINDO AO JOGO BATALHA NOVAL " + "="*6)
        print("1 - JOGADOR")
        print("2 - JOGO")
        opcao = int(input("O QUE VOCÊ DESEJA ACESSAR? "))
        return opcao