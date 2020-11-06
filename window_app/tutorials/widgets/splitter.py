# Author: Lila Morgen
# ProjectName: test
# FileName: splitter.py
# Date: 2020/11/6
# Description:

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSplitter, QHBoxLayout, QFrame
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        h_box = QHBoxLayout(self)

        top_left = QFrame(self)
        top_right = QFrame(self)
        bottom = QFrame(self)

        top_left.setFrameStyle(QFrame.StyledPanel)
        top_right.setFrameStyle(QFrame.StyledPanel)
        bottom.setFrameStyle(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(top_left)
        splitter1.addWidget(top_right)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        h_box.addWidget(splitter2)
        self.setLayout(h_box)

        self.setGeometry(300, 300, 450, 400)
        self.setWindowTitle('Splitter')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
