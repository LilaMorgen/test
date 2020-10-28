# Version : python 3.7.4
# File : custom_signal.py
# Author : Lila Morgen
# Time : 2020/10/28 20:13
# description : 

import sys
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow


class Communicate(QObject):
    # 创建一个信号对象
    close_app = pyqtSignal()


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.c = Communicate()
        # 将信号与槽相连
        self.c.close_app.connect(self.close)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Custom Signal')
        self.show()

    def mouseMoveEvent(self, event):
        # 信号接收鼠标移动事件，当点击窗口时，发送信号
        self.c.close_app.emit()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
