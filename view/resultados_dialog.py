from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QMessageBox

from view.listagem_dialog import ListagemDialog
from model.resultado import ResultadoRepository


class ResultadosWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Resultados das Competições")
        self.resize(500, 400)

        layout = QVBoxLayout()

        # Botão para atualizar resultados
        btn_atualizar = QPushButton("Atualizar Resultados")
        btn_atualizar.clicked.connect(self.visualizar_resultados)
        layout.addWidget(btn_atualizar)

        # Container central
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def visualizar_resultados(self):
        try:
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
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Não foi possível carregar os resultados:\n{e}")
