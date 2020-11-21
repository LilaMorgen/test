# Version : python 3.7.4
# File : signals.py
# Author : Lila Morgen
# Time : 2020/11/20 12:24
# description : 

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Signals')

        layout = QVBoxLayout()

        for n in range(10):
            btn = QPushButton(str(n))
            btn.pressed.connect(lambda x=n: self.my_custom_fn(x))
            layout.addWidget(btn)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def my_custom_fn(self, n):
        print('Button %d was clicked.' % n)


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
