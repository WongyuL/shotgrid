# import os
# from collections import defaultdict
#
# class Model:
#     def __init__(self, dirname):
#         self.dirname = dirname
#         self.dict_path = defaultdict(list)
#
#     def search(self):
#         try:
#             filenames = os.listdir(self.dirname)
#             for filename in filenames:
#                 full_filename = os.path.join(self.dirname, filename)
#                 if os.path.isdir(full_filename):
#                     sub_search = Model(full_filename)
#                     sub_search.search()
#                     for folder_name, folder_paths in sub_search.dict_path.items():
#                         self.dict_path[folder_name].extend(folder_paths)
#                 else:
#                     ext = os.path.splitext(full_filename)[-1]
#                     if ext == '.jpg':
#                         parent_folder = os.path.basename(full_filename).split('.')[0]
#                         self.dict_path[parent_folder].append(full_filename)
#         except PermissionError:
#             pass

import os
from collections import defaultdict

class Model:
    def __init__(self, dirname):
        self.dirname = dirname
        self.list_path = []
        self.list_blender_path = []
        self.file_name = []

    def search(self):
        try:
            filenames = os.listdir(self.dirname)
            # print(self.dirname)
            for filename in filenames:
                full_filename = os.path.join(self.dirname, filename)
                # print(full_filename)
                if os.path.isdir(full_filename):
                    # print(full_filename)
                    sub_search = Model(full_filename)
                    sub_search.search()
                    self.list_path.extend(sub_search.list_path)
                    self.list_blender_path.extend(sub_search.list_blender_path)
                    self.file_name.extend(sub_search.file_name)
                else:
                    ext = os.path.splitext(full_filename)[-1]
                    # print(ext)
                    parent_folder = os.path.basename(self.dirname)
                    # print(parent_folder)
                    if ext == '.jpg' and parent_folder == os.path.splitext(filename)[0]:
                        self.list_path.append(full_filename)
                        self.file_name.append(parent_folder)
                        # print(self.list_path)
                    if ext == '.blend' and parent_folder == os.path.splitext(filename)[0]:
                        self.list_blender_path.append(full_filename)
                        # print(self.list_blender_path)
        except PermissionError:
            pass

if __name__ == '__main__':
    model = Model("C:\\chunsik\\")
    model.search()
    print(model.list_path)
    print(model.list_blender_path)
    print(model.file_name)

    print("어쩔 전자렌지")