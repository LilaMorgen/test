# Author: Lila Morgen
# ProjectName: test
# FileName: checkbox.py
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
        self.setWindowTitle('CheckBox')

        checkbox = QCheckBox()
        # 两种设置复选框状态方式(.setChecked() and .setCheckState())
        # 如需设置三态，则也有两种方式(.setTristate() and .setCheckState(Qt.PartiallyChecked))
        checkbox.setChecked(True)
        checkbox.setTristate(True)
        # checkbox.setCheckState(Qt.PartiallyChecked)  # 复选框有三种状态(Qt.Checked, Qt.Unchecked, Qt.PartiallyChecked)

        checkbox.stateChanged.connect(self.show_state)

        self.setCentralWidget(checkbox)

    def show_state(self, state):
        print('state:', state == Qt.Checked)
        print(state)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
