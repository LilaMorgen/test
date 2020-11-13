# Version : python 3.7.4
# File : stackedlayout.py
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
        self.setWindowTitle('Stacked Layout')

        stacked_layout = QStackedLayout()
        button_layout = QHBoxLayout()
        page_layout = QVBoxLayout()

        # stacked_layout.addWidget(Color('red'))
        # stacked_layout.addWidget(Color('green'))
        # stacked_layout.addWidget(Color('blue'))
        # stacked_layout.addWidget(Color('purple'))
        #
        # stacked_layout.setCurrentIndex(1)

        page_layout.addLayout(button_layout)
        page_layout.addLayout(stacked_layout)

        colors = ['red', 'green', 'blue', 'purple', 'pink']
        for n, color in enumerate(colors):
            stacked_layout.addWidget(Color(color))

            btn = QPushButton(color)
            btn.pressed.connect(lambda i=n: stacked_layout.setCurrentIndex(i))
            button_layout.addWidget(btn)

        widget = QWidget()
        widget.setLayout(page_layout)

        self.setCentralWidget(widget)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
