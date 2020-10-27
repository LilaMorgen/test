# Version : python 3.7.4
# File : box_layout.py
# Author : Lila Morgen
# Time : 2020/10/27 10:52
# description : 

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QHBoxLayout, QVBoxLayout


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        v_widget = QWidget(self)
        v_widget.setGeometry(100, 100, 200, 120)
        ok_button = QPushButton('OK', v_widget)
        cancel_button = QPushButton('Cancel', v_widget)

        h_box = QHBoxLayout()
        h_box.addStretch(1)
        h_box.addWidget(ok_button)
        h_box.addWidget(cancel_button)

        v_box = QVBoxLayout(v_widget)
        v_box.addStretch(1)
        v_box.addLayout(h_box)

        v_widget.setLayout(v_box)
        # self.setLayout(v_widget)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Box Layout')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
