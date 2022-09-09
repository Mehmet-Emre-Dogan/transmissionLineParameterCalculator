from tokenize import Double
from common import *
from guiFiles.jsonToTxtGui import Ui_MainWindow as json2txtWind

class json2txtWindow(myWindowSkeleton):
    sigCreated = pyqtSignal(str)
    def __init__(self):
        super(json2txtWindow, self).__init__()
        self.ui = json2txtWind()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('img.png'))
        self.ui.btnRefresh.clicked.connect(self.loadCbox)
        self.ui.btnConvert.clicked.connect(self.save)
        self.loadCbox()
        
    def save(self):
        pass

    def loadCbox(self, selectedText=DEFAULT_CBOX_TEXT):
        self.ui.comboBox.clear() 
        files = os.listdir(currDirectory + "\\userdata")
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

        
    def save(self):         
        filenameIn = self.ui.comboBox.currentText()
        filepathIn = currDirectory + "\\userdata\\" + filenameIn
        cleanFilename = filenameIn.split("."); cleanFilename.pop(-1); 
        filenameOut = "converted_" +  "".join(cleanFilename) + ".txt" # Convert the filename.anything to filename.txt
        filepathOut = currDirectory + "\\userdata\\" + filenameOut
        dataDict = loadDict(filepathIn)
        linedata = (f'Sbase (MVA)\n'
        f'{dataDict["Sbase (MVA)"]}\n'
        f'Vbase (kV)\n'
        f'{dataDict["Vbase (kV)"]}\n'
        f'Number of circuits\n'
        f'{dataDict["Number of circuits"]}\n'
        f'Number of bundle conductors per phase\n'
        f'{dataDict["Number of bundle conductors per phase"]}\n'
        f'Bundle distance (m)\n'
        f'{dataDict["Bundle distance (m)"]}\n'
        f'Length of the line (km)\n'
        f'{dataDict["Length of the line (km)"]}\n'
        f'ACSR conductor name\n'
        f'{dataDict["ACSR conductor name"]}\n'
        f'C1 Phase C (centre)\n'
        f'{dataDict["C1 Phase C (centre)"][0]}\n'
        f'{dataDict["C1 Phase C (centre)"][1]}\n'
        f'C1 Phase A (centre)\n'
        f'{dataDict["C1 Phase A (centre)"][0]}\n'
        f'{dataDict["C1 Phase A (centre)"][1]}\n'
        f'C1 Phase B (centre)\n'
        f'{dataDict["C1 Phase B (centre)"][0]}\n'
        f'{dataDict["C1 Phase B (centre)"][1]}\n')

        if dataDict["Number of circuits"] == 2:
            linedata += (f'C2 Phase C (centre)\n'
                f'{dataDict["C2 Phase C (centre)"][0]}\n'
                f'{dataDict["C2 Phase C (centre)"][1]}\n'
                f'C2 Phase A (centre)\n'
                f'{dataDict["C2 Phase A (centre)"][0]}\n'
                f'{dataDict["C2 Phase A (centre)"][1]}\n'
                f'C2 Phase B (centre)\n'
                f'{dataDict["C2 Phase B (centre)"][0]}\n'
                f'{dataDict["C2 Phase B (centre)"][1]}\n')

        linedata += "-999"
        try:
            with open(filepathOut, "w", encoding="UTF-8") as fptr:
                fptr.write(linedata)
        except Exception as ex:
            self.errorMessage("Invalid file detected!", str(ex))
            return
        else:
            self.infoMessage("Success", f"{filepathIn} saved successfully to file {filepathOut}")
            self.sigCreated.emit(filenameOut)
def app():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    win = json2txtWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app()