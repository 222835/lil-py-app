import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Magic 8 Ball")
        self.setWindowIcon(QtGui.QIcon('icon.png'))

        self.magic8ball = ["Yes, definetly", "No!!", "Perchance...", "Ask me later", "idk", "OMG YES", "mmmm i would think abt it"]

        self.button = QtWidgets.QPushButton("New answer")
        self.text = QtWidgets.QLabel("Ask and you shall get an answer...",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.magic8ball))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())