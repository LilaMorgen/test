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
        # from random import randint, choice
        # colors = ['#FFD141', '#376F9F', '#0D1F2D', '#E9EBEF', '#EB5160']
        # painter = QPainter(self.label.pixmap())
        # pen = QPen()
        # pen.setWidth(3)
        # painter.setPen(pen)
        #
        # for i in range(10000):
        #     # pen = painter.pen()
        #     pen.setColor(QColor(choice(colors)))
        #     painter.setPen(pen)
        #     painter.drawPoint(200+randint(-100, 100), 150+randint(-100, 100))
        #
        # painter.end()

        # step3
        # from random import randint
        # painter = QPainter(self.label.pixmap())
        # pen = QPen()
        # pen.setWidth(15)
        # pen.setColor(QColor('blue'))
        # painter.setPen(pen)
        # painter.drawLine(QPoint(100, 100), QPoint(300, 200))
        # painter.end()

        # step4
        # from random import randint
        # painter = QPainter(self.label.pixmap())
        # pen = QPen()
        # pen.setWidth(3)
        # pen.setColor(QColor('#EB5160'))
        # painter.setPen(pen)
        #
        # brush = QBrush()
        # brush.setColor(QColor('#FFD141'))
        # brush.setStyle(Qt.Dense1Pattern)
        # painter.setBrush(brush)

        # painter.drawRect(50, 50, 100, 100)
        # painter.drawRect(60, 60, 150, 100)
        # painter.drawRect(70, 70, 100, 150)
        # painter.drawRect(80, 80, 150, 100)
        # painter.drawRect(90, 90, 100, 150)
        # painter.drawRects(QRect(50, 50, 100, 100),
        #                   QRect(60, 60, 150, 100),
        #                   QRect(70, 70, 100, 150),
        #                   QRect(80, 80, 150, 100),
        #                   QRect(90, 90, 100, 150))
        # painter.end()

        # step5
        # from random import randint
        # painter = QPainter(self.label.pixmap())
        # pen = QPen()
        # pen.setWidth(3)
        # pen.setColor(QColor('#EB5160'))
        # painter.setPen(pen)
        # painter.drawRoundedRect(40, 40, 100, 100, 10, 10)
        # painter.drawRoundedRect(80, 80, 100, 100, 10, 50)
        # painter.drawRoundedRect(120, 120, 100, 100, 50, 10)
        # painter.drawRoundedRect(160, 160, 100, 100, 50, 50)
        # painter.end()

        # step6
        # from random import randint
        # painter = QPainter(self.label.pixmap())
        # pen = QPen()
        # pen.setWidth(3)
        # pen.setColor(QColor(204, 0, 0))
        # painter.setPen(pen)
        # painter.drawEllipse(10, 10, 100, 100)
        # painter.drawEllipse(10, 10, 150, 200)
        # painter.drawEllipse(10, 10, 200, 300)
        # painter.end()

        # step7
        from random import randint
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor(204, 0, 0))
        painter.setPen(pen)

        # brush = QBrush()
        # brush.setColor(QColor('#FFD141'))
        # # brush.setStyle(Qt.Dense1Pattern)
        # brush.setStyle(Qt.SolidPattern)
        # painter.setBrush(brush)

        painter.drawEllipse(QPoint(100, 100), 10, 10)
        painter.drawEllipse(QPoint(100, 100), 15, 20)
        painter.drawEllipse(QPoint(100, 100), 20, 25)
        painter.drawEllipse(QPoint(100, 100), 25, 30)
        painter.drawEllipse(QPoint(100, 100), 30, 35)
        painter.end()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
