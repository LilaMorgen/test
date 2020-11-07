# Version : python 3.7.4
# File : my_awesome_app.py
# Author : Lila Morgen
# Time : 2020/11/7 22:12
# description : 

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        # 继承QMainWindow的__init__方法
        super().__init__(*args, **kwargs)

        # 设置窗口标题
        self.setWindowTitle('My Awesome App')

        lbl = QLabel('This is awesome!!!', self)
        # 设置标签对齐方式，Qt.AlignCenter是中心对齐
        lbl.setAlignment(Qt.AlignCenter)
        # 在窗口中心设置标签
        self.setCentralWidget(lbl)


# 创建应用实例，传入命令参数列表
app = QApplication(sys.argv)

# 创建窗口实例
window = MainWindow()
# 显示窗口
window.show()

# 应用事件循环
app.exec_()
