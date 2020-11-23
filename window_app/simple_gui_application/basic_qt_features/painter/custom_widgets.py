# Author: Lila Morgen
# ProjectName: test
# FileName: custom_widgets.py
# Date: 2020/11/23
# Description:

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import random


class LineCanvas(QLabel):
    def __init__(self):
        super(LineCanvas, self).__init__()

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

        self.draw_line(painter, e)

        self.update()

        # 将最后一次鼠标位置传给self.last_x和self.last_y
        self.last_x = e.x()
        self.last_y = e.y()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None

    def draw_line(self, painter, e):
        painter.begin(self)
        pen = painter.pen()
        pen.setWidth(4)
        pen.setColor(self.pen_color)
        painter.setPen(pen)

        painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
        painter.end()


class SprayCanvas(QLabel):
    def __init__(self):
        super(SprayCanvas, self).__init__()

        canvas = QPixmap(700, 300)
        canvas.fill(Qt.white)
        self.setPixmap(canvas)

        # self.last_x, self.last_y = None, None
        self.pen_color = QColor('#000000')

    def set_pen_color(self, c):
        self.pen_color = QColor(c)

    def mouseMoveEvent(self, e):
        painter = QPainter(self.pixmap())

        self.draw_point(painter, e)

        self.update()

    def draw_point(self, painter, e):
        painter.begin(self)
        pen = painter.pen()
        pen.setWidth(1)
        pen.setColor(self.pen_color)
        painter.setPen(pen)

        for i in range(SPRAY_PARTICLES):
            xo = random.gauss(0, SPRAY_DIAMETER)
            yo = random.gauss(0, SPRAY_DIAMETER)
            painter.drawPoint(QPointF(e.x() + xo, e.y() + yo))

        painter.end()


SPRAY_PARTICLES = 100
SPRAY_DIAMETER = 10

COLORS = ['#000000', '#141923', '#414168', '#3a7fa7', '#35e3e3', '#8fd970', '#5ebb49',
          '#458352', '#dcd37b', '#fffee5', '#ffd035', '#cc9245', '#a15c3e', '#a42f3b',
          '#f45b7a', '#c24998', '#81588d', '#bcb0c2', '#ffffff']


class QPaletteButton(QPushButton):
    def __init__(self, color):
        super(QPaletteButton, self).__init__()

        self.setFixedSize(QSize(24, 24))
        self.color = color
        self.setStyleSheet('background-color: %s;' % color)
