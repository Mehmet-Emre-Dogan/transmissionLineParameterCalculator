from common import *
import calculate
import create
import txt2json

from guiFiles.mainGui import Ui_MainWindow as mainMainWindow

currDirectory = os.path.dirname(__file__)

class myWindow(myWindowSkeleton):
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
        # self.ui.comboBox.currentIndexChanged.connect(self.calc)
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
            case "Online documentation":
                self.showHelpOnline()
            case "Offline help":
                self.showHelpOffline()

    def loadCbox(self, selectedText=DEFAULT_CBOX_TEXT):
        print("hi")
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
    
    def calc(self):
        if self.ui.comboBox.currentText() == DEFAULT_CBOX_TEXT:
            return # do not calculate, exit immediately

        try:
            res = calculate.calculate(currDirectory + "\\userdata\\" + self.ui.comboBox.currentText())
        except ZeroDivisionError as zde:
            zde = str(zde)
            self.ui.rpu.setText(zde)
            self.ui.xpu.setText(zde)
            self.ui.bpu.setText(zde)
            self.ui.lbl_r.setText(zde)
            self.ui.lbl_x.setText(zde)
            self.ui.lbl_b.setText(zde)
            self.errorMessage("Zero division error!", "Division by zero occured while calculating")
        except FileNotFoundError as fnfe:
            self.errorMessage(str(fnfe))

        else:
            self.ui.rpu.setText(str(res["R_pu"]) + " pu")
            self.ui.xpu.setText(str(res["X_pu"]) + " pu")
            self.ui.bpu.setText(str(res["B_pu"]) + " pu")
            self.ui.lbl_r.setText(str(res["R"]) + " Ω")
            self.ui.lbl_x.setText(str(res["X_L"]) + " Ω")
            self.ui.lbl_b.setText(str(res["B_C"]) + " S")

    def makefile(self):
        self.creatorWindow = create.creatorWindow()
        self.creatorWindow.show()
        self.creatorWindow.sigCreated.connect(self.loadCbox)
        self.creatorWindow.sigCreated.connect(self.calc)

    def txt2json(self):
        self.txt2jsonWindow = txt2json.txt2jsonWindow()
        self.txt2jsonWindow.show()
        self.txt2jsonWindow.sigCreated.connect(self.loadCbox)
        self.txt2jsonWindow.sigCreated.connect(self.calc)


    ################################
    """Help displayers"""
    ################################

    def showHelpOnline(self, lang="EN"):
        if lang == "TR":
            os.system('start https://github.com/Mehmet-Emre-Dogan/transmissionLineParameterCalculator/blob/main/BEN%C4%B0OKU.md')
        else:
           os.system('start https://github.com/Mehmet-Emre-Dogan/transmissionLineParameterCalculator/blob/main/README.md')

    def showHelpOffline(self, lang="EN"):
        try:
            if lang == "TR":
                os.system(f'start notepad.exe "{currDirectory}\\benioku.txt"')
            else:
                os.system(f'start notepad.exe "{currDirectory}\\readme.txt"')
        except (Exception, OSError, FileNotFoundError) as err:
            if lang == "TR":
                self.errorMessage(title="Çevrimdışı yardım görüntülenemiyor", text="'benioku.txt' dosyasını sildiniz mi?")
            else:
                self.errorMessage(title="Unable to show offline help", text="Did you deleted 'readme.txt' file?")



def app():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    win = myWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app()