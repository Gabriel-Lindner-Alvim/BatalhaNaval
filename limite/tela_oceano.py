

class TelaOceano():
    def tamanho_oceano(self):
        print("\n--------TAMANHO DO OCEANO--------")
        while True:
            tamanho_matriz = int(input("Digite o tamanho do oceano: "))
            if tamanho_matriz < 6 or tamanho_matriz > 10:
                print("Tamanho inválido. Digite um tamanho entre 6 e 10.")
            else:
                print("\nOceano criado com sucesso!")
                print()
                return tamanho_matriz
    
    def posicionar_bote(self):
        print("--------POSICIONAR BOTE--------")
        print(f"Posicionar Bote (1 posição)")
        linha_bote = int(input("Digite a linha do bote: "))
        while linha_bote < 1:  #or linha_bote > len(matriz)
            linha_bote = int(input("Linha inválida. Tente Novamente"))

        coluna_bote = int(input("Digite a coluna do bote: "))
        while coluna_bote < 1: #or colunha_bote > len(matriz)
            coluna_bote = int(input("Coluna inválida. Tente Novamente"))
        print()
        return linha_bote, coluna_bote
    
    def posicionar_submarino(self):
        print("--------POSICIONAR SUBMARINO--------")
        print(f"Posicionar Submarino (2 posições)")
        linha_proa_submarino = int(input("Digite a linha da posição inicial do submarino: "))
        while linha_proa_submarino < 1: #or linha_proa_submarino > len(matriz)
            linha_proa_submarino = int(input("Linha inválida. Tente Novamente"))

        coluna_proa_submarino = int(input("Digite a coluna da posição inicial do submarino: "))
        while coluna_proa_submarino < 1: #or coluna_proa_submarino > len(matriz)
            coluna_proa_submarino = int(input("Coluna inválida. Tente Novamente"))

        linha_popa_submarino = int(input("Digite a linha da posição final do submarino: "))
        while linha_popa_submarino < 1: #or linha_popa_submarino > len(matriz)
            linha_popa_submarino = int(input("Linha inválida. Tente Novamente"))
        
        coluna_popa_submarino = int(input("Digite a coluna da posição final do submarino: "))
        while coluna_popa_submarino < 1: #or coluna_popa_submarino > len(matriz)
            coluna_popa_submarino = int(input("Coluna inválida. Tente Novamente"))
        print()
        return linha_proa_submarino, coluna_proa_submarino, linha_popa_submarino, coluna_popa_submarino
    
    def posicionar_fragata(self):
        print("--------POSICIONAR FRAGATA--------")
        print(f"Posicionar Fragata (3 posições)")
        linha_proa_fragata = int(input("Digite a linha da posição inicial da fragata: "))
        while linha_proa_fragata < 1: #or linha_proa_fragata > len(matriz)
            linha_proa_fragata = int(input("Linha inválida. Tente Novamente"))

        coluna_proa_fragata = int(input("Digite a coluna da posição inicial da fragata: "))
        while coluna_proa_fragata < 1: #or coluna_proa_fragata > len(matriz)
            coluna_proa_fragata = int(input("Coluna inválida. Tente Novamente"))
        
        linha_popa_fragata = int(input("Digite a linha da posição final da fragata: "))
        while linha_popa_fragata < 1: #or linha_popa_fragata > len(matriz)
            linha_popa_fragata = int(input("Linha inválida. Tente Novamente"))

        coluna_popa_fragata = int(input("Digite a coluna da posição final da fragata: "))
        while coluna_popa_fragata < 1: # or coluna_popa_fragata > len(matriz)
            coluna_popa_fragata = int(input("Coluna inválida. Tente Novamente"))
        print()
        return linha_proa_fragata, coluna_proa_fragata, linha_popa_fragata, coluna_popa_fragata
    
    def posicionar_porta_avioes(self):
        print("--------POSICIONAR PORTA-AVIÕES--------")
        print(f"Posicionar Porta-Aviões (4 posições)")
        linha_proa_porta_avioes = int(input("Digite a linha da posição inicial do porta-aviões: "))
        while linha_proa_porta_avioes < 1: # or linha_proa_porta_avioes > len(matriz)
            linha_proa_porta_avioes = int(input("Linha inválida. Tente Novamente"))
        
        coluna_proa_porta_avioes = int(input("Digite a coluna da posição inicial do porta-aviões: "))
        while coluna_proa_porta_avioes < 1: # or coluna_proa_porta_avioes > len(matriz)
            coluna_proa_porta_avioes = int(input("Coluna inválida. Tente Novamente"))

        linha_popa_porta_avioes = int(input("Digite a linha da posição final do porta-aviões: "))
        while linha_popa_porta_avioes < 1: # or linha_popa_porta_avioes > len(matriz)
            linha_popa_porta_avioes = int(input("Linha inválida. Tente Novamente"))
        
        coluna_popa_porta_avioes = int(input("Digite a coluna da posição final do porta-aviões: "))
        while coluna_popa_porta_avioes < 1:
            coluna_popa_porta_avioes = int(input("Coluna inválida. Tente Novamente"))

        print()
        return linha_proa_porta_avioes, coluna_proa_porta_avioes, linha_popa_porta_avioes, coluna_popa_porta_avioes
    
    def mostra_oceano(self, matriz):
        for linha in matriz:
            print(" ".join(linha))
        print()