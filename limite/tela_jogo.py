

class TelaJogo():
    def obter_posicao(self, tamanho):
        while True:
            try:
                linha_tiro = int(input("Digite a linha do tiro: "))
                coluna_tiro = int(input("Digite a coluna do tiro: "))
                print()
                if 0 <= linha_tiro <= tamanho and 0 <= coluna_tiro <= tamanho:
                    return linha_tiro, coluna_tiro
                else:
                    print("Coordenadas inválidas. Tente novamente.")
            except:
                print("Coordenadas inválidas. Tente novamente.")
    
    def mostra_mensagem(self, mensagem):
        print(mensagem)
        print()