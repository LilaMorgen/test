import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox, QMenu


class Example(QMainWindow):
    """docstring for Example"""

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        menubar = self.menuBar()
        self.statusBar()
        file_menu = menubar.addMenu('File(&B)')

        exit_act = QAction('Exit', self)
        exit_act.setStatusTip('This is a Exit action.')
        exit_act.setToolTip('Exit application')
        exit_act.setShortcut('Ctrl+Q')
        exit_act.triggered.connect(self.close)

        toolbar = self.addToolBar('Tools')
        toolbar.addAction(exit_act)

        file_menu.addAction(exit_act)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('My Window')
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     'Are you sure to exit application?',
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def contextMenuEvent(self, event):
        c_menu = QMenu(self)

        copy_act = c_menu.addAction('Copy')
        paste_act = c_menu.addAction('Paste')
        cut_act = c_menu.addAction('Cut')
        quit_act = c_menu.addAction('Quit')

        action = c_menu.exec_(self.mapFromGlobal(event.pos()))

        if action == quit_act:
            self.close()
            # print('Quit')


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
