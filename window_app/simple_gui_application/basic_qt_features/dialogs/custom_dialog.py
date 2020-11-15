# Version : python 3.7.4
# File : custom_dialog.py
# Author : Lila Morgen
# Time : 2020/11/14 20:46
# description : 

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class CustomDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(CustomDialog, self).__init__(*args, **kwargs)

        self.setWindowTitle('Hello')

        # 创建按钮
        btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        # 将按钮放在按钮盒中
        self.buttonbox = QDialogButtonBox(btn)
        # 将信号与槽相连
        self.buttonbox.accepted.connect(self.accept)
        self.buttonbox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.buttonbox)
        self.setLayout(self.layout)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Custom Dialog')

        action = QAction(QIcon('../../icons/named/compass.png'), 'Dialog', self)
        action.setStatusTip('Create Dialog Box')
        action.triggered.connect(self.showDialog)

        toolbar = QToolBar('My Toolbar')
        self.setIconSize(QSize(16, 16))
        self.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.addToolBar(toolbar)

        toolbar.addAction(action)

    def showDialog(self, s):
        print('Click', s)

        dialog = CustomDialog()
        if dialog.exec_():
            print('Success!')
        else:
            print('Cancel!')


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
