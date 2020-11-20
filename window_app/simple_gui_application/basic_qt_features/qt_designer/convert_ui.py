# Version : python 3.7.4
# File : convert_ui.py
# Author : Lila Morgen
# Time : 2020/11/20 2:52
# description : 

import sys
from PyQt5.QtWidgets import *
from ui_files.use_method_to_load import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
