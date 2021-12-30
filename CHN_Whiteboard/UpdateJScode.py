from PyQt5.QtCore import QUrl
import sys
from PyQt5.QtCore import *
from PyQt5. QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class WhitboardWindow(QMainWindow):
    def __init__(self):
        super(WhitboardWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://chnsoftwaredevelopers.com/CHN-Classroom/Whiteboard/v1.3.0/Function.js'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

Whiteboard = QApplication(sys.argv)
QApplication.setApplicationName('CHN Whiteboard v1.3.0')
window = WhitboardWindow()