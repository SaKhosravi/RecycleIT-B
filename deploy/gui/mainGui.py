import os

from PyQt5.QtWidgets import QPushButton, QAction, QMenu

try:
    from PyQt5 import sip
except ImportError:
    import sip
from PyQt5 import QtWidgets, uic
import sys


class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainUi, self).__init__()  # Call the inherited classes __init__ method
        self.ui = uic.loadUi(self.__getPath(), self)  # Load the .ui file
        self.create
        self.show()  # Show the GUI
        self.__defineWidgets()
        self.__clicker()

    def _addMenuBar(self):
        pass

    def __getPath(self, ):
        path = os.getcwd().split("gui")[0]
        path = path + os.sep + "files" + os.sep + "RecycleIT_B_gui.ui"
        if os.sep == "\\":
            path.replace("/", "\\")
        return path

    def __defineWidgets(self, ):
        # self.button_brows = self.findChild(QPushButton, "btn_brws")
        pass

    def __clicker(self):
        self.action_Open_Model.triggered.connect(lambda: self.__menuBarListener("openModel"))

    def __menuBarListener(self, state):
        print(state)


# initialize the app
app = QtWidgets.QApplication(sys.argv)
window = MainUi()
app.exec_()
