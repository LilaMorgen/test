# Version : python 3.7.4
# File : calculator.py
# Author : Lila Morgen
# Time : 2020/10/27 12:52
# description : This is a GridLayout

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 创建网格布局对象
        grid = QGridLayout()
        # 在窗口上设置网格布局
        self.setLayout(grid)

        # 创建计算器按钮字符名称列表
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        # 创建计算器字符位置列表
        positions = [(i, j) for i in range(5) for j in range(4)]

        # 将两个列表元素一一对应
        for position, name in zip(positions, names):
            # 当按钮字符为空时，继续循环，不执行创建按钮操作
            if name == '':
                continue
            # 创建按钮
            button = QPushButton(name)
            # 在网格布局中指定位置加入该按钮
            # position是元组，*position是对其进行拆包处理，得到row和column的坐标
            grid.addWidget(button, *position)

        # 设置窗口在屏幕中的位置
        self.move(300, 300)
        # 设置窗口标题
        self.setWindowTitle('Calculator')
        # 循环显示窗口
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
