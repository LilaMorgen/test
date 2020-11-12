# Author: Lila Morgen
# ProjectName: test
# FileName: combobox.py
# Date: 2020/11/12
# Description:

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('ComboBox')

        combobox = QComboBox(self)
        # 在下拉列表框中添加选项
        combobox.addItems(['One', 'Two', 'Three'])
        # 设置可编辑
        combobox.setEditable(True)

        # 设置插入选项模式，默认是在末尾插入
        combobox.setInsertPolicy(QComboBox.InsertAtTop)

        # 设置选项最大数目
        combobox.setMaxCount(5)

        # 默认发送的是index信号
        combobox.currentIndexChanged.connect(self.index_changed)

        # 可以发送文本信号
        combobox.currentIndexChanged[str].connect(self.text_changed)

        # self.setCentralWidget(combobox)

    def index_changed(self, index):
        print(index)

    def text_changed(self, text):
        print(text)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
