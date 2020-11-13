# Version : python 3.7.4
# File : line_edit.py
# Author : Lila Morgen
# Time : 2020/11/13 8:44
# description : 

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Line Edit')

        line_edit = QLineEdit(self)
        # 设置行编辑的最大字符长度
        line_edit.setMaxLength(10)
        # 设置提示词
        line_edit.setPlaceholderText('Enter your Text')

        # 设置行编辑为只读
        # line_edit.setReadOnly(True)

        # 信号.returnPressed是接收回车信号
        line_edit.returnPressed.connect(self.return_pressed)
        # 信号.selectionChanged是接收鼠标选中的文本信号
        line_edit.selectionChanged.connect(self.selection_changed)
        # 信号.textChanged是接收文本改变信号
        line_edit.textChanged.connect(self.text_changed)
        # 信号。textEdited是接收文本编辑信号
        line_edit.textEdited.connect(self.text_edit)

        self.setCentralWidget(line_edit)
        print(self.centralWidget())

    def return_pressed(self):
        print('Return Pressed')
        # 设置行编辑部件文本
        self.centralWidget().setText('BOOM!')

    def selection_changed(self):
        print('Selection Changed')
        print(self.centralWidget().selectedText())

    def text_changed(self, text):
        print('Text changed...')
        print(text)

    def text_edit(self, text):
        print('Text edited...')
        print(text)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
