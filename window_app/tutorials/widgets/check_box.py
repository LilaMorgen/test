# Version : python 3.7.4
# File : check_box.py
# Author : Lila Morgen
# Time : 2020/11/3 18:40
# description : 

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 创建复选框对象
        cb = QCheckBox('Show Title', self)
        cb.move(20, 20)
        # 选中复选框
        cb.toggle()
        # 将复选框信号与槽相连
        cb.stateChanged.connect(self.change_title)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Check Box')
        self.show()

    def change_title(self, state):
        # 如果信号是Qt.Checked就显示窗口标题，否则不显示
        if state == Qt.Checked:
            self.setWindowTitle('Check Box')
        else:
            self.setWindowTitle(' ')


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
