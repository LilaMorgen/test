# Version : python 3.7.4
# File : icon.py
# Author : Lila Morgen
# Time : 2020/10/25 13:54
# description : 

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):
    def __init__(self):
        super().__init__()

        # GUI创建
        self.init_ui()

    def init_ui(self):
        # 定位窗口和设置窗口大小,参数(x,y,w,h)
        self.setGeometry(300, 300, 300, 220)
        # 设置窗口标题
        self.setWindowTitle('Icon')
        # 设置窗口图标
        self.setWindowIcon(QIcon('../../../images/eword.ico'))
        # 显示窗口
        self.show()


def main():
    # 创建应用对象
    app = QApplication(sys.argv)
    # 创建小部件/窗口
    ex = Example()
    # 应用循环，创建出口
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
