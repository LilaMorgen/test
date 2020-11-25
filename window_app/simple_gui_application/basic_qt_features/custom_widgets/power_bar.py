# Author: Lila Morgen
# ProjectName: test
# FileName: power_bar.py
# Date: 2020/11/24
# Description:

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class _Bar(QWidget):
    def __init__(self, *args, **kwargs):
        super(_Bar, self).__init__(*args, **kwargs)

        self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)

    def sizeHint(self):
        return QSize(40, 120)

    def paintEvent(self, e):
        painter = QPainter(self)
        brush = QBrush()
        brush.setColor(QColor('black'))
        brush.setStyle(Qt.SolidPattern)
        rect = QRect(0, 0, painter.device().width(), painter.device().height())
        painter.fillRect(rect, brush)

        dial = self.parent()._dial
        vmin, vmax = dial.minimum(), dial.maximum()
        value = dial.value()

        pen = painter.pen()
        pen.setColor(QColor('red'))
        painter.setPen(pen)

        font = painter.font()
        font.setFamily('Times')
        font.setPointSize(18)
        painter.setFont(font)

        painter.drawText(25, 25, '{}---{}---{}'.format(vmin, value, vmax))
        painter.end()

    def _trigger_refresh(self):
        self.update()


class PowerBar(QWidget):
    """
    Custom Qt Widget to show power bar and dial.
    """
    def __init__(self, steps=5, *args, **kwargs):
        super(PowerBar, self).__init__(*args, **kwargs)

        layout = QVBoxLayout()
        self._bar = _Bar()
        layout.addWidget(self._bar)

        self._dial = QDial()
        self._dial.valueChanged.connect(self._bar._trigger_refresh)
        layout.addWidget(self._dial)

        self.setLayout(layout)


app = QApplication(sys.argv)
window = PowerBar()
window.show()
app.exec_()
