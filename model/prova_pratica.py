from .prova import Prova

class ProvaPratica(Prova):
    def __init__(self, id, nome, pontuacao_maxima, tempo_limite):
        super().__init__(id, nome, pontuacao_maxima)
        self.tempo_limite = tempo_limite

    def calcular_pontuacao(self, tempo_gasto):
        if tempo_gasto <= self.tempo_limite:
            return self.pontuacao_maxima
        else:
            return max(0, self.pontuacao_maxima - (tempo_gasto - self.tempo_limite))

