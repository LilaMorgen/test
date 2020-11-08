# Version : python 3.7.4
# File : draw_text.py
# Author : Lila Morgen
# Time : 2020/11/8 11:56
# description : 

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QFont


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.text = '你是谁？'

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Draw Text')

    def paintEvent(self, e):
        # 创建画笔对象
        p = QPainter()
        # 在窗口上启动画笔
        p.begin(self)
        # 调用绘制函数
        self.draw_text(e, p)
        # 关闭画笔
        p.end()

    def draw_text(self, e, p):
        # 设置画笔颜色
        p.setPen(QColor(168, 34, 3))
        # 设置画笔字体与大小
        p.setFont(QFont('Decorative', 10))
        # 绘制文本drawText(画框大小， 绘制位置， 绘制内容)
        p.drawText(e.rect(), Qt.AlignCenter, self.text)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
