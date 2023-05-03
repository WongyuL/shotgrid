import os
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, QPushButton, QApplication


class FileView(QWidget):
    def __init__(self, folder_paths):
        super().__init__()
        print(f"folder_paths type: {type(folder_paths)}")
        self.file_data = []
        if isinstance(folder_paths, str):
            folder_paths = [folder_paths]
        elif isinstance(folder_paths, tuple):
            folder_paths = list(folder_paths)
        for folder_path in folder_paths:
            print(f"folder_path type: {type(folder_path)}")
            self.file_data += self.get_file_data(folder_path)
        self.init_ui()

    # def get_file_data(self, folder_data):
    #     folder_path = folder_data[0]
    #     file_data = []
    #     for file_name in os.listdir(folder_path):
    #         if file_name.endswith('.jpg'):
    #             name = file_name[:-4]
    #             thumbnail_path = os.path.join(folder_path, file_name)
    #             blender_path = os.path.join(folder_path, name + '.blend')
    #             if os.path.exists(blender_path):
    #                 file_data.append({'name': name, 'thumbnail_path': thumbnail_path, 'blender_path': blender_path})
    #     return file_data
    def get_file_data(self, folder_paths):
        file_data = []
        for folder_path in folder_paths:
            if os.path.isdir(folder_path):
                for file_name in os.listdir(folder_path):
                    file_path = os.path.join(folder_path, file_name)
                    if os.path.isfile(file_path):
                        file_size = os.path.getsize(file_path)
                        file_data.append((file_name, file_size))
        return file_data
        # for file_name in os.listdir(folder_path):
        #     print(f"file_name: {file_name}")
        #     if file_name.endswith('.blender'):
        #         name = os.path.splitext(file_name)[0]
        #         thumbnail_path = os.path.join(folder_path, name + '.jpg')
        #         blender_path = os.path.join(folder_path, file_name)
        #         file_data.append({
        #             'name': name,
        #             'thumbnail_path': thumbnail_path,
        #             'blender_path': blender_path
        #         })
        # 
        # return files

    def init_ui(self):
        self.setWindowTitle('File Viewer')
        self.setGeometry(100, 100, 800, 600)

        # create main layout
        main_layout = QVBoxLayout()

        # create scroll area
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        # create widget to hold all thumbnails
        thumbnails_widget = QWidget(scroll_area)
        thumbnails_layout = QHBoxLayout()

        # set number of rows and columns
        rows = 4
        cols = 3

        # calculate thumbnail size based on number of rows and columns
        thumbnail_width = int(self.width() / cols)
        thumbnail_height = int(thumbnail_width * 0.8)

        # create thumbnails
        for i, data in enumerate(self.file_data):
            thumbnail_pixmap = QPixmap(data['thumbnail_path']).scaled(thumbnail_width, thumbnail_height)
            thumbnail_label = QLabel(self)
            thumbnail_label.setPixmap(thumbnail_pixmap)


            # create label for file name
            file_name_label = QLabel(data['name'], self)
            file_name_label.setAlignment(Qt.AlignCenter)

            # create button to open blender file
            open_button = QPushButton('Open Blender', self)
            open_button.clicked.connect(lambda state, path=data['blender_path']: self.open_blender(path))

            # create layout for thumbnail
            thumbnail_layout = QVBoxLayout()
            thumbnail_layout.addWidget(thumbnail_label)
            thumbnail_layout.addWidget(file_name_label)
            thumbnail_layout.addWidget(open_button)

            # add thumbnail to thumbnails layout
            thumbnails_layout.addLayout(thumbnail_layout)

            # add spacer to make layout more flexible
            if (i + 1) % cols == 0:
                thumbnails_layout.addStretch()

        # set thumbnails widget layout
        thumbnails_widget.setLayout(thumbnails_layout)

        # set thumbnails widget as scroll area widget
        scroll_area.setWidget(thumbnails_widget)

        # add scroll area to main layout
        main_layout.addWidget(scroll_area)

        # set main layout
        self.setLayout(main_layout)

    def resizeEvent(self, event):
        self.init_ui()

    def open_blender(self, blender_path):
        os.system('blender "' + blender_path + '"')



