from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QTextEdit, QLineEdit
import sys


from PyQt5.QtGui import QPixmap
import getFile as gt


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "Add Item To Express V.0.0.2"
        self.top = 300
        self.left = 700
        self.width = 350
        self.height = 170

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()
        self.label1 = QLabel("Add Item")
        self.label1.setFont(QtGui.QFont('SansSerif', 10))
        vbox.addWidget(self.label1)

        self.btn1 = QPushButton("Brows")
        self.btn1.clicked.connect(self.getImage)

        vbox.addWidget(self.btn1)

        self.lineEdit = QLineEdit("")
        vbox.addWidget(self.lineEdit)

        self.btn2 = QPushButton("Run")
        self.btn2.setFixedHeight(40)
        self.btn2.clicked.connect(self.run)

        vbox.addWidget(self.btn2)

        

        self.setLayout(vbox)

        self.show()

    def getImage(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file','c:\\', "Excel File (*.xlsx)")
        imagePath = fname[0]
        self.lineEdit.setText(imagePath)
        # pixmap = QPixmap(imagePath)
        # self.label.setPixmap(QPixmap(pixmap))
        # self.resize(pixmap.width(), pixmap.height())
    def run(self):
        print(self.lineEdit.text())
        gt.auto(self.lineEdit.text())
        #pass

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())