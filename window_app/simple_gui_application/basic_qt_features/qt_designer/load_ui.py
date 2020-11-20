# Version : python 3.7.4
# File : load_ui.py
# Author : Lila Morgen
# Time : 2020/11/20 2:35
# description : 

import sys
from PyQt5 import QtWidgets, uic


def mainwindow(w):
    w.setWindowTitle('Hello')


app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi('ui_files/use_method_to_load.ui')
mainwindow(window)
window.show()
app.exec_()
