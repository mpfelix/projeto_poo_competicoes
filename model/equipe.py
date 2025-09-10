class Equipe:
    def __init__(self, nome):
        self.nome = nome
        self.membros = []

    def adicionar_membro(self, nome_membro):
        if nome_membro not in self.membros:
            self.membros.append(nome_membro)

    def __repr__(self):
        return f"Equipe({self.nome}, membros={len(self.membros)})"


class EquipeRepository:
    def __init__(self):
        self.equipes = []

    def adicionar_equipe(self, nome):
        # Evitar duplicatas
        for e in self.equipes:
            if e.nome == nome:
                return e
        equipe = Equipe(nome)
        self.equipes.append(equipe)
        return equipe

    def adicionar_membro(self, nome_equipe, nome_membro):
        for equipe in self.equipes:
            if equipe.nome == nome_equipe:
                equipe.adicionar_membro(nome_membro)
                return True
        return False

    def listar_equipes(self):
        return self.equipes
