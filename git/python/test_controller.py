import sys
from PySide2.QtWidgets import QApplication, QWidget
from test_model import FileModel


class Form(QWidget):
    def __init__(self):
        super(Form, self).__init__()


app = QApplication([])
form = Form()
form.show()
sys.exit(app.exec_())