# Version : python 3.7.4
# File : hlayout.py
# Author : Lila Morgen
# Time : 2020/11/13 10:32
# description : 

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Color(QWidget):
    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('H Layout')

        h_layout = QHBoxLayout()

        h_layout.addWidget(Color('red'))
        h_layout.addWidget(Color('green'))
        h_layout.addWidget(Color('blue'))

        widget = QWidget()
        widget.setLayout(h_layout)

        self.setCentralWidget(widget)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
