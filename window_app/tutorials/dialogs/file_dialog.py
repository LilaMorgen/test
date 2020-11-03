# Version : python 3.7.4
# File : file_dialog.py
# Author : Lila Morgen
# Time : 2020/11/3 14:00
# description : 

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog
from PyQt5.QtGui import QIcon
from pathlib import Path
import os


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 创建文本编辑对象
        self.text_edit = QTextEdit()
        # 将文本编辑对象放置在窗口中心
        self.setCentralWidget(self.text_edit)
        # 创建状态栏
        self.statusBar()

        # 创建打开文件动作
        open_file = QAction(QIcon('../../../images/open_file.png'), 'Open', self)
        # 为动作设置快捷键
        open_file.setShortcut('Ctrl+O')
        # 为动作设置状态提示
        open_file.setStatusTip('Open New File')
        # 将动作信号与槽相连
        open_file.triggered.connect(self.show_dialog)

        # 创建菜单栏
        menubar = self.menuBar()
        # 在菜单栏上添加菜单
        file_menu = menubar.addMenu('File')
        # 在菜单中添加动作
        file_menu.addAction(open_file)

        self.setGeometry(300, 300, 550, 450)
        self.setWindowTitle('File Dialog')
        self.show()

    def show_dialog(self):
        # 能够解析的后缀名列表
        ends_with = ['.text', '.txt', '.md']
        # 获取家目录
        home_dir = str(Path.home())
        # 创建文件选取对话框获取文件目录名，第一个参数是对话框标题，第二个参数是对话框工作目录
        file_name = QFileDialog.getOpenFileName(self, 'Open File', home_dir)

        if file_name[0]:
            # print(os.path.splitext(file_name[0])[-1], type(os.path.splitext(file_name[0])[-1]))
            # 判断选择的文件的后缀名是否在解析列表中
            # 在则可解析并展示在文本编辑框中
            # 不在则以二进制解析并展示在文本编辑框中
            if os.path.splitext(file_name[0])[-1] in ends_with:
                # print(file_name[0], type(file_name[0]))
                with open(file_name[0], 'r', encoding='utf-8') as f:
                    data = f.read()
                    # print(str(data), type(data))
                    self.text_edit.setText(data)
            else:
                with open(file_name[0], 'rb') as f:
                    data = f.read()
                    # print(str(data), type(data))
                    self.text_edit.setText(str(data))


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
