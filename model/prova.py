import mysql.connector
from model.database import Database

class Prova:
    def __init__(self, id=None, nome=None, tipo=None, pontuacao_maxima=None, num_questoes=None, tempo_limite=None):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.pontuacao_maxima = pontuacao_maxima
        self.num_questoes = num_questoes
        self.tempo_limite = tempo_limite

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
        conn = Prova.conectar()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM provas")
        rows = cur.fetchall()
        conn.close()
        return rows

    @staticmethod
    def inserir(nome, tipo, pontuacao_maxima, num_questoes=None, tempo_limite=None):
        conn = Prova.conectar()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO provas (nome, tipo, pontuacao_maxima, num_questoes, tempo_limite)
            VALUES (%s, %s, %s, %s, %s)
        """, (nome, tipo, pontuacao_maxima, num_questoes, tempo_limite))
        conn.commit()
        conn.close()

    @staticmethod
    def remover(id):
        conn = Prova.conectar()
        cur = conn.cursor()
        cur.execute("DELETE FROM provas WHERE id=%s", (id,))
        conn.commit()
        conn.close()

class ProvaRepository:
    @staticmethod
    def listar():
        conn = Database.conectar()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM provas")
        rows = cur.fetchall()
        conn.close()
        return [Prova(**r) for r in rows]

    @staticmethod
    def adicionar(nome, tipo, pontuacao_maxima, num_questoes=None, tempo_limite=None):
        conn = Database.conectar()
        cur = conn.cursor()
        cur.execute(
            """INSERT INTO provas (nome, tipo, pontuacao_maxima, num_questoes, tempo_limite)
               VALUES (%s, %s, %s, %s, %s)""",
            (nome, tipo, pontuacao_maxima, num_questoes, tempo_limite),
        )
        conn.commit()
        conn.close()
