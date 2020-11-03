# Version : python 3.7.4
# File : toggle_button.py
# Author : Lila Morgen
# Time : 2020/11/3 18:58
# description : 

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame
from PyQt5.QtGui import QColor


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.col = QColor(0, 0, 0)

        red_btn = QPushButton('Red', self)
        red_btn.setCheckable(True)
        red_btn.move(10, 10)

        red_btn.clicked[bool].connect(self.set_color)

        green_btn = QPushButton('Green', self)
        green_btn.setCheckable(True)
        green_btn.move(10, 60)

        green_btn.clicked[bool].connect(self.set_color)

        blue_btn = QPushButton('Blue', self)
        blue_btn.setCheckable(True)
        blue_btn.move(10, 110)

        blue_btn.clicked[bool].connect(self.set_color)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet('QWidget {background-color: %s}'
                                  % self.col.name())

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Toggle Button')
        self.show()

    def set_color(self, pressed):
        source = self.sender()

        if pressed:
            val = 255
        else:
            val = 0

        if source.text() == 'Red':
            self.col.setRed(val)
        elif source.text() == 'Green':
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)

        self.square.setStyleSheet('QWidget {background-color: %s}'
                                  % self.col.name())


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
