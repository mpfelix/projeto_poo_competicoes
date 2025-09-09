from model.equipe import EquipeRepository
from model.membros import MembroRepository
from model.resultado import ResultadoRepository
from model.prova import ProvaRepository
from .database import Database

class EquipeRepository:
    @staticmethod
    def listar():
        conn = Database.conectar()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM equipes")
        rows = cur.fetchall()
        conn.close()
        return rows

class MembroRepository:
    @staticmethod
    def listar():
        conn = Database.conectar()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM membros")
        rows = cur.fetchall()
        conn.close()
        return rows

class ProvaRepository:
    @staticmethod
    def listar():
        conn = Database.conectar()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM provas")
        rows = cur.fetchall()
        conn.close()
        return rows

class ResultadoRepository:
    @staticmethod
    def listar():
        conn = Database.conectar()
        cur = conn.cursor(dictionary=True)
        cur.execute("""
            SELECT p.nome AS prova, e.nome AS equipe, r.pontuacao
            FROM resultados r
            JOIN equipes e ON r.equipe_id = e.id
            JOIN provas p ON r.prova_id = p.id
            ORDER BY p.nome, r.pontuacao DESC
        """)
        rows = cur.fetchall()
        conn.close()
        return rows


__all__ = [
    "EquipeRepository",
    "MembroRepository",
    "ProvaRepository",
    "ResultadoRepository",
]
