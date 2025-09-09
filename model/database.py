import mysql.connector

class Database:
    @staticmethod
    def conectar():
        """
        Cria e retorna a conexão com o banco de dados MySQL.
        Ajuste os parâmetros conforme sua configuração.
        """
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",       # seu usuário do MySQL
                password="",       # sua senha do MySQL
                database="competicoes"
            )
            return conn
        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            raise
