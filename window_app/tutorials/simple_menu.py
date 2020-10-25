# Version : python 3.7.4
# File : simple_menu.py
# Author : Lila Morgen
# Time : 2020/10/25 16:54
# description : 

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 创建一个操作，&(表示Alt)
        exit_act = QAction(QIcon('../../images/eword.ico'), '&Exit', self)
        # 为操作创建快捷键
        exit_act.setShortcut('Ctrl+Q')
        # 创建提示，当鼠标指针悬浮在操作上，出现提示
        exit_act.setStatusTip('Exit application')
        # 将信号与槽相连
        exit_act.triggered.connect(qApp.quit)

        self.statusBar()

        # 创建菜单栏
        menubar = self.menuBar()
        # 在菜单栏中添加File菜单
        file_menu = menubar.addMenu('&File')
        # 在File菜单中添加exit_act操作
        file_menu.addAction(exit_act)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Simple Menu')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
