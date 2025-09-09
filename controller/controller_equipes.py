from model.repositories import EquipeRepository, MembroRepository

class ControllerEquipes:
    def __init__(self):
        self.equipes = []  # Lista que vai guardar as equipes cadastradas

    def cadastrar_equipe(self, nome, membros):
        equipe = {
            "nome": nome,
            "membros": membros
        }
        self.equipes.append(equipe)
        print("Equipe cadastrada:", equipe)
        return equipe
    
    @staticmethod
    def criar_equipe(nome):
        return EquipeRepository.criar(nome)

    @staticmethod
    def listar_equipes():
        return EquipeRepository.listar()

    @staticmethod
    def adicionar_membro(nome, equipe_id):
        return MembroRepository.criar(nome, equipe_id)

    @staticmethod
    def listar_membros(equipe_id):
        return MembroRepository.listar_por_equipe(equipe_id)

