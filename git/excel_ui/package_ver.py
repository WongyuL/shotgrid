import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic


class Form(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.ui = uic.loadUi("ui.ui", self)
        self.ui.show()

    def init_widget(self):
        self.setWindowTitle("Signal Slot")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())