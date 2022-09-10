from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QMainWindow
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtCore 
from PyQt5 import QtGui
import sys
import os
from json import load, dump
import re
import datetime
import sys

DEBUG = True
DEFAULT_CBOX_TEXT = "Select Dataset"

STYLESHEET_STR = """
*:disabled {
	background-color:rgb(30, 30, 30);	
	color: rgb(127, 127, 127);
}
*{
	background-color: rgb(90, 90, 90);
	color: white;
}
QLabel:disabled {
	background-color: rgb(90, 90, 90);
}
QGroupBox{
	border: 1px solid rgb(70, 70, 70);
	margin-top: 1em;
	color: rgb(255, 255, 255);
}
QGroupBox:disabled {
	background-color: rgb(90, 90, 90);
}
QGroupBox::title {
	background-color: rgb(90, 90, 90);
    	top: -0.8em;
    	left: 1em;
}
QMenu::item{
	background-color: rgb(90, 90, 90);
	color: white;
}

QMenuBar::item:selected{
	color: cyan;
}
QMenu::item:selected {
	color: cyan;
}
QToolTip{
	background-color: whitesmoke;
	color:black;
}
"""

# determine if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    currDirectory = os.path.dirname(sys.executable)
elif __file__:
    currDirectory = os.path.dirname(__file__)

# https://stackoverflow.com/questions/4836710/is-there-a-built-in-function-for-string-natural-sort
def naturalSort(arr: list) -> list: 
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(arr, key=alphanum_key)

def getExtensionsOnly(arr:list, ext:str) -> list:
    return [item for item in arr if str(item).endswith(ext)]

def loadDict(filepath:str) -> dict:
    with open(filepath, "r", encoding="utf-8") as fptr:
        dictToReturn = load(fptr)
    return dictToReturn

def dumpDict(dictionary:dict, filepath) -> None:
    with open(filepath, "w", encoding="utf-8") as fptr:
        dump(dictionary, fptr)


class myWindowSkeleton(QMainWindow):

    ###############################
    """Message boxes"""
    ###############################

    # See the link below to learn more about editing texts of message box buttons
    # https://stackoverflow.com/questions/35887523/qmessagebox-change-text-of-standard-button

    def infoMessage(self, title="Info", text="Text text"):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setWindowIcon(QtGui.QIcon('img.png'))
        msg.setText(text)
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        btnOk = msg.button(QMessageBox.Ok)
        # btnOk.setText(self.msögBoxStrs[self.lang]["ok"])
        msg.setStyleSheet(STYLESHEET_STR)
        msg.exec_()

    def errorMessage(self, title="Error", text="An error occured"):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setWindowIcon(QtGui.QIcon('img.png'))
        msg.setText(text)
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)
        btnOk = msg.button(QMessageBox.Ok)
        # btnOk.setText(self.msgBoxStrs[self.lang]["ok"])
        msg.setStyleSheet(STYLESHEET_STR)
        msg.exec_()

    def confirmationMsg(self, title="Question", text="Are you sure doing xyz?"):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setWindowIcon(QtGui.QIcon('img.png'))
        msg.setText(text)
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        btnYes = msg.button(QMessageBox.Yes)
        # btnYes.setText(self.msgBoxStrs[self.lang]["yes"])
        btnNo = msg.button(QMessageBox.No)
        # btnNo.setText(self.msgBoxStrs[self.lang]["no"])
        msg.setStyleSheet(STYLESHEET_STR)
        answer = msg.exec_()
        return answer == QMessageBox.Yes

    # For more info about QFileDialog objects, visit the links below
    # https://learndataanalysis.org/source-code-how-to-use-qfiledialog-file-dialog-in-pyqt5/

    # https://stackoverflow.com/questions/59245576/attributeerror-qdialog-object-has-no-attribute-qfiledialog
    # https://stackoverflow.com/questions/28916010/qfiledialog-to-open-multiple-files

    def getDirectoryDialog(self, title="Select folder"):
        response = QFileDialog.getExistingDirectory(self, caption=title)
        return response

    def getFilesDialog(self, title="Select files", path=None, filter="All files (*.*)"):
        if path == None:
            # determine if application is a script file or frozen exe
            if getattr(sys, 'frozen', False):
                path = os.path.dirname(sys.executable)
            elif __file__:
                path = os.path.dirname(__file__)
        fileDialog = QFileDialog()
        fileDialog.setFileMode(QFileDialog.ExistingFiles)
        fileList = fileDialog.getOpenFileNames(caption=title, directory=path, filter=filter)[0]
        return fileList
