# Version : python 3.7.4
# File : test.py
# Author : Lila Morgen
# Time : 2020/11/22 23:05
# description : 

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Canvas(QLabel):
    def __init__(self):
        super(Canvas, self).__init__()

        canvas = QPixmap(700, 300)
        canvas.fill(Qt.white)
        self.setPixmap(canvas)

        self.last_x, self.last_y = None, None
        self.pen_color = QColor('#000000')

    def set_pen_color(self, c):
        self.pen_color = QColor(c)

    def mouseMoveEvent(self, e):
        if self.last_x is None:
            self.last_x = e.x()
            self.last_y = e.y()
            return

        painter = QPainter(self.pixmap())

        painter.begin(self)
        pen = painter.pen()
        pen.setWidth(4)
        pen.setColor(self.pen_color)
        painter.setPen(pen)

        painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
        painter.end()
        self.update()

        # 将最后一次鼠标位置传给self.last_x和self.last_y
        self.last_x = e.x()
        self.last_y = e.y()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None


COLORS = ['#000000', '#141923', '#414168', '#3a7fa7', '#35e3e3', '#8fd970', '#5ebb49',
          '#458352', '#dcd37b', '#fffee5', '#ffd035', '#cc9245', '#a15c3e', '#a42f3b',
          '#f45b7a', '#c24998', '#81588d', '#bcb0c2', '#ffffff']


class QPaletteButton(QPushButton):
    def __init__(self, color):
        super(QPaletteButton, self).__init__()

        self.setFixedSize(QSize(24, 24))
        self.color = color
        self.setStyleSheet('background-color: %s;' % color)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Test')

        self.canvas = Canvas()
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        v_layout.addWidget(self.canvas)

        self.add_palette_button(h_layout)

        v_layout.addLayout(h_layout)

        w = QWidget()
        w.setLayout(v_layout)

        self.setCentralWidget(w)

    def add_palette_button(self, layout):
        for c in COLORS:
            b = QPaletteButton(c)
            b.pressed.connect(lambda x=c: self.canvas.set_pen_color(x))
            layout.addWidget(b)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
