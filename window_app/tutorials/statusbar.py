# Version : python 3.7.4
# File : statusbar.py
# Author : Lila Morgen
# Time : 2020/10/25 16:43
# description : 

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 设置状态栏并且设置状态栏消息，消息显示5秒
        self.statusBar().showMessage('Ready', 5000)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Status Bar')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
