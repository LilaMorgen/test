# Version : python 3.7.4
# File : slider.py
# Author : Lila Morgen
# Time : 2020/11/3 19:29
# description : 

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 创建滑条对象
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 200, 30)
        # 将滑条数字信号与槽相连
        sld.valueChanged[int].connect(self.change_value)

        # 创建标签对象，并设置图像标签
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('../../../images/mute.png'))
        self.label.setGeometry(250, 40, 30, 30)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Slider')
        self.show()

    def change_value(self, value):
        # 根据数字信号的不同，设置不同图像标签
        if value == 0:
            self.label.setPixmap(QPixmap('../../../images/mute.png'))
        elif 0 < value <= 30:
            self.label.setPixmap(QPixmap('../../../images/volume_min.png'))
        elif 30 < value <= 80:
            self.label.setPixmap(QPixmap('../../../images/volume_mid.png'))
        else:
            self.label.setPixmap(QPixmap('../../../images/volume_max.png'))


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
