import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie

class Loadingscreen(QWidget):
    def __init__(self):
        super.__init__()


        self.setFixedsize(200, 200)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)


        self.label_animation = QLabel
        self.movie = QMovie('AIVA.gif')



        timer = QTimer(self)
        self.startAnimation()
        timer.singleShot(3000, self.stopAnimation)

        self.show()

        def startAnimation(self):
            self.movie.start()

        def stopAnimation(self):
            self.movie.stop()
            self.close()

class Appdemo(QWidget):
    def __init__(self):
        super().__init__()
        label = QLabel('<font size = 12> App', self)
        label.setGeometry(150, 150, 300, 50)
        self.Loading_screen = Loadingscreen()


        self.show()
app = QApplication(sys,argv)
demo = Appdemo()
app.exit(app.exec_())