# Author: Lila Morgen
# ProjectName: test
# FileName: todolist.py
# Date: 2020/11/26
# Description:

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from todo_app.model import TodoModel
import json


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('TODO')
        self.init_ui()

        self.model = TodoModel()
        self.load()
        self.todoView(self.model)

    def init_ui(self):
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        self.list_view = QListView()
        v_layout.addWidget(self.list_view)

        delete_btn = QPushButton('Delete')
        delete_btn.pressed.connect(self.delete)
        complete_btn = QPushButton('Complete')
        complete_btn.pressed.connect(self.complete)
        h_layout.addWidget(delete_btn)
        h_layout.addWidget(complete_btn)
        v_layout.addLayout(h_layout)

        self.line_edit = QLineEdit()
        v_layout.addWidget(self.line_edit)

        add_btn = QPushButton('Add ToDo')
        add_btn.pressed.connect(self.add)
        v_layout.addWidget(add_btn)

        widget = QWidget(self)
        widget.setLayout(v_layout)

        self.setCentralWidget(widget)

    def todoView(self, model, flag=1):
        if flag == 1:
            self.list_view.setModel(model)
        elif flag == 2:
            # print(self.list_view.selectedIndexes())
            return self.list_view.selectedIndexes()
        elif flag == 3:
            self.list_view.clearSelection()

    def todoEdit(self, flag=1):
        if flag == 1:
            return self.line_edit.text()
        elif flag == 2:
            self.line_edit.setText('')

    def add(self):
        # 获取行编辑处文本
        text = self.todoEdit(flag=1)
        if text:
            self.model.todos.append((False, text))
            # 触发更新
            self.model.layoutChanged.emit()
            # 将行编辑设置为空文本
            self.todoEdit(flag=2)
            self.save()

    def delete(self):
        # print('in delete')
        indexs = self.todoView(self.model, flag=2)
        # print(indexs)
        if indexs:
            index = indexs[0]
            # print(index)
            del self.model.todos[index.row()]
            self.model.layoutChanged.emit()
            self.todoView(self.model, flag=3)
            self.save()

    def complete(self):
        # print('in complete')
        indexs = self.todoView(self.model, flag=2)
        if indexs:
            index = indexs[0]
            row = index.row()
            status, text = self.model.todos[row]
            self.model.todos[row] = (True, text)
            self.model.dataChanged.emit(index, index)
            self.todoView(self.model, flag=3)
            self.save()

    def load(self):
        try:
            with open('data.json', 'r') as f:
                self.model.todos = json.load(f)
        except Exception:
            pass

    def save(self):
        with open('data.json', 'w') as f:
            json.dump(self.model.todos, f)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
