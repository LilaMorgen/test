# Version : python 3.7.4
# File : signals_slots.py
# Author : Lila Morgen
# Time : 2020/10/28 18:38
# description : Slider and lcdNumber

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QSlider, QVBoxLayout


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 创建lcd数字面板对象
        lcd = QLCDNumber(self)
        # 创建水平滑块条对象，如果不传入参数Qt.Horizontal,那么滑块条默认是垂直布置
        sld = QSlider(Qt.Horizontal, self)

        # 创建垂直布局，并在布局中加入上面两个对象
        v_box = QVBoxLayout()
        v_box.addWidget(lcd)
        v_box.addWidget(sld)

        self.setLayout(v_box)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Signals and Slots')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
