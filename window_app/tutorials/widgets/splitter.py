# Author: Lila Morgen
# ProjectName: test
# FileName: splitter.py
# Date: 2020/11/6
# Description:

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSplitter, QHBoxLayout, QFrame
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 创建水平布局
        h_box = QHBoxLayout(self)

        # 创建左上角、右上角和底部框架对象
        top_left = QFrame(self)
        top_right = QFrame(self)
        bottom = QFrame(self)

        # 设置三个框架样式，以看见框架边界
        top_left.setFrameStyle(QFrame.StyledPanel)
        top_right.setFrameStyle(QFrame.StyledPanel)
        bottom.setFrameStyle(QFrame.StyledPanel)

        # 创建水平分割器对象， 并将两个框架添加进分割器中
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(top_left)
        splitter1.addWidget(top_right)

        # 创建垂直分割器对象，将第一个分割器与底部框架添加进分割器中
        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        # 将第二个分割器添加进水平布局中
        h_box.addWidget(splitter2)
        self.setLayout(h_box)

        self.setGeometry(300, 300, 450, 400)
        self.setWindowTitle('Splitter')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
