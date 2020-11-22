# Author: Lila Morgen
# ProjectName: test
# FileName: paint_panel.py
# Date: 2020/11/22
# Description:

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
        print(e.x(), e.y(), type(e.y()))
        if self.last_x is None:
            self.last_x = e.x()
            self.last_y = e.y()
            return

        painter = QPainter(self.pixmap())

        painter.begin(self)
        pen = painter.pen()
        pen.setWidth(1)
        pen.setColor(self.pen_color)
        painter.setPen(pen)
        print(self.last_x, self.last_y)

        painter.drawPoint(self.last_x, self.last_x)
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
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Paint Panel')

        self.canvas = Canvas()

        widget = QWidget()
        v_layout = QVBoxLayout()
        v_layout.addWidget(self.canvas)

        palette_layout = QHBoxLayout()
        self.add_palette_button(palette_layout)
        v_layout.addLayout(palette_layout)

        widget.setLayout(v_layout)
        self.setCentralWidget(widget)

    def add_palette_button(self, p):
        for c in COLORS:
            button = QPaletteButton(c)
            button.pressed.connect(lambda x=c: self.canvas.set_pen_color(x))
            p.addWidget(button)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
