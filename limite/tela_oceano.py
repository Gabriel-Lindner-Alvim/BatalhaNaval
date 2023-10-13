


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
        print("-------POSICIONAR EMBARCAÇOES-------")
        print()
        for a in range (1,4):
            print(f"POSICIONANDO BOTE nº {a}: ")
            linha_bote = int(input("DIGITE A LINHA: "))
            coluna_bote = int(input("DIGITE A COLUNA: "))
            print()
        for b in range (1,3):
            print(f"POSICIONANDO SUBMARINO nº {b}: ")
            linha_submarino = int(input("DIGITE A LINHA: "))
            coluna_submarino = int(input("DIGITE A COLUNA: "))
            print()
        for c in range (1,3):
            print(f"POSICIONANDO FRAGATA nº {c}: ")
            linha_fragata = int(input("DIGITE A LINHA: "))
            coluna_fragata = int(input("DIGITE A COLUNA: "))
            print()
        for d in range (1,2):
            print(f"POSICIONANDO PORTA-AVIÕES (ÚNICO): ")
            linha_porta_aviao = int(input("DIGITE A LINHA: "))
            coluna_porta_aviao = int(input("DIGITE A COLUNA: "))
            print()
