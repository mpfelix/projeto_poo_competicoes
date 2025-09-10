import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from controller.controller_equipes import ControllerEquipes
from controller.controller_provas import ControllerProvas
from controller.controller_resultados import ControllerResultados


from view.tela_principal import Ui_TelaPrincipal
from view.cadastro_equipes import Ui_CadastroEquipes
from view.cadastro_provas import Ui_CadastroProvas
from view.visualizar_resultados import Ui_VisualizarResultados
from view.cadastro_membros import Ui_CadastroMembros



class TelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TelaPrincipal()
        self.ui.setupUi(self)

       
        self.equipes_ctrl = ControllerEquipes()
        self.provas_ctrl = ControllerProvas()
        self.resultados_ctrl = ControllerResultados()

        
        self._popular_dados()

        
        self.ui.btn_equipes.clicked.connect(self.abrir_equipes)
        self.ui.btn_membros.clicked.connect(self.abrir_membros)
        self.ui.btn_provas.clicked.connect(self.abrir_provas)
        self.ui.btn_resultados.clicked.connect(self.abrir_resultados)

    def _popular_dados(self):
        
        self.equipes_ctrl.adicionar_equipe("Equipe Falcões")
        self.equipes_ctrl.adicionar_equipe("Equipe Águias")
        self.equipes_ctrl.adicionar_equipe("Equipe Leões")

     
        self.equipes_ctrl.adicionar_membro("Equipe Falcões", "Ana Silva")
        self.equipes_ctrl.adicionar_membro("Equipe Falcões", "Carlos Souza")
        self.equipes_ctrl.adicionar_membro("Equipe Águias", "Beatriz Lima")
        self.equipes_ctrl.adicionar_membro("Equipe Águias", "Marcos Rocha")
        self.equipes_ctrl.adicionar_membro("Equipe Leões", "João Pedro")

       
        self.provas_ctrl.adicionar_prova_teorica("Prova Teórica 1", 100, 20)
        self.provas_ctrl.adicionar_prova_pratica("Prova Prática 1", 100, 60)

        self.resultados_ctrl.adicionar_resultado("Equipe Falcões", "Prova Teórica 1", 85.0)
        self.resultados_ctrl.adicionar_resultado("Equipe Águias", "Prova Teórica 1", 70.0)
        self.resultados_ctrl.adicionar_resultado("Equipe Leões", "Prova Prática 1", 95.0)

    def abrir_equipes(self):
        self.janela_equipes = TelaEquipes(self.equipes_ctrl)
        self.janela_equipes.show()

    def abrir_provas(self):
        self.janela_provas = TelaProvas(self.provas_ctrl)
        self.janela_provas.show()

    def abrir_resultados(self):
        self.janela_resultados = TelaResultados(self.resultados_ctrl)
        self.janela_resultados.show()

    def abrir_membros(self):
        self.janela_membros = TelaMembros(self.equipes_ctrl)
        self.janela_membros.show()



class TelaEquipes(QWidget):
    def __init__(self, equipes_ctrl):
        super().__init__()
        self.ui = Ui_CadastroEquipes()
        self.ui.setupUi(self)
        self.equipes_ctrl = equipes_ctrl

      
        self.ui.btn_adicionar.clicked.connect(self.adicionar_equipe)

    def adicionar_equipe(self):
        nome = self.ui.input_nome.text()
        if nome:
            self.equipes_ctrl.adicionar_equipe(nome)
            self.ui.lista_equipes.addItem(nome)
            self.ui.input_nome.clear()



class TelaProvas(QWidget):
    def __init__(self, provas_ctrl):
        super().__init__()
        self.ui = Ui_CadastroProvas()
        self.ui.setupUi(self)
        self.provas_ctrl = provas_ctrl

       
        self.ui.btn_adicionar.clicked.connect(self.adicionar_prova)

    def adicionar_prova(self):
        nome = self.ui.input_nome.text()
        tipo = self.ui.combo_tipo.currentText()
        if nome and tipo:
            if tipo == "Teórica":
                num_questoes = int(self.ui.input_questoes.text())
                self.provas_ctrl.adicionar_prova_teorica(nome, 100, num_questoes)
            else:
                tempo = int(self.ui.input_tempo.text())
                self.provas_ctrl.adicionar_prova_pratica(nome, 100, tempo)

            self.ui.lista_provas.addItem(f"{nome} ({tipo})")
            self.ui.input_nome.clear()
            self.ui.input_questoes.clear()
            self.ui.input_tempo.clear()


class TelaResultados(QWidget):
    def __init__(self, resultados_ctrl):
        super().__init__()
        self.ui = Ui_VisualizarResultados()
        self.ui.setupUi(self)
        self.resultados_ctrl = resultados_ctrl

       
        for r in self.resultados_ctrl.listar_resultados():
            self.ui.lista_resultados.addItem(f"{r['equipe']} - {r['prova']}: {r['pontuacao']}")


class TelaMembros(QWidget):
    def __init__(self, equipes_ctrl):
        super().__init__()
        self.ui = Ui_CadastroMembros()
        self.ui.setupUi(self)
        self.equipes_ctrl = equipes_ctrl

        
        self.ui.btn_adicionar.clicked.connect(self.adicionar_membro)

    def adicionar_membro(self):
        equipe = self.ui.input_equipe.text()
        nome = self.ui.input_nome.text()
        if equipe and nome:
            self.equipes_ctrl.adicionar_membro(equipe, nome)
            self.ui.lista_membros.addItem(f"{nome} ({equipe})")
            self.ui.input_nome.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TelaPrincipal()
    window.show()
    sys.exit(app.exec_())
