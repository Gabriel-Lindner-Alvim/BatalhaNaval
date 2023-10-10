from controle.controlador_jogador import ControladorJogador

class TelaJogador():
    def tela_opcoes(self):
        print("--------CADASTRO DO JOGADOR--------")
        print("ESCOLHA A OPÇÃO DESEJADA")
        print("1 - Incluir Jogador")
        print("2 - Alterar Dados do Jogador")
        print("3 - Listar Todos os Jogadores")
        print("4 - Excluir Jogador")
        print("0 - Retornar")

        opcao = int(input("Escolha sua opção: "))
        return opcao
    

    def atribui_dados_jogador(self):
        print("--------CADASTRO JOGADOR--------")
        jogador = input("Nome do Jogador: ")
        data = input("Data de Nascimento do Jogador (Formato DDMMAAAA): ")
        
        return {"jogador": jogador, "data": data}
    
    def mostra_jogador(self):
        print("--------LISTA DE JOGADORES--------")
        for jogador in ControladorJogador.jogadores:
            print(jogador)