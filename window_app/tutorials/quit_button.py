# Version : python 3.7.4
# File : quit_button.py
# Author : Lila Morgen
# Time : 2020/10/25 15:45
# description : 

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        btn = QPushButton('Quit', self)

        # 信号(btn.clicked)与槽(QApplication.instance().quit)相连
        btn.clicked.connect(QApplication.instance().quit)

        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Quit Button')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
