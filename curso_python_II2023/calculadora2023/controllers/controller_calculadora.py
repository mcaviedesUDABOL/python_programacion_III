#librerias y paquetes
from PyQt6 import QtCore, QtGui, QtWidgets
import sys
import math

#paquetes propios del sistema
from view.view_calculadora import Ui_Calculadorav3
from events.event_calculadora import eventos

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.calculadora = Ui_Calculadorav3()
        self.calculadora.setupUi(self)

        # -- Button: clicked ---
        self.calculadora.btn_0.clicked.connect(lambda: self.btnClicked("0"))
        self.calculadora.btn_1.clicked.connect(lambda: self.btnClicked("1"))
        self.calculadora.btn_2.clicked.connect(lambda: self.btnClicked("2"))
        self.calculadora.btn_3.clicked.connect(lambda: self.btnClicked("3"))
        self.calculadora.btn_4.clicked.connect(lambda: self.btnClicked("4"))
        self.calculadora.btn_5.clicked.connect(lambda: self.btnClicked("5"))
        self.calculadora.btn_6.clicked.connect(lambda: self.btnClicked("6"))
        self.calculadora.btn_7.clicked.connect(lambda: self.btnClicked("7"))
        self.calculadora.btn_8.clicked.connect(lambda: self.btnClicked("8"))
        self.calculadora.btn_9.clicked.connect(lambda: self.btnClicked("9"))
        self.calculadora.btn_suma.clicked.connect(lambda: self.btnClicked("+"))
        self.calculadora.btn_resta.clicked.connect(lambda: self.btnClicked("-"))
        self.calculadora.btn_multiplicacion.clicked.connect(lambda: self.btnClicked("*"))
        self.calculadora.btn_division.clicked.connect(lambda: self.btnClicked("/"))
        self.calculadora.btn_pa.clicked.connect(lambda: self.btnClicked("("))
        self.calculadora.btn_pc.clicked.connect(lambda: self.btnClicked(")"))
        self.calculadora.btn_c.clicked.connect(lambda: self.btnClicked("C"))
        self.calculadora.btn_igual.clicked.connect(lambda: self.btnClicked("="))
        self.calculadora.btn_punto.clicked.connect(lambda: self.btnClicked("."))
        self.calculadora.btn_all_clear.clicked.connect(lambda: self.btnClicked("CE"))
        self.calculadora.btn_porcentaje.clicked.connect(lambda: self.btnClicked("%"))
        # calculadora parte cientifica
        self.calculadora.btn_pow.clicked.connect(lambda: self.btnClicked("pow"))
        self.calculadora.btn_sin.clicked.connect(lambda: self.btnClicked("sin"))
        self.calculadora.btn_cos.clicked.connect(lambda: self.btnClicked("cos"))
        self.calculadora.btn_tan.clicked.connect(lambda: self.btnClicked("tan"))
        self.calculadora.btn_sen_m1.clicked.connect(lambda: self.btnClicked("asin"))
        self.calculadora.btn_cos_m1.clicked.connect(lambda: self.btnClicked("acos"))
        self.calculadora.btn_tan_m1.clicked.connect(lambda: self.btnClicked("atan"))

    def btnClicked(self, boton):
        try:
            self.validarLabel()
            texto = self.calculadora.lbl_formula.text()
            if ((boton.isnumeric() == True) or (boton.isalnum() == False) and boton != "="):
                self.calculadora.lbl_formula.setText(texto + boton)
            elif boton == "C":
                self.calculadora.lbl_formula.setText(texto[:-1])
            elif boton == "CE":
                self.calculadora.lbl_formula.setText("CalculadoraQT")
                self.calculadora.lne_resultado.clear()
            elif boton == "mod":
                pass
            elif boton == "%":
                self.calculadora.lbl_formula.setText(texto + boton)
            elif boton == "=":
                if self.calculadora.lne_resultado.text() != "":
                    self.calculadora.lne_resultado.clear()
                try:
                    self.calculadora.lne_resultado.insert(str(eval(texto)))
                except:
                    self.calculadora.lne_resultado.insert("Error")
                    self.calculadora.statusBar.showMessage("Error: verifique la operación ingresada")
            elif boton == "pow":
                self.calculadora.lbl_formula.setText(texto + "sqrt(")
            elif boton == "sin":
                self.calculadora.lbl_formula.setText(texto + "math.sin(")
            elif boton == "cos":
                self.calculadora.lbl_formula.setText(texto + "math.cos(")
            elif boton == "tan":
                self.calculadora.lbl_formula.setText(texto + "math.tan(")
            elif boton == "asin":
                self.calculadora.lbl_formula.setText(texto + "math.sinh(")
            elif boton == "acos":
                self.calculadora.lbl_formula.setText(texto + "math.acos(")
            elif boton == "atan":
                self.calculadora.lbl_formula.setText(texto + "math.atan(")
        except(NameError):
            self.calculadora.statusBar.showMessage("Error: funsiones")

    def validarLabel(self):
        if self.calculadora.lbl_formula.text() == "CalculadoraQT":
            self.calculadora.lbl_formula.setText("")
