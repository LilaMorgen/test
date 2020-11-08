# Version : python 3.7.4
# File : draw_points.py
# Author : Lila Morgen
# Time : 2020/11/8 17:00
# description : 

import sys, random
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Draw Points')

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        self.draw_points(p)
        p.end()

    def draw_points(self, p):
        p.setPen(Qt.red)
        size = self.size()

        if size.height() <= 1 or size.width() <= 1:
            return

        for i in range(1000):
            x = random.randint(1, size.width() - 1)
            y = random.randint(1, size.height() - 1)
            p.drawPoint(x, y)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
