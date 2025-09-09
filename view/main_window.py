from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox

from view.equipe_dialog import EquipeDialog
from view.prova_dialog import ProvaDialog
from view.listagem_dialog import ListagemDialog
from view.resultados_dialog import ResultadosWindow

from model.equipe import EquipeRepository
from model.prova import ProvaRepository
from model.resultado import ResultadoRepository


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Competições")
        self.resize(500, 400)

        self.janelas = []

        layout = QVBoxLayout()

        # Botão: cadastrar equipe
        btn_cadastrar_equipe = QPushButton("Cadastrar Equipe")
        btn_cadastrar_equipe.clicked.connect(self.cadastrar_equipe)
        layout.addWidget(btn_cadastrar_equipe)

        # Botão: listar equipes
        btn_listar_equipes = QPushButton("Listar Equipes")
        btn_listar_equipes.clicked.connect(self.listar_equipes)
        layout.addWidget(btn_listar_equipes)

        # Botão: cadastrar prova
        btn_cadastrar_prova = QPushButton("Cadastrar Prova")
        btn_cadastrar_prova.clicked.connect(self.cadastrar_prova)
        layout.addWidget(btn_cadastrar_prova)

        # Botão: listar provas
        btn_listar_provas = QPushButton("Listar Provas")
        btn_listar_provas.clicked.connect(self.listar_provas)
        layout.addWidget(btn_listar_provas)

        # Botão: cadastrar resultado
        btn_cadastrar_resultado = QPushButton("Cadastrar Resultado")
        btn_cadastrar_resultado.clicked.connect(self.cadastrar_resultado)
        layout.addWidget(btn_cadastrar_resultado)

        # Botão: visualizar resultados
        btn_visualizar_resultados = QPushButton("Visualizar Resultados")
        btn_visualizar_resultados.clicked.connect(self.visualizar_resultados)
        layout.addWidget(btn_visualizar_resultados)

        # Botão: abrir janela de resultados
        btn_abrir_resultados = QPushButton("Abrir Resultados (Janela)")
        btn_abrir_resultados.clicked.connect(self.abrir_resultados)
        layout.addWidget(btn_abrir_resultados)

        # Widget central
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


    # =========================
    # Métodos
    # =========================
    def cadastrar_equipe(self):
        dialog = EquipeDialog()
        if dialog.exec_() == dialog.Accepted:
            QMessageBox.information(self, "Sucesso", "Equipe cadastrada com sucesso!")

    def listar_equipes(self):
        equipes = EquipeRepository.listar()
        dados = [{"ID": e.id, "Nome": e.nome} for e in equipes]
        dialog = ListagemDialog("Equipes", dados)
        dialog.exec_()

    def cadastrar_prova(self):
        dialog = ProvaDialog()
        if dialog.exec_() == dialog.Accepted:
            QMessageBox.information(self, "Sucesso", "Prova cadastrada com sucesso!")

    def listar_provas(self):
        provas = ProvaRepository.listar()
        dados = [
            {
                "ID": p.id,
                "Nome": p.nome,
                "Tipo": p.tipo,
                "Máxima": p.pontuacao_maxima,
                "Questões": p.num_questoes,
                "Tempo": p.tempo_limite,
            }
            for p in provas
        ]
        dialog = ListagemDialog("Provas", dados)
        dialog.exec_()
        
    def cadastrar_resultado(self):
        dialog = ResultadosWindow()
        if dialog.exec_() == dialog.Accepted:
            QMessageBox.information(self, "Sucesso", "Resultado cadastrado com sucesso!")


    def visualizar_resultados(self):
        resultados = ResultadoRepository.listar()
        dados = [
            {
                "ID": r["id"],
                "Equipe": r["equipe_nome"],
                "Prova": r["prova_nome"],
                "Pontuação": r["pontuacao"],
            }
            for r in resultados
        ]
        dialog = ListagemDialog("Resultados", dados)
        dialog.exec_()

    def abrir_resultados(self):
        janela = ResultadosWindow()
        janela.show()
        self.janelas.append(janela)
