# Author: Lila Morgen
# ProjectName: test
# FileName: listbox.py
# Date: 2020/11/12
# Description:

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **  kwargs)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('ListBox')

        list_widget = QListWidget(self)
        list_widget.addItems(['One', 'Two', 'Three'])

        list_widget.currentItemChanged.connect(self.index_changed)
        list_widget.currentTextChanged.connect(self.text_changed)

    def index_changed(self, index):
        print(index)  # QListWidgetItem object
        print(index.text())

    def text_changed(self, text):
        print(text)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
