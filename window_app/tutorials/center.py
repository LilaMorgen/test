# Version : python 3.7.4
# File : center.py
# Author : Lila Morgen
# Time : 2020/10/25 16:24
# description : 

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.resize(300, 220)
        self.center()

        self.setWindowTitle('Center')
        self.show()

    def center(self):
        # 设置一个矩形框架
        qr = self.frameGeometry()
        # 获取显示屏分辨率,从分辨率中得到屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 将矩形框架中心放在屏幕中心
        qr.moveCenter(cp)
        # 将窗口左上角移到矩形框架的左上角
        self.move(qr.topLeft())


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
