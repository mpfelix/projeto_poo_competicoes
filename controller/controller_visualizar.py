from model.equipe import Equipe
from model.prova import Prova
from model.resultado import ResultadoRepository

import mysql.connector

class ControllerVisualizar:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",       # ajuste para seu usuário
            password="",       # ajuste para sua senha
            database="competicoes"
        )
        self.cur = self.conn.cursor(dictionary=True)

    
    def listar_resultados(self):
        return ResultadoRepository.listar()

    def registrar_resultado(self, equipe_id, prova_id, pontuacao):
        ResultadoRepository.registrar(equipe_id, prova_id, pontuacao)
        return f"Resultado atualizado: equipe {equipe_id} -> {pontuacao} pontos"

    def remover_resultado(self, equipe_id, prova_id):
        ResultadoRepository.remover(equipe_id, prova_id)
        return f"Resultado removido (Equipe {equipe_id}, Prova {prova_id})"