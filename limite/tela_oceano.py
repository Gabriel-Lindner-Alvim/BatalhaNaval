


class TelaOceano():
    def opcoes_tela(self):
        print("--------CONFIGURAÇÕES DO OCEANO--------")
        print("ESCOLHA A OPÇÃO DESEJADA")
        print("1 - Escolher o tamanho do oceano")
        print("2 - Posicionar as embarcações")
        print("0 - Retornar")
        
        opcao = int(input("\nEscolha sua opção: "))
        print()
        return opcao
    
    def tamanho_oceano(self):
        print("--------TAMANHO DO OCEANO--------")
        while True:
            tamanho_matriz = int(input("Digite o tamanho do oceano: "))
            if tamanho_matriz < 5 or tamanho_matriz > 10:
                print("Tamanho inválido. Digite um tamanho entre 5 e 10.")
            else:
                
                print("\nOceano criado com sucesso!")
                print()
                return tamanho_matriz
                
    def posicionar_embarcacoes(self):
        print("-------POSICIONAR EMBARCAÇÕES-------")
        print("1 - Posicionar Botes")
        print("2 - Posicionar Submarinos")
        print("3 - Posicionar Fragatas")
        print("4 - Posicionar Porta-Aviões")
        print("0 - Retornar")
        
        opcao = int(input("\nEscolha sua opção: "))
        print()
        return opcao
    
    def posicionar_bote(self):
        print("--------POSICIONAR BOTE--------")
        print(f"Posicionar Bote (1 posição)")
        linha_bote = int(input("Digite a linha do bote: "))
        coluna_bote = int(input("Digite a coluna do bote: "))
        print()
        return linha_bote, coluna_bote
    
    def posicionar_submarino(self):
        print("--------POSICIONAR SUBMARINO--------")
        print(f"Posicionar Submarino (2 posições))")
        linha_proa_submarino = int(input("Digite a linha da posição inicial do submarino: "))
        coluna_proa_submarino = int(input("Digite a coluna da posição inicial do submarino: "))
        linha_popa_submarino = int(input("Digite a linha da posição final do submarino: "))
        coluna_popa_submarino = int(input("Digite a coluna da posição final do submarino: "))
        print()
        return linha_proa_submarino, coluna_proa_submarino, linha_popa_submarino, coluna_popa_submarino
    
    def posicionar_fragata(self):
        print("--------POSICIONAR FRAGATA--------")
        print(f"Posicionar Fragata (3 posições)")
        linha_proa_fragata = int(input("Digite a linha da posição inicial da fragata: "))
        coluna_proa_fragata = int(input("Digite a coluna da posição inicial da fragata: "))
        linha_popa_fragata = int(input("Digite a coluna da posição final da fragata: "))
        coluna_popa_fragata = int(input("Digite a coluna da posição final da fragata: "))
        print()
        return linha_proa_fragata, coluna_proa_fragata, linha_popa_fragata, coluna_popa_fragata
    
    def posicionar_porta_avioes(self):
        print("--------POSICIONAR PORTA-AVIÕES--------")
        print(f"Posicionar Porta-Aviões (4 posições)")
        linha_proa_porta_avioes = int(input("Digite a linha da posição inicial do porta-aviões: "))
        coluna_proa_porta_avioes = int(input("Digite a coluna da posição inicial do porta-aviões: "))
        linha_popa_porta_avioes = int(input("Digite a linha da posição final do porta-aviões: "))
        coluna_popa_porta_avioes = int(input("Digite a coluna da posição final do porta-aviões: "))

        print()
        return linha_proa_porta_avioes, coluna_proa_porta_avioes, linha_popa_porta_avioes, coluna_popa_porta_avioes