# Version : python 3.7.4
# File : font_dialog.py
# Author : Lila Morgen
# Time : 2020/11/3 13:31
# description : 

import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QVBoxLayout, QPushButton, QLabel,
                             QSizePolicy, QFontDialog)


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 创建垂直布局对象
        v_box = QVBoxLayout()

        # 创建按钮
        btn = QPushButton('Dialog', self)
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        btn.move(20, 20)

        # 在垂直布局中加入按钮
        v_box.addWidget(btn)

        # 将按钮信号与槽相连
        btn.clicked.connect(self.show_dialog)

        # 创建标签
        self.lbl = QLabel('Knowledge only matters', self)
        self.lbl.move(130, 20)

        # 在垂直布局中加入标签
        v_box.addWidget(self.lbl)

        # 在窗口中设置布局
        self.setLayout(v_box)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Font Dialog')
        self.show()

    def show_dialog(self):
        # 接收字体和提交信号
        font, ok = QFontDialog.getFont()
        print(font)

        # 提交信号为True，则将字体应用在标签上
        if ok:
            self.lbl.setFont(font)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
