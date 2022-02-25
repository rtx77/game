from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import QtWidgets

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def click(self):
        global map_name
        map_name = self.textbox.text()

    def initUI(self):

        self.setGeometry(400,400,400,300)
        self.setWindowTitle('Message box')
        self.setFixedSize(400, 300)
        self.textbox = QtWidgets.QLineEdit(self)
        self.textbox.move(100, 100)
        self.textbox.resize(180, 40)
        button = QtWidgets.QPushButton(self)
        button.setText("MAP name")
        button.move(150, 200)
        button.clicked.connect(self.click)
        self.show()


    def closeEvent(self, event1):
        global dop_window

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            dop_window = True
            self.close()
        else:
            event1.ignore()