# Author: Lila Morgen
# ProjectName: test
# FileName: calender.py
# Date: 2020/11/6
# Description:

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QDate


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 创建垂直布局
        v_box = QVBoxLayout(self)

        # 创建日历对象
        cal = QCalendarWidget(self)
        # 显示日历网格
        cal.setGridVisible(True)
        # 将日历上的QDate信号与槽相连
        cal.clicked[QDate].connect(self.show_date)

        # 在垂直布局中添加日历
        v_box.addWidget(cal)

        # 创建标签对象
        self.lbl = QLabel(self)
        # 获取当前日历选择的日期
        date = cal.selectedDate()
        # 在标签上展示日期
        self.lbl.setText(date.toString())

        # 在垂直布局中加入标签对象
        v_box.addWidget(self.lbl)

        # 将垂直布局放置在窗口上
        self.setLayout(v_box)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calender')
        self.show()

    def show_date(self, date):
        self.lbl.setText(date.toString())


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
