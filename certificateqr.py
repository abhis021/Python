import sys
import pyqrcode
from PyQt5 import QtGui, QtCore, QtWidgets
from pyqrcode import QRCode
from PIL import ImageQt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
from PyQt5.QtGui import QPixmap

class QRCodeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(700, 550)
        self.setWindowTitle("QR Code Generator for PC")
        self.initUI()
        
    def initUI(self):
        font = QFont("Times", 16)

        btn = QtWidgets.QPushButton("OK", self)
        btn.clicked.connect(self.generate_QRCode)
        btn.resize(100, 50)
        btn.move(250, 400)

        btn = QtWidgets.QPushButton("View", self)
        btn.clicked.connect(self.showQR)
        btn.resize(100, 50)
        btn.move(350, 400)

        btn = QtWidgets.QPushButton("Quit", self)
        btn.clicked.connect(self.Quit)
        btn.resize(100, 50)
        btn.move(450, 400)

        mainLayout = QVBoxLayout()
        entryLayout = QHBoxLayout()
        buttonLayout = QHBoxLayout()
        imageLayout = QVBoxLayout()
        imageLayout.addStretch()

        label = QLabel("Enter Text : ")
        label.setFont(font)

        self.textEntry = QLineEdit(self)
        self.textEntry.setFont(font)
        entryLayout.addWidget(label)
        entryLayout.addWidget(self.textEntry)
        mainLayout.addLayout(entryLayout)

        self.setLayout(mainLayout)

    def generate_QRCode(self):
        s = self.textEntry.text()
        url = pyqrcode.create(s)
        url.png("ResultQR.png", scale = 6)
    
    def showQR(self):
        graphicsView = QtWidgets.QGraphicsView(QWidget)

        pix = QPixmap("ResultQR.png")
        item = QWidgets.QGraphicsPixmapItem(pix)
        scene = QWidgets.QGraphicsScence(self)
        scene.addItem(item)
        self.ui.graphicsView.setScene(scene)
        
        # img = mpimg.imread('ResultQR.png')
        # imgplot = plt.imshow(img)
        # plt.show()
        
    def Quit(self):
        sys.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    demo = QRCodeApp()
    demo.show()
    sys.exit(app.exec_())
