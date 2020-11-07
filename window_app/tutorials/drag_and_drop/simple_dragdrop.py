# Version : python 3.7.4
# File : simple_dragdrop.py
# Author : Lila Morgen
# Time : 2020/11/7 18:26
# description : 

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton


# 创建一个继承QPushButton的按钮类
class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)

        # 接受落下
        self.setAcceptDrops(True)

    # 重写拖拽进入事件
    def dragEnterEvent(self, e):
        # 如果拖拽事件格式是纯文本，就接受事件；反之不接受。
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    # 重写落下事件
    def dropEvent(self, e):
        # 落下，将事件的文本在按钮上显示
        self.setText(e.mimeData().text())


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 创建行编辑对象
        edit = QLineEdit('', self)
        # 设置行编辑对象可以拖拽
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = Button('Button', self)
        button.move(220, 62)

        self.setGeometry(300, 300, 400, 220)
        self.setWindowTitle('Simple Drag and Drop')


def main():
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
