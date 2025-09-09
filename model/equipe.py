from model.database import Database

class Equipe:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome


class EquipeRepository:
    @staticmethod
    def listar():
        conn = Database.conectar()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT id, nome FROM equipes")
        rows = cur.fetchall()
        conn.close()
        return [Equipe(r["id"], r["nome"]) for r in rows]

    @staticmethod
    def adicionar(nome):
        conn = Database.conectar()
        cur = conn.cursor()
        cur.execute("INSERT INTO equipes (nome) VALUES (%s)", (nome,))
        conn.commit()
        conn.close()
