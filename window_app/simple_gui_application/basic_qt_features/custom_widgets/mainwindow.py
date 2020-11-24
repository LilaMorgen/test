# Author: Lila Morgen
# ProjectName: test
# FileName: mainwindow.py
# Date: 2020/11/24
# Description:

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from power_bar import PowerBar


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Display Window')

        self.volume = PowerBar()
        self.setCentralWidget(self.volume)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
