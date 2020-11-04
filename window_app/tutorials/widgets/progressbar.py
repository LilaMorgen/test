# Version : python 3.7.4
# File : progressbar.py
# Author : Lila Morgen
# Time : 2020/11/4 23:03
# description : 

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QPushButton
from PyQt5.QtCore import QBasicTimer


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 创建进度条对象
        self.pbar = QProgressBar(self)
        # 设置进度条位置及大小
        self.pbar.setGeometry(30, 40, 200, 25)

        # 创建按钮对象来控制进度条开始、停止
        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.do_action)

        # 创建计时器对象
        self.timer = QBasicTimer()
        # 设置初始进度值
        self.step = 0

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Progress Bar')
        self.show()

    # 重写timerEvent(self, event)方法
    def timerEvent(self, event):
        # 如果进度值大于等于100,则停止计时，并且在按钮上显示Finished
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return
        # 计时器计时累加
        self.step += 1
        # 将进度值设置在进度条上进行显示
        self.pbar.setValue(self.step)
        # print(self.step)

    # 最开始点击按钮进入此方法，这时计时器还是未激活状态
    # 所以是执行else下面的语句， 这时会开始计时并且在按钮上显示Stop
    # 当计时器激活时，再次点击按钮，那么此时应该执行if成立条件下语句，即会停止计时并在按钮上显示Start
    def do_action(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
            # print('timer is active')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')
            # print('timer is not active')


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
