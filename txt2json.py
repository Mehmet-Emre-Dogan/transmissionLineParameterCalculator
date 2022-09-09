from tokenize import Double
from common import *
from guiFiles.txtToJsonGui import Ui_MainWindow as txt2jsonWind

class txt2jsonWindow(myWindowSkeleton):
    sigCreated = pyqtSignal(str)
    def __init__(self):
        super(txt2jsonWindow, self).__init__()
        self.ui = txt2jsonWind()
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
        files = getExtensionsOnly(files, ".txt")
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
        filenameOut = "".join(cleanFilename) + ".json" # Convert the filename.anything to filename.json
        filepathOut = currDirectory + "\\userdata\\" + filenameOut
        try:
            with open(filepathIn, "r", encoding="UTF-8") as fptr:
                lines =  fptr.readlines()
        except Exception as ex:
            self.errorMessage("An error occurd during file reading!", str(ex))
            return
        
        try:
            noc = int(lines[5])     
            dataDict = {
                "Sbase (MVA)": float(lines[1]),
                "Vbase (kV)": float(lines[3]),
                "Number of circuits": int(lines[5])  ,
                "Number of bundle conductors per phase": int(lines[7]),
                "Bundle distance (m)": float(lines[9]),
                "Length of the line (km)": float(lines[11]),
                "ACSR conductor name": lines[13].strip(),
                "C1 Phase C (centre)": [float(lines[15]), float(lines[16])],
                "C1 Phase A (centre)": [float(lines[18]), float(lines[19])],
                "C1 Phase B (centre)": [float(lines[21]), float(lines[22])],
                # no need for placeholder. i fixed the calculator now
                # # placeholder for 1 cct case to prevent calc from crashing
                # # i will push 0 to those unnecessary areas
                # "C2 Phase C (centre)": [0, 0],
                # "C2 Phase A (centre)": [0, 0],
                # "C2 Phase B (centre)": [0, 0],
            }
            if noc == 2:
                dataDict.update({
                "C2 Phase C (centre)": [float(lines[24]), float(lines[25])],
                "C2 Phase A (centre)": [float(lines[27]), float(lines[28])],
                "C2 Phase B (centre)": [float(lines[30]), float(lines[31])],
                })
        except Exception as ex:
            self.errorMessage("Invalid file detected!", str(ex))
            return
        
        try:
            dumpDict(dataDict, filepath=filepathOut)
        except (Exception, OSError, FileNotFoundError) as ex:
            self.errorMessage(text=str(ex))
        else:
            self.infoMessage("Success", f"{filepathIn} saved successfully to file {filepathOut}")
            self.sigCreated.emit(filenameOut)
def app():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    win = txt2jsonWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app()