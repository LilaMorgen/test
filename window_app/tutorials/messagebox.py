# Version : python 3.7.4
# File : messagebox.py
# Author : Lila Morgen
# Time : 2020/10/25 15:59
# description : 

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Message Box')
        self.show()

    # 重写QWidget中的closeEvent()方法
    def closeEvent(self, event):
        # QMessageBox.question(self, '消息提示窗口标题',
        #                      '提示消息',
        #                      对话框中按钮组合,
        #                      默认高亮按钮)
        reply = QMessageBox.question(self, 'Message',
                                     'Are you sure to quit?',
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        # 判断接收的返回值，根据不同返回值对事件进行不同操作
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
