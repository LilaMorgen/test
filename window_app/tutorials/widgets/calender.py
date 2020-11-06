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
        v_box = QVBoxLayout(self)

        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.show_date)

        v_box.addWidget(cal)

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())

        v_box.addWidget(self.lbl)

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
