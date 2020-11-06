# Author: Lila Morgen
# ProjectName: test
# FileName: combobox.py
# Date: 2020/11/6
# Description:

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLabel


class Eample(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 创建标签对象
        self.lbl = QLabel('Ubuntu', self)

        # 创建选择按钮
        combo = QComboBox(self)
        # 添加选项
        combo.addItem('Ubuntu')
        combo.addItem('Mandriva')
        combo.addItem('Fedora')
        combo.addItem('Arch')
        combo.addItem('Gentoo')

        # 将选项信号与槽相连
        combo.activated[str].connect(self.on_activated)

        combo.move(50, 50)
        self.lbl.move(50, 150)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('ComboBox')
        self.show()

    def on_activated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


def main():
    app = QApplication(sys.argv)
    ex = Eample()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
