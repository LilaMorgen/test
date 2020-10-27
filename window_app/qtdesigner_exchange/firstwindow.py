# Version : python 3.7.4
# File : firstwindow.py
# Author : Lila Morgen
# Time : 2020/10/23 22:02
# description : 

import sys
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QDesktopWidget, QMainWindow, QApplication, QWidget
from PyQt5.QtGui import QIcon


class FirstMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(FirstMainWindow, self).__init__(parent)

        # 设置主窗口标题
        self.setWindowTitle('第一个窗口应用')

        # 设置窗口尺寸
        self.resize(400, 300)
        # 设置状态栏
        self.status = self.statusBar()
        self.status.showMessage('只存在5秒消息时间', 5000)
        # 设置按钮关闭窗口
        self.button1 = QPushButton('退出应用')
        # 将信号与槽相连
        self.button1.clicked.connect(self.click_button)
        # self.button1.clicked.connect(self.close)

        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainframe = QWidget()
        mainframe.setLayout(layout)

        self.setCentralWidget(mainframe)

    # 自定义槽
    def click_button(self):
        sender = self.sender()
        print(sender.text() + '按钮被按下')
        window = QApplication.instance()
        window.quit()

    # 窗口居中
    def center(self):
        # 获取屏幕坐标系
        screen = QDesktopWidget.screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        # 新坐标
        new_left = (screen.width() - size.width()) / 2
        new_top = (screen.height() - size.height()) / 2
        self.move(new_left, new_top)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon('../../images/eword.ico'))

    main = FirstMainWindow()
    main.show()

    sys.exit(app.exec_())
