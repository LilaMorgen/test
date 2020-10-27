# Version : python 3.7.4
# File : review.py
# Author : Lila Morgen
# Time : 2020/10/27 13:24
# description : 

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 设置标签对象
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        # 设置行编辑组件对象和文本编辑组件对象
        title_edit = QLineEdit()
        author_edit = QLineEdit()
        review_edit = QTextEdit()

        # 设置网格布局
        grid = QGridLayout()
        # 设置网格数
        grid.setSpacing(10)

        # 在网格布局指定位置中添加标签对象和编辑对象
        # 网格布局中行是从1开始数起，列是从0开始数起
        grid.addWidget(title, 1, 0)
        grid.addWidget(title_edit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(author_edit, 2, 1)

        grid.addWidget(review, 3, 0)
        # 可以确定编辑组件跨网格范围，由3行1列到5行1列
        grid.addWidget(review_edit, 3, 1, 5, 1)

        # 在窗口中设置网格布局
        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
