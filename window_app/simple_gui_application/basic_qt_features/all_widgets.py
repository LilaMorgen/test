# Author: Lila Morgen
# ProjectName: test
# FileName: all_widgets.py
# Date: 2020/11/12
# Description:

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        # self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('All Widgets')

        layout = QVBoxLayout()
        widgets = [QCheckBox,  # 检查框
                   QComboBox,  # 下拉列表框
                   QDateEdit,  # 日期编辑框
                   QDateTimeEdit,  # 日期与时间编辑框
                   QDial,  # 刻度盘
                   QDoubleSpinBox,  # 双精度选值框
                   QFontComboBox,  # 字体下拉列表框
                   QLCDNumber,  # 数字显示屏
                   QLabel,  # 标签
                   QLineEdit,  # 行编辑框
                   QProgressBar,  # 进度条
                   QPushButton,  # 提交按钮
                   QRadioButton,  # 单选按钮
                   QSlider,  # 滑动条
                   QSpinBox,  # 选值框
                   QTimeEdit]  # 时间编辑框

        for w in widgets:
            layout.addWidget(w())

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
