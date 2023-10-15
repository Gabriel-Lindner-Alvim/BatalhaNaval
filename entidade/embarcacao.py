from abc import ABC, abstractmethod


class Embarcacao(ABC):
    @abstractmethod
    def __init__(self, tamanho_embarcacao: int, quantidade_embarcacao: int):
        self.__tamanho_embracacao = tamanho_embarcacao
        self.__quantidade_embarcacao = quantidade_embarcacao

    
    @property
    def tamanho_embarcacao(self):
        return self.__tamanho_embracacao
    
    @tamanho_embarcacao.setter
    def tamanho_embarcacao(self, tamanho_embarcacao):
        self.__tamanho_embracacao = tamanho_embarcacao

    @property
    def quantidade_embarcacao(self):
        return self.__quantidade_embarcacao
    
    @quantidade_embarcacao.setter
    def quantidade_embarcacao(self, quantidade_embarcacao):
        self.__quantidade_embarcacao = quantidade_embarcacao