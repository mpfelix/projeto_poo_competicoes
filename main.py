import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
from view.main_window import MainWindow
from view.listagem_dialog import ListagemDialog


if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
        win = MainWindow()
        win.show()
        sys.exit(app.exec_())
    except Exception as e:
        QMessageBox.critical(None, "Erro fatal", str(e))
        sys.exit(1)

