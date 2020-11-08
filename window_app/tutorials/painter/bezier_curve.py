# Version : python 3.7.4
# File : bezier_curve.py
# Author : Lila Morgen
# Time : 2020/11/8 18:19
# description : 

import sys
from PyQt5.QtGui import QPainter, QPainterPath
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 380, 250)
        self.setWindowTitle('Bezier curve')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        self.drawBezierCurve(qp)
        qp.end()

    def drawBezierCurve(self, qp):
        path = QPainterPath()
        path.moveTo(30, 30)
        path.cubicTo(30, 30, 200, 350, 350, 30)

        qp.drawPath(path)


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
