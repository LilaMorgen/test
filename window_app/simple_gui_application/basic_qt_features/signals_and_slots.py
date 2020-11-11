# Author: Lila Morgen
# ProjectName: test
# FileName: signals_and_slots.py
# Date: 2020/11/11
# Description:

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.windowTitleChanged.connect(self.onWindowTitleChanged)

        self.windowTitleChanged.connect(lambda x: self.my_custom_fn())

        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x))

        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x, 25))

        self.setWindowTitle('My Awesome App')
        lbl = QLabel('This is Awesome!!!')
        lbl.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(lbl)

    def onWindowTitleChanged(self, s):
        print(s)

    def my_custom_fn(self, a='Hello', b=5):
        print(a, b)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
