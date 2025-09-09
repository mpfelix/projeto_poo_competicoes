from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from controller.controller_provas import ControllerProvas

class ProvaDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastrar Prova")
        self.setGeometry(200, 200, 300, 200)

        self.controller = ControllerProvas()

        layout = QVBoxLayout()

        self.input_nome = QLineEdit()
        self.input_nome.setPlaceholderText("Nome da Prova")

        self.input_tipo = QLineEdit()
        self.input_tipo.setPlaceholderText("Tipo (teórica/prática)")

        self.input_pontos = QLineEdit()
        self.input_pontos.setPlaceholderText("Pontuação Máxima")

        btn_salvar = QPushButton("Salvar")
        btn_salvar.clicked.connect(self.salvar)

        layout.addWidget(QLabel("Nome da Prova:"))
        layout.addWidget(self.input_nome)
        layout.addWidget(QLabel("Tipo:"))
        layout.addWidget(self.input_tipo)
        layout.addWidget(QLabel("Pontuação Máxima:"))
        layout.addWidget(self.input_pontos)
        layout.addWidget(btn_salvar)

        self.setLayout(layout)

    def salvar(self):
        nome = self.input_nome.text()
        tipo = self.input_tipo.text()
        pontos = self.input_pontos.text()

        if not nome.strip() or not tipo.strip() or not pontos.strip():
            QMessageBox.warning(self, "Erro", "Todos os campos devem ser preenchidos.")
            return

        self.controller.cadastrar_prova(nome, tipo, pontos)
        QMessageBox.information(self, "Sucesso", f"Prova '{nome}' cadastrada!")
        self.close()
