from model.equipe import EquipeRepository

class ControllerEquipes:
    def __init__(self):
        self.repo = EquipeRepository()

    def adicionar_equipe(self, nome):
        return self.repo.adicionar_equipe(nome)

    def adicionar_membro(self, nome_equipe, nome_membro):
        return self.repo.adicionar_membro(nome_equipe, nome_membro)

    def listar_equipes(self):
        return self.repo.listar_equipes()
