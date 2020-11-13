# Version : python 3.7.4
# File : tabs_widget.py
# Author : Lila Morgen
# Time : 2020/11/13 12:20
# description : 

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Color(QWidget):
    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Tabs Widget')

        tabs = QTabWidget()
        # 打开文档模式，在MAC上可显示更小标签，Window上不变
        tabs.setDocumentMode(True)
        # 设置标签集部件位置
        tabs.setTabPosition(QTabWidget.North)
        # 方向键可切换标签
        tabs.setMovable(True)

        colors = ['red', 'green', 'blue', 'purple', 'pink']
        for n, color in enumerate(colors):
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
