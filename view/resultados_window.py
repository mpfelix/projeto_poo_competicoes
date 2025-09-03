from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QLabel
from controller.controller_equipes import ControllerEquipes
from controller.controller_provas import ControllerProvas

class ResultadosWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Resultados")
        self.resize(700, 400)

        self.ctrl_eq = ControllerEquipes()
        self.ctrl_pr = ControllerProvas()

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Equipes:"))
        self.tab_eq = QTableWidget(0, 2)
        self.tab_eq.setHorizontalHeaderLabels(["ID", "Nome"])
        layout.addWidget(self.tab_eq)

        layout.addWidget(QLabel("Provas:"))
        self.tab_pr = QTableWidget(0, 4)
        self.tab_pr.setHorizontalHeaderLabels(["ID", "Nome", "Tipo", "Máxima"])
        layout.addWidget(self.tab_pr)

        self.carregar()

    def carregar(self):
        self.tab_eq.setRowCount(0)
        for (id_, nome) in self.ctrl_eq.listar_equipes():
            r = self.tab_eq.rowCount()
            self.tab_eq.insertRow(r)
            self.tab_eq.setItem(r, 0, QTableWidgetItem(str(id_)))
            self.tab_eq.setItem(r, 1, QTableWidgetItem(nome))

        self.tab_pr.setRowCount(0)
        for (id_, nome, tipo, max_, _q, _t) in self.ctrl_pr.listar():
            r = self.tab_pr.rowCount()
            self.tab_pr.insertRow(r)
            self.tab_pr.setItem(r, 0, QTableWidgetItem(str(id_)))
            self.tab_pr.setItem(r, 1, QTableWidgetItem(nome))
            self.tab_pr.setItem(r, 2, QTableWidgetItem(tipo))
            self.tab_pr.setItem(r, 3, QTableWidgetItem(str(max_)))
