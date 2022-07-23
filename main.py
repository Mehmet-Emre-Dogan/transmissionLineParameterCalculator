import sys
import os
import re
from unittest import case
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtCore 
from PyQt5 import QtGui

import calculate


from guiFiles.mainGui import Ui_MainWindow as mainMainWindow
from guiFiles.creatorGui import Ui_MainWindow as creatorMainWindow

DEBUG = True
DEFAULT_CBOX_TEXT = "Select Dataset"

currDirectory = os.path.dirname(__file__)

# https://stackoverflow.com/questions/4836710/is-there-a-built-in-function-for-string-natural-sort
def naturalSort(arr: list) -> list: 
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(arr, key=alphanum_key)

def getExtensionsOnly(arr:list, ext:str) -> list:
    return [item for item in arr if str(item).endswith(ext)]


class myWindow(QtWidgets.QMainWindow):
    keyPressed = QtCore.pyqtSignal(QtCore.QEvent)
    def __init__(self):
        super(myWindow, self).__init__()
        self.ui = mainMainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('img.png'))

        # Menu bar connection: please see sources:
        # https://stackoverflow.com/questions/46082666/pyqt5-toolbar-onclick-function
        # https://zetcode.com/gui/pyqt5/menustoolbars/
        self.ui.menubar.triggered.connect(self.whoGotSelected)
        self.ui.comboBox.activated.connect(self.calc)
        self.ui.btnRefresh.clicked.connect(self.loadCbox)

        self.loadCbox()
    
        # Menu bar selection 
    def whoGotSelected(self, selection):
        txt = selection.text()
        if DEBUG:
            print(f"Selection from menubar: {txt}")
        
        match txt:
            case "Make File":
                self.makefile()
            case "Txt to json":
                self.txt2json()

    def loadCbox(self, selectedText=DEFAULT_CBOX_TEXT):
        self.ui.comboBox.clear() 
        files = os.listdir(currDirectory)
        if DEBUG:
            print(files)
        files = getExtensionsOnly(files, ".json")
        files = naturalSort(files)
        files.insert(0, DEFAULT_CBOX_TEXT)
        self.ui.comboBox.addItems(files)
        try:
            self.ui.comboBox.setCurrentIndex(files.index(selectedText))
        except ValueError: # pass if the selected text is not in cbox
            pass
    
    def calc(self):
        if self.ui.comboBox.currentText() == DEFAULT_CBOX_TEXT:
            return # do not calculate, exit immediately
        res = calculate.calculate(self.ui.comboBox.currentText())
        self.ui.rpu.setText(str(res["R_pu"]) + " pu")
        self.ui.xpu.setText(str(res["X_pu"]) + " pu")
        self.ui.bpu.setText(str(res["B_pu"]) + " pu")
        self.ui.lbl_r.setText(str(res["R"]) + " Ω")
        self.ui.lbl_x.setText(str(res["X_L"]) + " Ω")
        self.ui.lbl_b.setText(str(res["B_C"]) + " S")


            



def app():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    win = myWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app()