import os
from datetime import datetime


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
        return file_data

# if __name__ == '__main__':
#     test = FileModel('C://chunsik//')
#     test.get_file_data()
#
# import os
#
# class Model:
#     def __init__(self, dirname):
#         self.dirname = dirname
#         self.list_path = []
#         self.list_blender_path = []
#         self.file_name = []
#
#     def search(self):
#         try:
#             filenames = os.listdir(self.dirname)
#             # print(self.dirname)
#             for filename in filenames:
#                 full_filename = os.path.join(self.dirname, filename)
#                 # print(full_filename)
#                 if os.path.isdir(full_filename):
#                     # print(full_filename)
#                     sub_search = Model(full_filename)
#                     sub_search.search()
#                     self.list_path.extend(sub_search.list_path)
#                     self.list_blender_path.extend(sub_search.list_blender_path)
#                     self.file_name.extend(sub_search.file_name)
#                 else:
#                     ext = os.path.splitext(full_filename)[-1]
#                     # print(ext)
#                     parent_folder = os.path.basename(self.dirname)
#                     # print(parent_folder)
#                     if ext == '.jpg' and parent_folder == os.path.splitext(filename)[0]:
#                         self.list_path.append(full_filename)
#                         self.file_name.append(parent_folder)
#                         # print(self.list_path)
#                     if ext == '.blend' and parent_folder == os.path.splitext(filename)[0]:
#                         self.list_blender_path.append(full_filename)
#                         # print(self.list_blender_path)
#         except PermissionError:
#             pass
#
# if __name__ == '__main__':
#     model = Model("C:\\Users\\admin\\Documents\\Library")
#     model.search()
#     # print(model.list_path)
#     # print(model.list_blender_path)
#     # print(model.file_name)