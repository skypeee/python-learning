'''
@Author: skypeee
@LastEditors: skypeee
@Description: file content
@Date: 2019-11-19 14:53:38
'''
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout
from PyQt5.QtGui import QCursor, QMouseEvent
from PyQt5.QtCore import Qt
import sys


class testWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.btn1 = QPushButton("btn1")
        self.btn2 = QPushButton("btn2")
        self.btn3 = MyBtn(text="btn3")
        self.btn1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn2.setCursor(QCursor(Qt.CrossCursor))
        self.btn3.event

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.btn1)
        self.layout.addWidget(self.btn2)
        self.layout.addWidget(self.btn3)

        self.setLayout(self.layout)

    def test(self):
        print("ok")

class MyBtn(QPushButton):
    def __init__(self, text):
        super().__init__(text)
    
    def mouseMoveEvent(self, e):
        print("ok")
    
    def mousePressEvent(self, e):
        print("Not Ok")
    
    def enterEvent(self, a0):
        print("123")
        return super().enterEvent(a0)
    
    def leaveEvent(self, a0):
        print("321")
        return super().leaveEvent(a0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = testWindow()
    w.show()
    sys.exit(app.exec_())
