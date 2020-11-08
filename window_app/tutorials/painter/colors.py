# Version : python 3.7.4
# File : colors.py
# Author : Lila Morgen
# Time : 2020/11/8 17:13
# description : 

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QBrush


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Colors')

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        self.draw_rectangles(p)
        p.end()

    def draw_rectangles(self, p):
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')

        p.setPen(col)

        p.setBrush(QColor(200, 0, 0))
        p.drawRect(10, 15, 90, 60)

        p.setBrush(QColor(255, 80, 0, 160))
        p.drawRect(130, 15, 90, 60)

        p.setBrush(QColor(25, 0, 90, 200))
        p.drawRect(250, 15, 90, 60)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
