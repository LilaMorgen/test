# Version : python 3.7.4
# File : check_menu.py
# Author : Lila Morgen
# Time : 2020/10/25 18:33
# description : 

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        statusbar = self.statusBar()
        statusbar.showMessage('Ready')

        menubar = self.menuBar()
        view_menu = menubar.addMenu('View')

        view_stat_act = QAction('View statusbar', self, checkable=True)
        view_stat_act.setStatusTip('View statusbar')
        view_stat_act.setChecked(True)
        view_stat_act.triggered.connect(self.toggle_menu)

        view_menu.addAction(view_stat_act)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Check Menu')
        self.show()

    def toggle_menu(self, state):
        print(state)
        if state:
            self.statusBar().show()
        else:
            # self.statusbar.hide()
            # 运行进入这就抛出Process finished with exit code -1073740791 (0xC0000409)
            # 未解决问题所在

            # 正确解决如下，将statusbar改为statusBar()
            self.statusBar().hide()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
