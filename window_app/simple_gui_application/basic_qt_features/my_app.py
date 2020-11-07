# Version : python 3.7.4
# File : my_app.py
# Author : Lila Morgen
# Time : 2020/11/7 17:37
# description : 

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


# 创建应用实例
app = QApplication(sys.argv)

# 创建窗口实例
window = QMainWindow()
# 显示窗口
window.show()

# 应用事件循环
app.exec_()
