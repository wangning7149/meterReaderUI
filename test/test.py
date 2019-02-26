import sys
import UI.display as display
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog
from UI.display import Ui_MainWindow

class MainForm(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainForm,self).__init__()
        self.setupUi(self)
        self.choose_img.clicked.connect(self.openImg)

    def openImg(self):
        file,ok=QFileDialog.getOpenFileName(self, '打开', "D:/", "All Files (*);;Text Files (*.txt)")
        self.statusbar.showMessage(file)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow =MainForm()

    MainWindow.show()
    sys.exit(app.exec_())