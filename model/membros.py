from model.database import Database

class Membro:
    def __init__(self, id, nome, equipe_id):
        self.id = id
        self.nome = nome
        self.equipe_id = equipe_id


class MembroRepository:
    @staticmethod
    def listar():
        conn = Database.conectar()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT id, nome, equipe_id FROM membros")
        rows = cur.fetchall()
        conn.close()
        return [Membro(r["id"], r["nome"], r["equipe_id"]) for r in rows]

    @staticmethod
    def adicionar(nome, equipe_id):
        conn = Database.conectar()
        cur = conn.cursor()
        cur.execute("INSERT INTO membros (nome, equipe_id) VALUES (%s, %s)", (nome, equipe_id))
        conn.commit()
        conn.close()
