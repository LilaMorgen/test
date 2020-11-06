# Author: Lila Morgen
# ProjectName: test
# FileName: pixmap.py
# Date: 2020/11/6
# Description:

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel
from PyQt5.QtGui import QPixmap


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 创建水平布局
        h_box = QHBoxLayout(self)

        # 创建标签对象
        self.lbl = QLabel(self)

        # 获取像素图片
        pixmap = QPixmap('../../../images/sound.png')
        # 将像素图片设置在标签上
        self.lbl.setPixmap(pixmap)

        # 在水平布局中加入标签对象
        h_box.addWidget(self.lbl)
        # 在窗口中放置水平布局
        self.setLayout(h_box)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('PixMap')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
