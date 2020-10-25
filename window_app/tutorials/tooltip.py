# Version : python 3.7.4
# File : tooltip.py
# Author : Lila Morgen
# Time : 2020/10/25 15:17
# description : 

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton
from PyQt5.QtGui import QFont


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 设置工具提示字体和字号
        QToolTip.setFont(QFont('SansSerif', 10))
        # 创建工具提示
        self.setToolTip('This is a <b>QWidget</b> widget.')

        # 创建按钮
        btn = QPushButton('Button', self)
        # 设置按钮提示
        btn.setToolTip('This is a <b>QPushButton</b> widget.')
        # 设置按钮大小,使用默认大小sizeHint()
        btn.resize(btn.sizeHint())
        # 设置按钮位置
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('ToolTip')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
