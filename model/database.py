import mysql.connector
from mysql.connector import Error

# Configuração do banco
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",   # coloque sua senha do MySQL se tiver
    "database": "competicões"
}

def get_connection():
    """Cria e retorna uma conexão com o banco de dados MySQL"""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        if conn.is_connected():
            return conn
    except Error as e:
        print("Erro ao conectar ao MySQL:", e)
        return None
