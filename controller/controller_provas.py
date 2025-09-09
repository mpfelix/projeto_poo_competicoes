from model.repositories import ProvaRepository, ResultadoRepository

class ControllerProvas:
    def __init__(self):
        # aqui vamos armazenar as provas cadastradas em memória (lista simples)
        self.provas = []

    def cadastrar_prova(self, nome, tipo, pontos):
        """
        Cadastra uma nova prova no sistema
        :param nome: Nome da prova (str)
        :param tipo: Tipo da prova (str)
        :param pontos: Pontos da prova (int ou float)
        """
        prova = {
            "nome": nome,
            "tipo": tipo,
            "pontos": pontos
        }

        self.provas.append(prova)
        print(f"✅ Prova cadastrada: {prova}")
        return prova

    def listar_provas(self):
        """
        Retorna todas as provas cadastradas
        """
        return self.provas
