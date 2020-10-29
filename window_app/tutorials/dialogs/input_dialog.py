# Version : python 3.7.4
# File : input_dialog.py
# Author : Lila Morgen
# Time : 2020/10/29 13:27
# description : 

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QInputDialog


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.show_dialog)

        self.le = QLineEdit(self)
        self.le.move(130, 24)

        self.setGeometry(300, 300, 450, 300)
        self.setWindowTitle('Dialog')
        self.show()

    def show_dialog(self):
        # 创建输入对话框，用getText方法接收文本(text)和用户信号事件(ok)
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')

        # 如果用户返回True,那么将接收到的文本展示在行输入框内
        if ok:
            self.le.setText(str(text))


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
