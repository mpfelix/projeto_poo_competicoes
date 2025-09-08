from PyQt5.QtWidgets import QMainWindow,QPushButton
from view.equipe_dialog import EquipeDialog
from view.prova_dialog import ProvaDialog
from view.listagem_dialog import ListagemDialog
from .resultados_window import ResultadosWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de competições")
    ...
    def cadastrar_equipe(self):
        dialog = EquipeDialog()
        dialog.exec_()
        

    def listar_equipes(self):
        dialog = ListagemDialog("equipes")
        dialog.exec_()

    def cadastrar_prova(self):
        dialog = ProvaDialog()
        dialog.exec_()

    def listar_provas(self):
        dialog = ListagemDialog("provas")
        dialog.exec_()

    def visualizar_resultados(self):
        dialog = ListagemDialog("resultados")
        dialog.exec_()
        
    def abrir_resultados(self):
        janela = ResultadosWindow()
        janela.show()
        self.janelas.append(janela)
