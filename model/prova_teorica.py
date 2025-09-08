from .prova import Prova

class ProvaTeorica(Prova):
    def __init__(self, id, nome, pontuacao_maxima, numero_questoes):
        super().__init__(id, nome, pontuacao_maxima)
        self.numero_questoes = numero_questoes

    def calcular_pontuacao(self, acertos):
        return (acertos / self.numero_questoes) * self.pontuacao_maxima

