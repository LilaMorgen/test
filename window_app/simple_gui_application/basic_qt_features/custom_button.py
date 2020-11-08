# Version : python 3.7.4
# File : custom_button.py
# Author : Lila Morgen
# Time : 2020/11/7 23:37
# description : 

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class CustomButton(QPushButton):
    def __init__(self, text, parent):
        super().__init__(text, parent)

    # 自定义keyPressEvent(self, e)方法
    def keyPressEvent(self, e):
        super().keyPressEvent(e)
