import sys
import traceback
from PyQt5.QtWidgets import QApplication, QMessageBox
from view.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    try:
        win = MainWindow()
        win.show()
        sys.exit(app.exec_())
    except Exception as e:
        traceback.print_exc()
        QMessageBox.critical(None, "Erro fatal", f"{type(e).__name__}: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
