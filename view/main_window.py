from PyQt5.QtWidgets import QMainWindow,QPushButton, QVBoxLayout, QWidget

from view.equipe_dialog import EquipeDialog
from view.prova_dialog import ProvaDialog
from view.listagem_dialog import ListagemDialog
from .resultados_window import ResultadosWindow

from controller.controller_equipes import ControllerEquipes
from controller.controller_provas import ControllerProvas

class MainWindow(QMainWindow):
    def center(self):
        frame_geom = self.frameGeometry()
        screen_center = self.screen().availableGeometry().center()
        frame_geom.moveCenter(screen_center)
        self.move(frame_geom.topLeft())
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Competições")
        self.resize(400, 300)
        self.center()
        
        self.controller_equipes = ControllerEquipes()
        self.controller_provas = ControllerProvas()

        
        self.janelas = []
        
        layout = QVBoxLayout()
        
        btn_cadastrar_equipe = QPushButton("Cadastrar Equipe")
        btn_cadastrar_equipe.clicked.connect(self.cadastrar_equipe)
        btn_cadastrar_equipe.setStyleSheet("background-color: #4CAF50; color: white; padding: 8px;")

        layout.addWidget(btn_cadastrar_equipe)

        btn_listar_equipes = QPushButton("Listar Equipes")
        btn_listar_equipes.clicked.connect(self.listar_equipes)
        btn_listar_equipes.setStyleSheet("background-color: #4CAF50; color: white; padding: 8px;")

        layout.addWidget(btn_listar_equipes)

        btn_cadastrar_prova = QPushButton("Cadastrar Prova")
        btn_cadastrar_prova.clicked.connect(self.cadastrar_prova)
        btn_cadastrar_prova.setStyleSheet("background-color: #4CAF50; color: white; padding: 8px;")

        layout.addWidget(btn_cadastrar_prova)
        
        btn_listar_provas = QPushButton("Listar Provas")
        btn_listar_provas.clicked.connect(self.listar_provas)
        btn_listar_provas.setStyleSheet("background-color: #4CAF50; color: white; padding: 8px;")

        layout.addWidget(btn_listar_provas)

        btn_visualizar_resultados = QPushButton("Visualizar Resultados")
        btn_visualizar_resultados.clicked.connect(self.visualizar_resultados)
        btn_visualizar_resultados.setStyleSheet("background-color: #4CAF50; color: white; padding: 8px;")

        layout.addWidget(btn_visualizar_resultados)

        btn_abrir_resultados = QPushButton("Abrir Resultados (janela)")
        btn_abrir_resultados.clicked.connect(self.abrir_resultados)
        btn_abrir_resultados.setStyleSheet("background-color: #4CAF50; color: white; padding: 8px;")

        layout.addWidget(btn_abrir_resultados)

        # Widget central
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    ...
    def cadastrar_equipe(self):
        dialog = EquipeDialog()
        dialog.exec_()
        
    def listar_equipes(self):
        equipes = self.controller_equipes.listar_equipes()
        dialog = ListagemDialog("Listagem de Equipes", equipes)
        dialog.exec_()

    def cadastrar_prova(self):
        dialog = ProvaDialog()
        dialog.exec_()

    def listar_provas(self):
        provas = self.controller_provas.listar_provas()
        dialog = ListagemDialog("Listagem de Provas", provas)
        dialog.exec_()

    def visualizar_resultados(self):
        resultados = self.controller_resultados.listar_resultados()
        dialog = ListagemDialog("Resultados", resultados)
        dialog.exec_()
        
    def abrir_resultados(self):
        janela = ResultadosWindow()
        janela.show()
        self.janelas.append(janela)
