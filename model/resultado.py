import mysql.connector
from model.database import Database

class Resultado:
    def __init__(self, equipe_id=None, prova_id=None, pontuacao=None):
        self.equipe_id = equipe_id
        self.prova_id = prova_id
        self.pontuacao = pontuacao

    @staticmethod
    def conectar():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="competicoes"
        )

    @staticmethod
    def listar():
        conn = Resultado.conectar()
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

    @staticmethod
    def registrar(equipe_id, prova_id, pontuacao):
        conn = Resultado.conectar()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO resultados (equipe_id, prova_id, pontuacao)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE pontuacao = VALUES(pontuacao)
        """, (equipe_id, prova_id, pontuacao))
        conn.commit()
        conn.close()

    @staticmethod
    def remover(equipe_id, prova_id):
        conn = Resultado.conectar()
        cur = conn.cursor()
        cur.execute("DELETE FROM resultados WHERE equipe_id=%s AND prova_id=%s", (equipe_id, prova_id))
        conn.commit()
        conn.close()


class ResultadoRepository:
    @staticmethod
    def listar():
        conn = Database.conectar()
        cur = conn.cursor(dictionary=True)
        cur.execute("""
            SELECT r.id, r.equipe_id, r.prova_id, r.pontuacao,
                   e.nome AS equipe_nome, p.nome AS prova_nome
            FROM resultados r
            JOIN equipes e ON e.id = r.equipe_id
            JOIN provas p ON p.id = r.prova_id
            ORDER BY p.nome, r.pontuacao DESC
        """)
        rows = cur.fetchall()
        conn.close()
        return rows

    @staticmethod
    def registrar(equipe_id, prova_id, pontuacao):
        conn = Database.conectar()
        cur = conn.cursor()
        cur.execute(
            """INSERT INTO resultados (equipe_id, prova_id, pontuacao)
               VALUES (%s, %s, %s)
               ON DUPLICATE KEY UPDATE pontuacao = VALUES(pontuacao)""",
            (equipe_id, prova_id, pontuacao),
        )
        conn.commit()
        conn.close()

    @staticmethod
    def remover(equipe_id, prova_id):
        conn = Database.conectar()
        cur = conn.cursor()
        cur.execute("DELETE FROM resultados WHERE equipe_id=%s AND prova_id=%s", (equipe_id, prova_id))
        conn.commit()
        conn.close()
