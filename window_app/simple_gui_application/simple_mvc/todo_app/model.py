# Author: Lila Morgen
# ProjectName: test
# FileName: model.py
# Date: 2020/11/26
# Description:

from PyQt5.QtCore import *
from PyQt5.QtGui import *


tick = QImage('../../icons/named/tick.png')


class TodoModel(QAbstractListModel):
    def __init__(self, *args, todos=None, **kwargs):
        super(TodoModel, self).__init__(*args, **kwargs)

        self.todos = todos or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            _, text = self.todos[index.row()]
            return text
        if role == Qt.DecorationRole:
            status, _ = self.todos[index.row()]
            if status:
                return tick

    def rowCount(self, parent):
        return len(self.todos)
