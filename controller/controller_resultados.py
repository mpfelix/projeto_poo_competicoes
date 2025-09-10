from model.resultado import ResultadoRepository

class ControllerResultados:
    def __init__(self):
        self.repo = ResultadoRepository()

    def adicionar_resultado(self, equipe, prova, pontuacao):
        return self.repo.adicionar_resultado(equipe, prova, pontuacao)

    def listar_resultados(self):
        return self.repo.listar_resultados()
