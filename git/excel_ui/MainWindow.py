import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QUrl
from PySide2.QtGui import QDesktopServices
from urllib.parse import urlparse


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

    def handle_shotgrid_url(self, url):
        parsed_url = urlparse(url)
        path = parsed_url.path
        if path == '/create_xls':
            self.create_xls()


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    main_window = MainWindow()
    main_window.show()
    # Handle ShotGrid URLs
    if len(sys.argv) > 1:
        main_window.handle_shotgrid_url(sys.argv[1])
    sys.exit(app.exec_())
