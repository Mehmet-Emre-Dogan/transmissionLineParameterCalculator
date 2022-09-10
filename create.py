from common import *
from guiFiles.creatorGui import Ui_MainWindow as creatorMainWindow
import datetime

class creatorWindow(myWindowSkeleton):
    sigCreated = pyqtSignal(str)
    def __init__(self):
        super(creatorWindow, self).__init__()
        self.ui = creatorMainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('img.png'))
        self.ui.btnSave.clicked.connect(self.save)
        self.ui.comboBoxNccts.currentIndexChanged.connect(self.setVisiblePhases)
        


        self.setVisiblePhases()
        self.loadCboxFilesToInherit()

        self.ui.comboBoxFilesToInherit.currentIndexChanged.connect(self.loadUIData)


        customDT = datetime.datetime.now().strftime('%Y-%m-%d_%H.%M.%S')
        self.ui.lineEditFileName.setText("TL_" + customDT + ".json")

    def setVisiblePhases(self):
        isEnabled = False if self.ui.comboBoxNccts.currentText() == "1" else True          
        self.ui.doubleSpinBoxA2x.setEnabled(isEnabled)
        self.ui.doubleSpinBoxA2y.setEnabled(isEnabled)
        self.ui.doubleSpinBoxB2x.setEnabled(isEnabled)
        self.ui.doubleSpinBoxB2y.setEnabled(isEnabled)
        self.ui.doubleSpinBoxC2x.setEnabled(isEnabled)
        self.ui.doubleSpinBoxC2y.setEnabled(isEnabled)

    def loadUIData(self):
        currText = self.ui.comboBoxFilesToInherit.currentText()
        if currText == "Create New":
            datadict = {"Sbase (MVA)": 0.0,
            "Vbase (kV)": 0.0, 
            "Number of circuits": 1, 
            "Number of bundle conductors per phase": 1,
            "Bundle distance (m)": 0.0,
            "Length of the line (km)": 0.0,
            "ACSR conductor name": "Waxwing",
            "C1 Phase A (centre)": [0.0, 0.0],
            "C1 Phase B (centre)": [0.0, 0.0],
            "C1 Phase C (centre)": [0.0, 0.0],
            "C2 Phase A (centre)": [0.0, 0.0],
            "C2 Phase B (centre)": [0.0, 0.0],
            "C2 Phase C (centre)": [0.0, 0.0]}
        else:    
            datadict = loadDict(currDirectory + "\\userdata\\" + self.ui.comboBoxFilesToInherit.currentText())
        
        self.ui.doubleSpinBoxSbase.setValue(datadict["Sbase (MVA)"])
        self.ui.doubleSpinBoxVbase.setValue(datadict["Vbase (kV)"])
        self.ui.comboBoxNccts.setCurrentIndex([1, 2].index(datadict["Number of circuits"]))
        self.ui.spinBoxBundleCou.setValue(datadict["Number of bundle conductors per phase"])
        self.ui.doubleSpinBundleDistance.setValue(datadict["Bundle distance (m)"])
        self.ui.doubleSpinLineLength.setValue(datadict["Length of the line (km)"])

        # https://stackoverflow.com/questions/7479915/getting-all-items-of-qcombobox-pyqt4-python
        setattr(self.ui.comboBoxConductorName, "allItems", lambda: [self.ui.comboBoxConductorName.itemText(i) for i in range(self.ui.comboBoxConductorName.count())])
        # print(self.ui.comboBoxConductorName.allItems())
        self.ui.comboBoxConductorName.setCurrentIndex(self.ui.comboBoxConductorName.allItems().index(datadict["ACSR conductor name"]))
        self.ui.doubleSpinBoxA1x.setValue(datadict["C1 Phase A (centre)"][0])
        self.ui.doubleSpinBoxA1y.setValue(datadict["C1 Phase A (centre)"][1])
        self.ui.doubleSpinBoxB1x.setValue(datadict["C1 Phase B (centre)"][0])
        self.ui.doubleSpinBoxB1y.setValue(datadict["C1 Phase B (centre)"][1])
        self.ui.doubleSpinBoxC1x.setValue(datadict["C1 Phase C (centre)"][0])
        self.ui.doubleSpinBoxC1y.setValue(datadict["C1 Phase C (centre)"][1])

        if datadict["Number of circuits"] == 2:
            self.ui.doubleSpinBoxA2x.setValue(datadict["C2 Phase A (centre)"][0])
            self.ui.doubleSpinBoxA2y.setValue(datadict["C2 Phase A (centre)"][1])
            self.ui.doubleSpinBoxB2x.setValue(datadict["C2 Phase B (centre)"][0])
            self.ui.doubleSpinBoxB2y.setValue(datadict["C2 Phase B (centre)"][1])
            self.ui.doubleSpinBoxC2x.setValue(datadict["C2 Phase C (centre)"][0])
            self.ui.doubleSpinBoxC2y.setValue(datadict["C2 Phase C (centre)"][1])

        self.setVisiblePhases()

    def save(self):
        if not self.ui.lineEditFileName.text():
            customDT = datetime.datetime.now().strftime('%Y-%m-%d_%H.%M.%S')
            self.ui.lineEditFileName.setText("TL_" + customDT + ".json")      

        filename = self.ui.lineEditFileName.text()
        filepath = currDirectory + "\\userdata\\" + filename
        dataDict = {
            "Sbase (MVA)": self.ui.doubleSpinBoxSbase.value(),
            "Vbase (kV)": self.ui.doubleSpinBoxVbase.value(),
            "Number of circuits": int(self.ui.comboBoxNccts.currentText()),
            "Number of bundle conductors per phase": self.ui.spinBoxBundleCou.value(),
            "Bundle distance (m)": self.ui.doubleSpinBundleDistance.value(),
            "Length of the line (km)": self.ui.doubleSpinLineLength.value(),
            "ACSR conductor name": self.ui.comboBoxConductorName.currentText(),
            "C1 Phase A (centre)": [self.ui.doubleSpinBoxA1x.value(), self.ui.doubleSpinBoxA1y.value()],
            "C1 Phase B (centre)": [self.ui.doubleSpinBoxB1x.value(), self.ui.doubleSpinBoxB1y.value()],
            "C1 Phase C (centre)": [self.ui.doubleSpinBoxC1x.value(), self.ui.doubleSpinBoxC1y.value()],
            "C2 Phase A (centre)": [self.ui.doubleSpinBoxA2x.value(), self.ui.doubleSpinBoxA2y.value()],
            "C2 Phase B (centre)": [self.ui.doubleSpinBoxB2x.value(), self.ui.doubleSpinBoxB2y.value()],
            "C2 Phase C (centre)": [self.ui.doubleSpinBoxC2x.value(), self.ui.doubleSpinBoxC2y.value()],
        }

        try:
            dumpDict(dataDict, filepath=filepath)
        except (Exception, OSError, FileNotFoundError) as ex:
            self.errorMessage(text=str(ex))
        else:
            self.infoMessage("Success", f"Transmission line parameters saved successfully to file {filepath}")
            self.sigCreated.emit(filename)


    def loadCboxFilesToInherit(self, selectedText="Create New"):
        self.ui.comboBoxFilesToInherit.clear() 
        files = os.listdir(currDirectory + "\\userdata")
        if DEBUG:
            print(files)
        files = getExtensionsOnly(files, ".json")
        files = naturalSort(files)
        files.insert(0, "Create New")
        self.ui.comboBoxFilesToInherit.addItems(files)
        try:
            self.ui.comboBoxFilesToInherit.setCurrentIndex(files.index(selectedText))
        except ValueError: # pass if the selected text is not in cbox
            pass

def app():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    win = creatorWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app()