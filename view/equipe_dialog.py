from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from controller.controller_equipes import ControllerEquipes

class EquipeDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastrar Equipe")
        self.setGeometry(200, 200, 300, 200)

        self.controller = ControllerEquipes()

        layout = QVBoxLayout()

        self.input_nome = QLineEdit()
        self.input_nome.setPlaceholderText("Nome da Equipe")

        self.input_membros = QLineEdit()
        self.input_membros.setPlaceholderText("Membros (separados por vírgula)")

        btn_salvar = QPushButton("Salvar")
        btn_salvar.clicked.connect(self.salvar)

        layout.addWidget(QLabel("Nome da Equipe:"))
        layout.addWidget(self.input_nome)
        layout.addWidget(QLabel("Membros:"))
        layout.addWidget(self.input_membros)
        layout.addWidget(btn_salvar)

        self.setLayout(layout)

    def salvar(self):
        nome = self.input_nome.text()
        membros = self.input_membros.text().split(",")

        if not nome.strip():
            QMessageBox.warning(self, "Erro", "O nome da equipe não pode ser vazio.")
            return

        self.controller.cadastrar_equipe(nome, membros)
        QMessageBox.information(self, "Sucesso", f"Equipe '{nome}' cadastrada!")
        self.close()
