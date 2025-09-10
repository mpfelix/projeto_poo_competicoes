from model.prova import ProvaRepository

class ControllerProvas:
    def __init__(self):
        self.repo = ProvaRepository()

    def adicionar_prova_teorica(self, titulo, pontuacao_maxima, num_questoes):
        return self.repo.adicionar_prova_teorica(titulo, pontuacao_maxima, num_questoes)

    def adicionar_prova_pratica(self, titulo, pontuacao_maxima, tempo_execucao):
        return self.repo.adicionar_prova_pratica(titulo, pontuacao_maxima, tempo_execucao)

    def listar_provas(self):
        return self.repo.listar_provas()
