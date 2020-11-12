# Author: Lila Morgen
# ProjectName: test
# FileName: label.py
# Date: 2020/11/12
# Description:

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Label')

        lbl = QLabel('Hello')
        lbl.setPixmap(QPixmap('../../icons/named/heart.png'))
        # lbl.setScaledContents(True)  # 缩放标签，使标签填充满窗口
        font = lbl.font()
        font.setPointSize(30)
        lbl.setFont(font)
        lbl.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(lbl)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
