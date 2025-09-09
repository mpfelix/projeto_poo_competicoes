class Equipe:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.membros = []

    def adicionar_membro(self, membro):
        self.membros.append(membro)
