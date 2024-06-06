from PySide2 import QtCore, QtWidgets, QtGui
import sys
import random

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]
        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World")
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        self.button.clicked.connect(self.on_button_clicked)
    
    def on_button_clicked(self):
        self.text.setText(random.choice(self.hello))

app = QtWidgets.QApplication([])
widget = MyWidget()
widget.resize(800, 600)
widget.show()
sys.exit(app.exec_())