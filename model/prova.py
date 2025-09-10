class Prova:
    def __init__(self, titulo, pontuacao_maxima):
        self.titulo = titulo
        self.pontuacao_maxima = pontuacao_maxima


class ProvaTeorica(Prova):
    def __init__(self, titulo, pontuacao_maxima, num_questoes):
        super().__init__(titulo, pontuacao_maxima)
        self.num_questoes = num_questoes


class ProvaPratica(Prova):
    def __init__(self, titulo, pontuacao_maxima, tempo_execucao):
        super().__init__(titulo, pontuacao_maxima)
        self.tempo_execucao = tempo_execucao


class ProvaRepository:
    def __init__(self):
        self.provas = []

    def adicionar_prova_teorica(self, titulo, pontuacao_maxima, num_questoes):
        prova = ProvaTeorica(titulo, pontuacao_maxima, num_questoes)
        self.provas.append(prova)
        return prova

    def adicionar_prova_pratica(self, titulo, pontuacao_maxima, tempo_execucao):
        prova = ProvaPratica(titulo, pontuacao_maxima, tempo_execucao)
        self.provas.append(prova)
        return prova

    def listar_provas(self):
        return self.provas
