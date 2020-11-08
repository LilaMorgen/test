# Version : python 3.7.4
# File : pens.py
# Author : Lila Morgen
# Time : 2020/11/8 17:29
# description : 

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300,350, 300)
        self.setWindowTitle('Pens')

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        self.draw_lines(p)
        p.end()

    def draw_lines(self, p):
        pen = QPen(Qt.black, 2, Qt.SolidLine)

        p.setPen(pen)
        p.drawLine(20, 40, 250, 40)

        pen.setStyle(Qt.DashLine)
        p.setPen(pen)
        p.drawLine(20, 80, 250, 80)

        pen.setStyle(Qt.DotLine)
        p.setPen(pen)
        p.drawLine(20, 120, 250, 120)

        pen.setStyle(Qt.DashDotLine)
        p.setPen(pen)
        p.drawLine(20, 160, 250, 160)

        pen.setStyle(Qt.DashDotDotLine)
        p.setPen(pen)
        p.drawLine(20, 200, 250, 200)

        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1, 4, 5, 4])
        p.setPen(pen)
        p.drawLine(20, 240, 250, 240)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
