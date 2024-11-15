import sys
from sha256sum import sha256sum
from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QPushButton,
    QFileDialog, QMessageBox, QLineEdit,
    QLabel)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class HashChecker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle('HashChecker')
        self.setFixedSize(590,140)
        self.handleLabel()
        self.handleButton()
        self.handleEdit()


    def findFile(self):
        self.file_path, _ = QFileDialog.getOpenFileName(self, '파일 선택', '', 'All Files(*)')
        if self.file_path:
            self.file_hash_result = sha256sum(self.file_path)
            QMessageBox.information(self, '파일 해시 결과', self.file_hash_result)
            self.file_hash_label.setText(self.file_hash_result)


    def compareHash(self):
        self.compared_hash = self.hash_line_edit.text()

        if self.file_path and self.hash_line_edit.text():
            if self.compared_hash == self.file_hash_result:
                QMessageBox.information(self, '결과', '해시가 동일합니다.')
            else :
                 QMessageBox.warning(self, '결과', '해시가 동일하지 않습니다.')
        else :
            QMessageBox.information(self, '알림', '파일 및 해시를 지정해주세요')


    def handleLabel(self):
        self.file_hash_label = QLabel('파일 해시 :', self)
        self.file_hash_label.move(10, 10)

        self.file_hash_label = QLabel(self)
        self.file_hash_label.setFixedWidth(500)
        self.file_hash_label.move(70, 10)
        self.file_hash_label.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.hash_input_label = QLabel('해시 입력 :', self)
        self.hash_input_label.move(10, 50)


    def handleButton(self):
        self.find_file_btn = QPushButton(self)
        self.find_file_btn.setIcon(QIcon('./folder.png'))
        self.find_file_btn.setIconSize(self.find_file_btn.sizeHint())
        self.find_file_btn.clicked.connect(self.findFile)
        self.find_file_btn.move(10, 100)

        self.compare_hash_btn = QPushButton('해시 비교', self)
        self.compare_hash_btn.clicked.connect(self.compareHash)
        self.compare_hash_btn.move(120, 100)


    def handleEdit(self):
        self.hash_line_edit = QLineEdit(self)
        self.hash_line_edit.setMaxLength(65)
        self.hash_line_edit.setFixedWidth(500)
        self.hash_line_edit.move(68, 50)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HashChecker()
    ex.show()
    app.exec()
