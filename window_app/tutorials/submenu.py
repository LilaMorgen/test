# Version : python 3.7.4
# File : submenu.py
# Author : Lila Morgen
# Time : 2020/10/25 18:10
# description : 

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')

        # 创建一个菜单对象
        imp_menu = QMenu('Import', self)
        # 创建一个操作对象
        imp_act = QAction('Import mail', self)
        # 在菜单对象中添加操作对象
        imp_menu.addAction(imp_act)

        # 创建操作对象
        new_act = QAction('New', self)

        # 在菜单中添加操作对象
        file_menu.addAction(new_act)
        # 在菜单中添加菜单对象
        file_menu.addMenu(imp_menu)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('SubMenu')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
