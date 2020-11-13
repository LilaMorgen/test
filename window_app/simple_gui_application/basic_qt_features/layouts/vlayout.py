# Version : python 3.7.4
# File : vlayout.py
# Author : Lila Morgen
# Time : 2020/11/13 10:07
# description : 

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Color(QWidget):
    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        # 填充背景
        self.setAutoFillBackground(True)

        # 获取当前调色板
        palette = self.palette()
        # 对窗口调色板设置颜色
        palette.setColor(QPalette.Window, QColor(color))
        # 应用更新的调色板
        self.setPalette(palette)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('V Layout')

        v_layout = QVBoxLayout()

        color_widget = Color('red')
        v_layout.addWidget(color_widget)
        v_layout.addWidget(Color('green'))
        v_layout.addWidget(Color('blue'))

        widget = QWidget()
        widget.setLayout(v_layout)

        self.setCentralWidget(widget)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
