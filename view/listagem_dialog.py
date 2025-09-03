from PyQt5.QtWidgets import QDialog, QVBoxLayout, QListWidget, QPushButton
from controller.controller_equipes import ControllerEquipes
from controller.controller_provas import ControllerProvas
from model.repositories import ResultadoRepository

class ListagemDialog(QDialog):
    def __init__(self, tipo="equipes"):
        super().__init__()
        self.setWindowTitle(f"Listagem de {tipo.capitalize()}")
        self.setGeometry(200, 200, 400, 300)

        layout = QVBoxLayout()
        self.lista = QListWidget()

        if tipo == "equipes":
            controller = ControllerEquipes()
            dados = controller.listar_equipes()
            for e in dados:
                self.lista.addItem(f"ID {e[0]} - {e[1]}")
        elif tipo == "provas":
            controller = ControllerProvas()
            dados = controller.listar_provas()
            for p in dados:
                self.lista.addItem(f"ID {p[0]} - {p[1]} ({p[2]}) - Máx {p[3]}")
        elif tipo == "resultados":
            repo = ResultadoRepository()
            dados = repo.listar()
            for r in dados:
                self.lista.addItem(f"Equipe {r[0]} - Prova {r[1]} - Pontos {r[2]}")

        btn_fechar = QPushButton("Fechar")
        btn_fechar.clicked.connect(self.close)

        layout.addWidget(self.lista)
        layout.addWidget(btn_fechar)

        self.setLayout(layout)
