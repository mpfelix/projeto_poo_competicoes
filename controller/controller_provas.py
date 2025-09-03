from model.repositories import ProvaRepository, ResultadoRepository

class ControllerProvas:

    @staticmethod
    def criar_prova(nome, tipo, pontuacao_maxima, numero_questoes=None, tempo_limite=None):
        return ProvaRepository.criar(nome, tipo, pontuacao_maxima, numero_questoes, tempo_limite)

    @staticmethod
    def listar_provas():
        return ProvaRepository.listar()

    @staticmethod
    def registrar_resultado(equipe_id, prova_id, pontuacao):
        return ResultadoRepository.registrar(equipe_id, prova_id, pontuacao)

    @staticmethod
    def listar_resultados():
        return ResultadoRepository.listar()
