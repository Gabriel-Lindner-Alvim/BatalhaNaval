

class TelaJogador():
    def tela_opcoes(self):
        print("\n--------TELA DO JOGADOR--------")
        print("ESCOLHA A OPÇÃO DESEJADA")
        print("1 - Incluir Jogador")
        print("2 - Alterar Dados do Jogador")
        print("3 - Listar Todos os Jogadores")
        print("4 - Excluir Jogador")
        print("0 - Retornar")

        opcao = int(input("\nEscolha sua opção: "))
        print()
        return opcao
    
    
    def atribui_dados_jogador(self):
        print("--------CADASTRO JOGADOR--------")
        jogador = input("Nome do Jogador: ")
        data = input("Data de Nascimento do Jogador (Formato DDMMAAAA): ")
        print("JOGADOR CADASTRADO COM SUCESSO!")
        return jogador, data
    
    def reatribui_dados_jogador(self):
        print("--------ALTERAÇÃO JOGADOR--------")
        jogador = input("Novo Nome do Jogador: ")
        data = input("Nova Data de Nascimento do Jogador (Formato DDMMAAAA): ")
        print("DADOS ALTERADOS COM SUCESSO!")
        return jogador, data

    def mostra_jogador(self, jogadores):
        print("--------LISTA DE JOGADORES--------")
        for jogador in jogadores:
            print(f"NOME: {jogador.nome} | DATA DE NASCIMENTO: {jogador.nascimento}")
            print()
    
    def seleciona_jogador(self):
        print("--------SELECIONE O JOGADOR--------")
        jogador = input("Nome do Jogador: ")
        return jogador

    def mostra_mensagem(self, mensagem):
        print(mensagem)
    