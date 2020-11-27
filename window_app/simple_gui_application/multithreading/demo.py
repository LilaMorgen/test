# Author: Lila Morgen
# ProjectName: test
# FileName: demo.py
# Date: 2020/11/27
# Description:

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import time


class MainWindow(QMainWindow):
    def __init__(self,*args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('Demo Multithreading')
        self.init_ui()

    def init_ui(self):
        self.counter = 0

        v_layout = QVBoxLayout()

        self.lbl = QLabel('Start')
        self.btn = QPushButton('Danger')
        self.btn.pressed.connect(self.oh_on)

        self.btn2 = QPushButton('?')
        self.btn2.pressed.connect(self.change_message)

        v_layout.addWidget(self.lbl)
        v_layout.addWidget(self.btn)
        v_layout.addWidget(self.btn2)

        widget = QWidget(self)
        widget.setLayout(v_layout)

        self.setCentralWidget(widget)

        # self.timer = QTimer()
        # self.timer.setInterval(1000)
        # self.timer.timeout.connect(self.recurring_timer)
        # self.timer.start()

    def oh_on(self):
        self.message = 'Pressed'
        for n in range(1000):
            time.sleep(0.1)
            self.lbl.setText(self.message)
            QApplication.processEvents()

    def change_message(self):
        self.message = 'OH_ON'

    # def recurring_timer(self):
    #     self.counter += 1
    #     self.lbl.setText('Counter: %d' % self.counter)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
