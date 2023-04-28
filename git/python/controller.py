from PyQt5.QtWidgets import QApplication
from model import FileModel
from view import FileView

class FileController:
    def __init__(self, folder_path):
        self.model = FileModel(folder_path)
        self.view = FileView(self.model.file_data)
        self.view.show()

if __name__ == '__main__':
    folder_paths = ['C://chunsik//']
    app = QApplication([])
    for folder_path in folder_paths:
        controller = FileController(folder_path)
    app.exec_()
