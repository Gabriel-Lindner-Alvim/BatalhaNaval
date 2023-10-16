


class Oceano():
    def __init__(self, tamanho_matriz: int, matriz: list):
        self.__tamanho_matriz = tamanho_matriz
        self.__matriz = matriz
    
    @property
    def tamanho_matriz(self):
        return self.__tamanho_matriz
    
    @tamanho_matriz.setter
    def tamanho_matriz(self, tamanho_matriz):
        self.__tamanho_matriz = tamanho_matriz
    
    @property
    def matriz(self):
        return self.__matriz
    
    @matriz.setter
    def matriz(self, matriz):
        self.__matriz = matriz