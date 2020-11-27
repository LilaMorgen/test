# Author: Lila Morgen
# ProjectName: test
# FileName: browser.py
# Date: 2020/11/27
# Description:

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *


class MainWindow(QMainWindow):
    htmlFinished = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # self.setWindowTitle('My Browser')
        self.init_ui()

    def init_ui(self):
        # 菜单栏和菜单
        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')
        help_menu = menubar.addMenu('&Help')

        # 状态栏
        self.statusBar()

        # 打开文件动作
        open_file_action = QAction(QIcon('../../icons/named/folder-open.png'), 'Open File...', self)
        open_file_action.setStatusTip('Open from file')
        open_file_action.triggered.connect(self.open_file)
        file_menu.addAction(open_file_action)

        # 保存网页动作
        save_file_action = QAction(QIcon('../../icons/named/disk.png'), 'Save Page As...', self)
        save_file_action.setStatusTip('Save current page to file')
        save_file_action.triggered.connect(self.save_file)
        file_menu.addAction(save_file_action)

        # 打印网页动作
        print_action = QAction(QIcon('../../icons/named/printer.png'), 'Print...', self)
        print_action.setStatusTip('Print current page')
        print_action.triggered.connect(self.print_page)
        file_menu.addAction(print_action)

        # 关于软件信息动作
        about_action = QAction(QIcon('../../icons/named/question.png'), 'About', self)
        about_action.setStatusTip('Message about App')
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

        # 工具栏导航条
        navigation = QToolBar('Navigation')
        navigation.setIconSize(QSize(16, 16))
        self.addToolBar(navigation)

        # 创建浏览器部件并设置开始页面
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.baidu.com'))
        # 更新页面是否安全
        self.browser.urlChanged.connect(self.update_urlbar)
        # 更新窗口标题
        self.browser.loadFinished.connect(self.update_title)

        # 在导航栏上添加后退动作
        back_btn = QAction(QIcon('../../icons/named/arrow-180.png'), 'Back', self)
        back_btn.setStatusTip('Back to previous page')
        back_btn.triggered.connect(self.browser.back)
        navigation.addAction(back_btn)

        # 在导航栏上添加前进动作
        next_btn = QAction(QIcon('../../icons/named/arrow.png'), 'Forward', self)
        next_btn.setStatusTip('Forward to next page')
        next_btn.triggered.connect(self.browser.forward)
        navigation.addAction(next_btn)

        # 在导航栏上添加重新加载动作
        reload_btn = QAction(QIcon('../../icons/named/arrow-circle.png'), 'Reload', self)
        reload_btn.setStatusTip('Reload page')
        reload_btn.triggered.connect(self.browser.reload)
        navigation.addAction(reload_btn)

        # 在导航栏上添加主页动作
        home_btn = QAction(QIcon('../../icons/named/home.png'), 'Home', self)
        home_btn.setStatusTip('Go home')
        home_btn.triggered.connect(self.navigate_home)
        navigation.addAction(home_btn)

        # 网页安全标识
        self.httpsicon = QLabel()
        self.httpsicon.setPixmap(QPixmap('../../icons/named/lock.png'))
        navigation.addWidget(self.httpsicon)

        # 网址编辑栏
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navigation.addWidget(self.urlbar)

        # 在导航栏上添加停止网页加载动作
        stop_btn = QAction(QIcon('../../icons/named/cross-circle.png'), 'Stop', self)
        stop_btn.setStatusTip('Stop loading current page')
        stop_btn.triggered.connect(self.browser.stop)
        navigation.addAction(stop_btn)

        self.setCentralWidget(self.browser)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Open file', '',
                                                  'Hypertext Markup Language (*.htm *.html);;',
                                                  'All files (*.*)')
        if filename:
            with open(filename, 'r') as f:
                html = f.read()
            self.browser.setHtml(html)
            self.urlbar.setText(filename)
            self.browser.setUrl(QUrl(filename))
            # self.navigate_to_url()

    def callback(self, html):
        self.htmlFinished.emit()
        self.html = html

    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, 'Save Page As', '',
                                                  'Hypertext Markup Language (*.htm *.html);;',
                                                  'All files (*.*)')
        if filename:
            self.browser.page().toHtml(self.callback)
            loop = QEventLoop()
            self.htmlFinished.connect(loop.quit)
            loop.exec_()
            with open(filename, 'w') as f:
                f.write(self.html)

    def print_preview(self, printer):
        self.browser.render(QPainter(printer))

    def print_page(self):
        dlg = QPrintPreviewDialog()
        dlg.paintRequested.connect(self.print_preview)
        dlg.exec_()

    def about(self):
        dlg = QDialog()
        dlg.exec_()

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://www.baidu.com'))

    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == '':
            q.setScheme('http')

        self.browser.setUrl(q)

    def update_urlbar(self, q):
        if q.scheme() == 'https':
            self.httpsicon.setPixmap(QPixmap('../../icons/named/lock-ssl.png'))
        else:
            self.httpsicon.setPixmap(QPixmap('../../icons/named/lock.png'))

        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle('My Browser - %s' % title)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
