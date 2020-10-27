# Version : python 3.7.4
# File : toolbar.py
# Author : Lila Morgen
# Time : 2020/10/25 21:49
# description : 

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 设置操作
        exit_act = QAction(QIcon('../../../images/eword.ico'), 'Exit', self)
        # 为操作设置快捷键
        exit_act.setShortcut('Ctrl+Q')
        # 将操作信号与槽相连
        exit_act.triggered.connect(qApp.quit)

        # 设置工具栏并命名工具栏，窗口中鼠标右击可选择显示与不显示工具栏
        toolbar = self.addToolBar('Tools')
        # 在工具栏上添加操作
        toolbar.addAction(exit_act)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('ToolBar')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
