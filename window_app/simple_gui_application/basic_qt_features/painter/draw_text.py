# Author: Lila Morgen
# ProjectName: test
# FileName: draw_text.py
# Date: 2020/11/22
# Description:

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Draw Text')

        self.label = QLabel()
        canvas = QPixmap(400, 300)
        canvas.fill(QColor('white'))
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()

    def draw_something(self):
        painter = QPainter(self.label.pixmap())

        pen = QPen()
        pen.setWidth(1)
        pen.setColor(QColor('blue'))
        painter.setPen(pen)

        font = QFont()
        # 设置字体
        font.setFamily('Times')
        # 设置加粗
        font.setBold(True)
        # 设置字体大小
        font.setPointSize(40)
        painter.setFont(font)

        painter.drawText(50, 150, 'Hello World!')
        # drawText(position_x, position_y, width, height, align_ways, text)
        painter.drawText(50, 150, 100, 100, Qt.AlignCenter, 'Hello World!')
        painter.end()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
