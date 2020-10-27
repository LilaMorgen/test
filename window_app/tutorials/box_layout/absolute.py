# Version : python 3.7.4
# File : absolute.py
# Author : Lila Morgen
# Time : 2020/10/27 12:41
# description : 

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        lal1 = QLabel('Lila Morgen', self)
        lal1.move(15, 10)

        lal2 = QLabel('Tutorials', self)
        lal2.move(35, 40)

        lal3 = QLabel('For PyQt5', self)
        lal3.move(55, 70)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Absolute')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
