# Author: Lila Morgen
# ProjectName: test
# FileName: signals_and_slots.py
# Date: 2020/11/11
# Description:

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.windowTitleChanged.connect(self.onWindowTitleChanged)

        self.windowTitleChanged.connect(lambda x: self.my_custom_fn())

        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x))

        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x, 25))

        self.setWindowTitle('My Awesome App')
        self.setGeometry(300, 300, 300, 220)

        lbl = QLabel('This is Awesome!!!')
        lbl.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(lbl)

        toolbar = QToolBar('My Main Toolbar')
        # 设置工具栏图标大小
        self.setIconSize(QSize(16, 16))
        # 设置工具栏按钮风格
        self.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.addToolBar(toolbar)

        statusbar = QStatusBar(self)
        self.setStatusBar(statusbar)

        button_action = QAction(QIcon('../icons/16/045.png'),  'Home', self)
        button_action.setStatusTip('This is action.')
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(QIcon('../icons/named/bug.png'),  'Debug', self)
        button_action2.setStatusTip('This is action.')
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addSeparator()

        toolbar.addWidget(QLabel('Hello'))
        toolbar.addSeparator()
        toolbar.addWidget(QCheckBox())

        menu = self.menuBar()
        file_menu = menu.addMenu('&File')
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        file_menu.addAction(button_action2)


    def onMyToolBarButtonClick(self, s):
        print('click', s)

    def onWindowTitleChanged(self, s):
        print(s)

    def my_custom_fn(self, a='Hello', b=5):
        print(a, b)

    def contextMenuEvent(self, event):
        print('Context menu event.')
        super().contextMenuEvent(event)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
