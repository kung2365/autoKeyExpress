from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QTextEdit
import sys

from PyQt5.QtGui import QPixmap

global path

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Open File"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        fname = QFileDialog.getOpenFileName(self,'Open file', 'c:\\', "Image files (*.jpg *.gif)")
        imagePath = fname[0]
        return imagePath

def a():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
    return
