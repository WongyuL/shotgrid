import os
import sys
from test_model import Model
# from Library import View
from PySide2.QtWidgets import QMainWindow
from PySide2 import QtWidgets, QtGui, QtCore


class Library(QMainWindow):
    def __init__(self):
        super().__init__()

        self.model = Model("C:\\chunsik")  # Base Folder
        self.model.search()  # find .jpg / .blend
        # self.view = View()
        # self.ss = Stylesheet()

        self.setWindowTitle("Library") # UI title name
        self.setGeometry(350, 200, 1280, 720)

        self.my_button = QtWidgets.QPushButton('Library', self)  # Button name
        self.my_button.setFixedSize(150, 100)
        self.my_button.move(550, 310)
        # self.ss.style1(self.my_button)
        self.my_button.clicked.connect(self.my_button_clicked) # button connect

        self.setMinimumSize(QtCore.QSize(800, 600)) # 화면 최소 사이즈 설정
        self.resizeEvent = self.handleResize # 이벤트 핸들러 설정
        self.my_button_clicked() # 버튼 눌려잇~!

    def my_button_clicked(self):
        screen_width = self.width() # 화면 사이즈에 맞는 width 계산
        max_columns = max(1, screen_width // 300) # 스크린 사이즈에서 300으로 나눈 열 사이즈

        widget = QtWidgets.QWidget()
        layout = QtWidgets.QGridLayout(widget)
        row = 0
        col = 0

        # 초기값 설정

        for path, url, filename in zip(self.model.list_path, self.model.list_blender_path, self.model.file_name):
            # 필요한 정보값 3개 묶기
            pixmap = QtGui.QPixmap(path)
            label = QtWidgets.QLabel()
            label.setPixmap(pixmap.scaledToWidth(250, QtCore.Qt.SmoothTransformation))
            label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            label.setAlignment(QtCore.Qt.AlignCenter)
            label.mousePressEvent = lambda event, url=url: self.open_image(url)
            # self.ss.style2(label)
            # 이벤트 발생 시 open_image에 url 연결
            layout.addWidget(label, row, col)

            file_label = QtWidgets.QLabel(filename)
            # self.ss.style3(file_label)
            file_label.setAlignment(QtCore.Qt.AlignCenter)
            layout.addWidget(file_label, row + 1, col)

            col += 1
            if col == max_columns:
                row += 2
                col = 0

        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(widget)
        self.setCentralWidget(scroll_area)

    def open_image(self, url):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl.fromLocalFile(url))

    def handleResize(self, event):
        layout = self.centralWidget().widget().layout()
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().setParent(None)
        self.my_button_clicked()


def main():
    app = QtWidgets.QApplication()
    myapp = Library()
    myapp.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()