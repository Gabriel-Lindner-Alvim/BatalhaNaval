


class TelaPrincipal():
    def mostra_opcoes_tela(self):
        while True:
            try:    
                print("="*6 + " BEM-VINDO AO JOGO BATALHA NAVAL " + "="*6)
                print("1 - JOGADOR")
                print("2 - INICIAR JOGO")
                print("0 - SAIR")
                opcao = int(input("O QUE VOCÊ DESEJA ACESSAR? "))
                return opcao
            except ValueError:
                print()
                print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE.")
                print()
                pass