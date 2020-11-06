# Author: Lila Morgen
# ProjectName: test
# FileName: line_edit.py
# Date: 2020/11/6
# Description:

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        line_edit = QLineEdit(self)
        line_edit.move(60, 100)

        self.lbl = QLabel(self)
        self.lbl.move(60, 40)

        line_edit.textChanged[str].connect(self.on_changed)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Line Edit')
        self.show()

    def on_changed(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
