import os

from PyQt5.QtWidgets import QPushButton, QAction, QMenu

try:
    from PyQt5 import sip
except ImportError:
    import sip
from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()  # Call the inherited classes __init__ method
        self.ui = uic.loadUi(self.__getPath(), self)  # Load the .ui file
        self.__defineWidgets()

        self.worker = Worker1()
        self.worker.start()
        self.worker.ImageUpdate.connect(self.ImageUpdateSlot)

    def ImageUpdateSlot(self, image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(image))

    def __getPath(self, ):
        path = os.getcwd().split("gui")[0]
        path = path + os.sep + "files" + os.sep + "RecycleIT_B_gui.ui"
        if os.sep == "\\":
            path.replace("/", "\\")
        return path

    def __defineWidgets(self, ):
        self.FeedLabel = self.findChild(QLabel, "q_camera_label")

    def __clicker(self):
        self.action_Open_Model.triggered.connect(lambda: self.__menuBarListener("openModel"))
        self.action_Quit.triggered.connect(lambda: self.__menuBarListener("action_Quit"))

    def __menuBarListener(self, state):
        print(state)
        if state == "action_Quit":
            sys.exit()

    def __quitApp(self):
        sys.exit()


class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)

    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture(0)
        while self.ThreadActive:
            ret, frame = Capture.read()
            if ret:
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(image, 1)
                ConvertToQtFormat = QImage(FlippedImage.data,
                                           FlippedImage.shape[1],
                                           FlippedImage.shape[0],
                                           QImage.Format_RGB888)
                pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(pic)

    def stop(self):
        self.ThreadActive = False
        self.quit()


# initialize the app
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
