# Version : python 3.7.4
# File : runwindow.py
# Author : Lila Morgen
# Time : 2020/9/15 10:05
# description : 

import sys
from window_app import demo
from PyQt5.QtWidgets import QApplication, QMainWindow


def main():
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    ui = demo.Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
