import mysql.connector
from mysql.connector import Error
from .database import get_connection

class EquipeRepository:

    @staticmethod
    def criar(nome):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO equipes (nome) VALUES (%s)", (nome,))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Error as e:
            print("Erro ao criar equipe:", e)
            return False

    @staticmethod
    def listar():
        try:
            conn = get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM equipes")
            equipes = cursor.fetchall()
            cursor.close()
            conn.close()
            return equipes
        except Error as e:
            print("Erro ao listar equipes:", e)
            return []

class MembroRepository:

    @staticmethod
    def criar(nome, equipe_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO membros (nome, equipe_id) VALUES (%s, %s)", (nome, equipe_id))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Error as e:
            print("Erro ao criar membro:", e)
            return False

    @staticmethod
    def listar_por_equipe(equipe_id):
        try:
            conn = get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM membros WHERE equipe_id = %s", (equipe_id,))
            membros = cursor.fetchall()
            cursor.close()
            conn.close()
            return membros
        except Error as e:
            print("Erro ao listar membros:", e)
            return []

class ProvaRepository:

    @staticmethod
    def criar(nome, tipo, pontuacao_maxima, numero_questoes=None, tempo_limite=None):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO provas (nome, tipo, pontuacao_maxima, numero_questoes, tempo_limite) 
                VALUES (%s, %s, %s, %s, %s)
            """, (nome, tipo, pontuacao_maxima, numero_questoes, tempo_limite))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Error as e:
            print("Erro ao criar prova:", e)
            return False

    @staticmethod
    def listar():
        try:
            conn = get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM provas")
            provas = cursor.fetchall()
            cursor.close()
            conn.close()
            return provas
        except Error as e:
            print("Erro ao listar provas:", e)
            return []

class ResultadoRepository:

    @staticmethod
    def registrar(equipe_id, prova_id, pontuacao):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO resultados (equipe_id, prova_id, pontuacao) 
                VALUES (%s, %s, %s)
            """, (equipe_id, prova_id, pontuacao))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Error as e:
            print("Erro ao registrar resultado:", e)
            return False

    @staticmethod
    def listar():
        try:
            conn = get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT r.id, e.nome as equipe, p.nome as prova, r.pontuacao
                FROM resultados r
                JOIN equipes e ON r.equipe_id = e.id
                JOIN provas p ON r.prova_id = p.id
            """)
            resultados = cursor.fetchall()
            cursor.close()
            conn.close()
            return resultados
        except Error as e:
            print("Erro ao listar resultados:", e)
            return []

