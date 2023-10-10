from abc import ABC, abstractmethod

class Embarcacao(ABC):
    @abstractmethod
    def __init__(self, tamanho_embarcacao: int):
        self.__tamanho_embracacao = tamanho_embarcacao

    
    @property
    def tamanho_embarcacao(self):
        return self.__tamanho_embracacao
    
    @tamanho_embarcacao.setter
    def tamanho_embarcacao(self, tamanho_embarcacao):
        self.__tamanho_embracacao = tamanho_embarcacao