# Version : python 3.7.4
# File : qpainter.py
# Author : Lila Morgen
# Time : 2020/11/21 10:29
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
        self.setWindowTitle('QPainter')

        self.label = QLabel()
        # self.label.setText('123')
        canvas = QPixmap(400, 300)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()

    def draw_something(self):
        # step1
        # painter = QPainter(self.label.pixmap())
        # painter.begin(self)
        # pen = QPen()
        # pen.setWidth(40)
        # pen.setColor(QColor('red'))
        # painter.setPen(pen)
        # # painter.drawLine(10, 10, 300, 200)
        # painter.drawPoint(200, 150)
        # painter.end()

        # step2
        from random import randint, choice
        colors = ['#FFD141', '#376F9F', '#0D1F2D', '#E9EBEF', '#EB5160']
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(3)
        painter.setPen(pen)

        for i in range(10000):
            # pen = painter.pen()
            pen.setColor(QColor(choice(colors)))
            painter.setPen(pen)
            painter.drawPoint(200+randint(-100, 100), 150+randint(-100, 100))

        painter.end()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
