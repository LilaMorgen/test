# Version : python 3.7.4
# File : color_dialog.py
# Author : Lila Morgen
# Time : 2020/10/29 13:48
# description : 

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame, QColorDialog
from PyQt5.QtGui import QColor


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 创建一个颜色对象，设置其初始值(r,g,b)
        col = QColor(0, 0, 0)

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.show_dialog)

        # 设置框架对象
        self.frm = QFrame(self)
        # 在框架中设置风格背景样式
        self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())
        # 设置框架位置
        self.frm.setGeometry(130, 22, 200, 200)

        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('Color Dialog')
        self.show()

    def show_dialog(self):
        # 创建颜色选择对话框
        col = QColorDialog.getColor()
        print(col.name())

        # 颜色有效，则在框架中展示
        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
