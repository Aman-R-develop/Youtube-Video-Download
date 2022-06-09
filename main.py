import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from pytube import YouTube
import datetime
b = datetime.datetime.utcnow()
class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('icon.jfif'))
        self.title = 'Download Youtube Video'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 140
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)

        self.button = QPushButton('Download', self)
        self.button.move(20, 80)

        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        otp = "./video"
        YouTube(textboxValue).streams.get_highest_resolution().download(otp)
        with open('./video/inputs.txt','a') as f:
            with open('./video/inputs.txt', 'r') as f:
                v = f.read()
                if 'Hello.. How are you.. I wish you are liking this... This is the list of videos you downloaded' in v:
                    pass
                else:
                    with open('./video/inputs.txt', 'a') as f:
                        f.write("Hello.. How are you.. I wish you are liking this... This is the list of videos you downloaded")

        with open('./video/inputs.txt', 'a') as f:
            f.write("\n........................................\n")
            f.write(f"The time was: {b}\n")
            f.write("The user downloaded:\n")
            f.write(YouTube(textboxValue).title)
            f.write("\nThe user ended the program :)")
            f.write("\n........................................")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
