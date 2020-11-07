# Version : python 3.7.4
# File : drag_button.py
# Author : Lila Morgen
# Time : 2020/11/7 20:30
# description : 

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag


class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)

    def mouseMoveEvent(self, e):
        if e.buttons() != Qt.RightButton:
            return
        mimedata = QMimeData()

        drag = QDrag(self)
        drag.setMimeData(mimedata)
        # drag.setHotSpot(e.pos() - self.rect().topLeft())

        drag_action = drag.exec_(Qt.MoveAction)

    def mousePressEvent(self, e):
        super().mousePressEvent(e)

        if e.button() == Qt.LeftButton:
            print('Press')


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setAcceptDrops(True)

        self.button = Button('Button', self)
        self.button.move(100, 65)

        self.setGeometry(300, 300, 500, 450)
        self.setWindowTitle('Drag Button')

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        position = e.pos()
        self.button.move(position)

        e.setDropAction(Qt.MoveAction)
        e.accept()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
