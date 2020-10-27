# Version : python 3.7.4
# File : simple.py
# Author : Lila Morgen
# Time : 2020/10/25 13:33
# description : 

import sys
from PyQt5.QtWidgets import QApplication, QWidget


def main():
    # 创建应用对象，传入参数列表
    app = QApplication(sys.argv)

    # 创建用户界面对象的基类---小部件/窗口(没有父级类的小部件叫窗口)
    w = QWidget()
    # 调整小部件大小，传入宽和高的像素(px)
    w.resize(250, 150)
    # 移动小部件位置，定位是以小部件左上角为坐标位置进行定位
    # 即确定左上角点在屏幕中的位置，单位是像素(px)
    w.move(300, 300)
    # 设置窗口的标题显示在标题栏上
    w.setWindowTitle('Simple')
    # 显示小部件
    # 小部件先在内存中创建，然后显示在屏幕上
    w.show()
    # 应用循环，创建出口
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
