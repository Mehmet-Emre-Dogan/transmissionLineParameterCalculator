from common import *
from guiFiles.creatorGui import Ui_MainWindow as creatorMainWindow

class creatorWindow(QtWidgets.QMainWindow):
    sigCreated = pyqtSignal(str)
    def __init__(self):
        super(creatorWindow, self).__init__()
        self.ui = creatorMainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('img.png'))
        self.ui.btnSave.clicked.connect(self.save)
    
    
    
    
    def save(self):
        self.sigCreated.emit("data1.json")

def app():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    win = creatorWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app()