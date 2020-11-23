# Author: Lila Morgen
# ProjectName: test
# FileName: mainwindow.py
# Date: 2020/11/23
# Description:

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from custom_widgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Paint Panel')

        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()
        self.stack_layout = QStackedLayout()

        menubar = self.menuBar()
        file_m = menubar.addMenu('File')
        menubar.addSeparator()
        edit_m = menubar.addMenu('Edit')

        toggle_p = QAction('Toggle pen', self)
        toggle_p.setCheckable(True)

        toggle_p.triggered.connect(self.toggle_pen)

        edit_m.addAction(toggle_p)

        for i, canvas in enumerate([LineCanvas(), SprayCanvas()]):
            self.stack_layout.addWidget(canvas)

        v_layout.addLayout(self.stack_layout)

        self.add_palette_button(h_layout)

        v_layout.addLayout(h_layout)

        w = QWidget()
        w.setLayout(v_layout)

        self.setCentralWidget(w)

    def add_palette_button(self, layout):
        for c in COLORS:
            b = QPaletteButton(c)
            b.pressed.connect(lambda x=c: self.stack_layout.currentWidget().set_pen_color(x))
            layout.addWidget(b)

    def toggle_pen(self, e):
        if e is False:
            self.stack_layout.setCurrentIndex(0)
        else:
            self.stack_layout.setCurrentIndex(1)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
