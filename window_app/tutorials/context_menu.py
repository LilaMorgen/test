# Version : python 3.7.4
# File : context_menu.py
# Author : Lila Morgen
# Time : 2020/10/25 21:18
# description : 

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, qApp


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Context Menu')
        self.show()

    def contextMenuEvent(self, event):
        c_menu = QMenu(self)

        new_act = c_menu.addAction('New')
        open_act = c_menu.addAction('Open')
        quit_act = c_menu.addAction('Quit')

        # 右击呼出文本菜单
        # 捕捉鼠标事件坐标将其转化为全局坐标
        action = c_menu.exec_(self.mapFromGlobal(event.pos()))

        # 操作是否为退出操作
        if action == quit_act:
            qApp.quit()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
