from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow

class Widget(QMainWindow):        
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Generate.clicked.connect(self.buttonclick)
    def buttonclick(self, hereresult):
        self.ui.hereresult.setText("ніга дай")


app = QApplication([])
ex = Widget()
ex.show()
app.exec_()