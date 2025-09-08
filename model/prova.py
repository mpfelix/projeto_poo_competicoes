from abc import ABC, abstractmethod

class Prova(ABC):
    def __init__(self, id, nome, pontuacao_maxima):
        self.id = id
        self.nome = nome
        self.pontuacao_maxima = pontuacao_maxima

    @abstractmethod
    def calcular_pontuacao(self, *args):
        pass

