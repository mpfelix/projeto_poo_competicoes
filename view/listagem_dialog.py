from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem

class ListagemDialog(QDialog):
    def __init__(self, titulo, dados, parent=None):
        super().__init__(parent)
        self.setWindowTitle(titulo)
        self.resize(400, 300)

        layout = QVBoxLayout()

        # Tabela para exibir os dados
        self.table = QTableWidget()
        layout.addWidget(self.table)

        # Botão de fechar
        btn_fechar = QPushButton("Fechar")
        btn_fechar.clicked.connect(self.close)
        layout.addWidget(btn_fechar)

        self.setLayout(layout)

        # Preenche a tabela com os dados
        self.carregar_dados(dados)

    def carregar_dados(self, dados):
        if not dados:
            self.table.setRowCount(0)
            self.table.setColumnCount(0)
            return

        # Assume que todos os itens têm as mesmas chaves
        colunas = list(dados[0].keys())
        self.table.setColumnCount(len(colunas))
        self.table.setHorizontalHeaderLabels(colunas)
        self.table.setRowCount(len(dados))

        for row, item in enumerate(dados):
            for col, chave in enumerate(colunas):
                self.table.setItem(row, col, QTableWidgetItem(str(item[chave])))
                
    def listar_resultados(self):
        sql = """
        SELECT p.nome AS Prova, e.nome AS Equipe, r.pontuacao AS Pontuação
        FROM resultados r
        JOIN equipes e ON r.equipe_id = e.id
        JOIN provas p ON r.prova_id = p.id
        ORDER BY p.nome, r.pontuacao DESC
        """
        self.cur.execute(sql)
        rows = self.cur.fetchall()

        # já vem como dict porque usamos cursor(dictionary=True)
        return rows if rows else []
