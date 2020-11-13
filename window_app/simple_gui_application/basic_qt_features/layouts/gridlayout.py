# Version : python 3.7.4
# File : gridlayout.py
# Author : Lila Morgen
# Time : 2020/11/13 11:08
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
        self.setWindowTitle('Grid Layout')

        grid_layout = QGridLayout()

        grid_layout.addWidget(Color('red'), 0, 0)
        grid_layout.addWidget(Color('green'), 1, 0)
        grid_layout.addWidget(Color('blue'), 1, 1)
        grid_layout.addWidget(Color('purple'), 2, 1)

        widget = QWidget()
        widget.setLayout(grid_layout)

        self.setCentralWidget(widget)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
