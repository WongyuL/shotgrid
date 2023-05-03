
import os


class FileModel:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.file_data = []
        self.blender_path = []

    def get_file_data(self):
        file_data = []
        for folder_name in os.listdir(self.folder_path):
            folder_path = os.path.join(self.folder_path, folder_name)
            if os.path.isdir(folder_path):
                thumbnail_path = os.path.join(folder_path, folder_name + '.jpg')
                blender_path = os.path.join(folder_path, folder_name + '.blend')
                if os.path.isfile(thumbnail_path) and os.path.isfile(blender_path):
                    file_data.append((folder_name, thumbnail_path, blender_path))
                    # print(file_data)
        return file_data


if __name__ == '__main__':
    test = FileModel('C:\\chunsik\\')
    test.get_file_data()