from common import *
from guiFiles.txtToJsonGui import Ui_MainWindow as txt2jsonWind

class txt2jsonWindow(QtWidgets.QMainWindow):
    sigCreated = pyqtSignal(str)
    def __init__(self):
        super(txt2jsonWindow, self).__init__()
        self.ui = txt2jsonWind()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('img.png'))
        
    def save(self):

        self.sigCreated.emit("data1.json")
    def save(self):
        if not self.ui.lineEditFileName.text():
            customDT = datetime.datetime.now().strftime('%Y-%m-%d_%H.%M.%S')
            self.ui.lineEditFileName.setText("TL_" + customDT + ".json")            
        
        filepath = currDirectory + "\\userdata\\" + self.ui.lineEditFileName.text()
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
            self.sigCreated.emit("data1.json")
def app():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    win = txt2jsonWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app()