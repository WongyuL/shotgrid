import sys
import os
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel
from PySide2.QtGui import QPixmap
from model import FileModel


class ModelViewController(QMainWindow):
    def __init__(self):
        super().__init__()

        # Instantiate the model
        self.model = FileModel('C:\\chunsik\\')

        # Get the model data
        self.model_data = self.model.get_file_data()

        # Create QLabel widgets to display the thumbnails
        self.image_labels = []
        for idx, data in enumerate(self.model_data):
            label = QLabel(self)
            label.setPixmap(QPixmap(data[1]))
            label.move(10, 10 + idx * 250)
            self.image_labels.append(label)

        # Connect the labels to their respective Blender files
        for idx, data in enumerate(self.model_data):
            self.image_labels[idx].mousePressEvent = self.create_click_handler(data[2])

    def create_click_handler(self, blender_path):
        def handle_click(event):
            os.system(f'blender {blender_path}')
        return handle_click


if __name__ == '__main__':
    app = QApplication(sys.argv)
    controller = ModelViewController()
    controller.show()
    sys.exit(app.exec_())
