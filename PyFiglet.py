#!/usr/bin/python
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic
import pyfiglet


class Ui(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('figlet.ui', self)
        self.setFixedSize(510, 350)

        def scelta_fonts(self):
            self.cB_font.addItem("colossal")
            self.cB_font.addItem("3x5")
            self.cB_font.addItem("slant")
            self.cB_font.addItem("3-d")
            self.cB_font.addItem("5lineoblique")
            self.cB_font.addItem("alphabet")
            self.cB_font.addItem("banner3-D")
            self.cB_font.addItem("doh")
            self.cB_font.addItem("isometric1")
            self.cB_font.addItem("letters")
            self.cB_font.addItem("alligator")
            self.cB_font.addItem("dotmatrix")
            self.cB_font.addItem("bubble")
            self.cB_font.addItem("bulbhead")
            self.cB_font.addItem("digital")

        scelta_fonts(self)

    def pB_FigletClick(self):
        try:
            cur_font = (self.cB_font.currentText())
            testo = self.lE_testo.text()
            result = pyfiglet.figlet_format(testo, font=cur_font)
            self.pTE_Figlet.setPlainText(result)
        except:
            print("Testo non valido")

    def lE_testoChange(self):
        self.pTE_Figlet.clear()


app = QApplication([])
window = Ui()
window.show()
app.exec()