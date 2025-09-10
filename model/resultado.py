class Resultado:
    def __init__(self, equipe, prova, pontuacao):
        self.equipe = equipe
        self.prova = prova
        self.pontuacao = pontuacao

    def __repr__(self):
        return f"{self.equipe} - {self.prova}: {self.pontuacao}"


class ResultadoRepository:
    def __init__(self):
        self.resultados = []

    def adicionar_resultado(self, equipe, prova, pontuacao):
        resultado = Resultado(equipe, prova, pontuacao)
        self.resultados.append(resultado)
        return resultado

    def listar_resultados(self):
        return self.resultados
