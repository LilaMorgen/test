# Version : python 3.7.4
# File : reimplement_handler.py
# Author : Lila Morgen
# Time : 2020/10/28 18:59
# description : 

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('ReImplement Handler')
        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
