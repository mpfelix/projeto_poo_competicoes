from PyQt5.QtWidgets import QMainWindow
from view.equipe_dialog import EquipeDialog
from view.prova_dialog import ProvaDialog
from view.listagem_dialog import ListagemDialog

class MainWindow(QMainWindow):
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
