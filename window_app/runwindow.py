# Version : python 3.7.4
# File : runwindow.py
# Author : Lila Morgen
# Time : 2020/9/15 10:05
# description : 

import sys
from window_app import signal_slot
from PyQt5.QtWidgets import QApplication, QMainWindow


def _main():
    # 创建应用程序
    app = QApplication(sys.argv)
    # 创建主窗口
    main_window = QMainWindow()
    # 创建控件实例
    ui = signal_slot.Ui_MainWindow()
    # 绘制窗口中的控件
    ui.setupUi(main_window)
    # 循环显示主窗口
    main_window.show()
    # 退出循环命令
    sys.exit(app.exec_())


if __name__ == '__main__':
    _main()
