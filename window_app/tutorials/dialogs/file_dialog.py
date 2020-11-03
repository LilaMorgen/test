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
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)
        self.statusBar()

        open_file = QAction(QIcon('../../../images/open_file.png'), 'Open', self)
        open_file.setShortcut('Ctrl+O')
        open_file.setStatusTip('Open New File')
        open_file.triggered.connect(self.show_dialog)

        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        file_menu.addAction(open_file)

        self.setGeometry(300, 300, 550, 450)
        self.setWindowTitle('File Dialog')
        self.show()

    def show_dialog(self):
        ends_with = ['.text', '.txt', '.md']
        home_dir = str(Path.home())
        file_name = QFileDialog.getOpenFileName(self, 'Open File', home_dir)

        if file_name[0]:
            # print(os.path.splitext(file_name[0])[-1], type(os.path.splitext(file_name[0])[-1]))
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
