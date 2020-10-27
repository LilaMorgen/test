# Version : python 3.7.4
# File : main_window.py
# Author : Lila Morgen
# Time : 2020/10/25 22:10
# description : 

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QTextEdit
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 创建文本输入对象
        text_edit = QTextEdit()
        # 将其放在窗口中心位置
        self.setCentralWidget(text_edit)

        # 创建操作
        exit_act = QAction(QIcon('../../../images/eword.ico'), 'Exit', self)
        # 设置操作快捷键
        exit_act.setShortcut('Ctrl+Q')
        # 设置鼠标悬浮于操作上时的状态提示
        exit_act.setStatusTip('Exit application')
        # 将操作信号于槽相连
        exit_act.triggered.connect(self.close)

        # 创建状态栏
        self.statusBar()

        # 创建菜单栏
        menubar = self.menuBar()
        # 在菜单栏中添加菜单
        file_menu = menubar.addMenu('File')
        # 在菜单中添加操作
        file_menu.addAction(exit_act)

        # 创建工具栏
        toolbar = self.addToolBar('Tools')
        # 在工具栏中添加操作
        toolbar.addAction(exit_act)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Main Window')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
