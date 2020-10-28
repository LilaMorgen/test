# Version : python 3.7.4
# File : event_sender.py
# Author : Lila Morgen
# Time : 2020/10/28 19:55
# description : 

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        btn1 = QPushButton('Button1', self)
        btn1.move(30, 90)

        btn2 = QPushButton('Button2', self)
        btn2.move(150, 90)

        btn1.clicked.connect(self.button_clicked)
        btn2.clicked.connect(self.button_clicked)

        self.statusBar()

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Event Sender')
        self.show()

    def button_clicked(self):
        # 获取信号发送者
        sender = self.sender()
        # 在状态栏展示信息
        self.statusBar().showMessage(sender.text() + ' was pressed')


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
