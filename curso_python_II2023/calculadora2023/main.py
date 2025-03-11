from PyQt6 import QtCore, QtGui, QtWidgets
import sys

#paquetes propios
from controllers.controller_calculadora import MainWindow
#rom view.view_calculadora import Ui_Calculadorav3


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())