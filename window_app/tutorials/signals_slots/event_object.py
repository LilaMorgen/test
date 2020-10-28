# Version : python 3.7.4
# File : event_object.py
# Author : Lila Morgen
# Time : 2020/10/28 19:11
# description : 

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()

        x = 0
        y = 0

        # 设置标签小部件显示x,y坐标
        self.text = f'x:{x}, y:{y}'
        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        # 启用鼠标跟踪，默认是未启用，未启用则需按一下鼠标才会收到鼠标移动事件
        self.setMouseTracking(True)

        self.setLayout(grid)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Event and Object')
        self.show()

    def mouseMoveEvent(self, event):
        # 获取鼠标位置的x,y坐标
        x = event.x()
        y = event.y()

        # 设置文本，并在标签上将该文本显示
        text = f'x:{x}, y:{y}'
        self.label.setText(text)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
