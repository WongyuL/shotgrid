
import os
import sys
from PySide2.QtWidgets import QWidget, QPushButton, QLabel, QGridLayout, QScrollArea
from PySide2 import QtWidgets, QtGui, QtCore
from test_model import FileModel


class Library(QWidget):
    """
    A QWidget-based application for browsing and opening Blender files.

    Attributes:
        model (FileModel): A FileModel instance representing the base folder to browse.
        max_columns (int): The maximum number of columns to display in the grid layout.
    """
    def __init__(self):
        """Initializes a new instance of the Library class."""

        super().__init__()

        self.model = FileModel("C:\\chunsik")

        self.setWindowTitle("Library")
        self.setGeometry(350, 200, 720, 480)

        self.setMinimumSize(QtCore.QSize(800, 600))

        screen_width = self.width()
        self.max_columns = max(1, screen_width // 300)
        self.update_layout()

    def update_layout(self):
        """Initializes a new instance of the Library class."""

        file_data = self.model.get_file_data()

        widget = QtWidgets.QWidget()
        layout = QtWidgets.QGridLayout(widget)
        row = 0
        col = 0

        # 초기값 설정

        for folder_name, thumbnail_path, blender_path in file_data:

            pixmap = QtGui.QPixmap(thumbnail_path)
            label = QtWidgets.QLabel()
            label.setPixmap(pixmap.scaledToWidth(250, QtCore.Qt.SmoothTransformation))
            label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            label.setAlignment(QtCore.Qt.AlignCenter)
            label.mousePressEvent = lambda event, url=blender_path: self.open_image(url)
            layout.addWidget(label, row, col)

            file_label = QtWidgets.QLabel(folder_name)
            file_label.setAlignment(QtCore.Qt.AlignCenter)
            layout.addWidget(file_label, row + 1, col)

            col += 1
            if col == self.max_columns:
                row += 2
                col = 0

        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(widget)
        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().addWidget(scroll_area)

    def open_image(self, url):
        """Opens a Blender file at the specified URL.

        Args:
            url (str): The URL of the Blender file to open.
        """
        QtGui.QDesktopServices.openUrl(QtCore.QUrl.fromLocalFile(url))

    def resizeEvent(self, event):
        """Overrides the base class's resizeEvent method to handle resizing the application window."""

        self.handleResize(event)

    def handleResize(self, event):
        """Handles the resizing of the application window.

        Args:
            event (QEvent): The resize event to handle.
        """
        layout = self.layout()
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().setParent(None)

        screen_width = self.width()
        self.max_columns = max(1, screen_width // 300)
        self.update_layout()


def main():
    app = QtWidgets.QApplication()
    myapp = Library()
    myapp.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
