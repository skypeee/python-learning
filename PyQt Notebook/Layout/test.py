'''
@Author: skypeee
@LastEditors: skypeee
@Description: file content
@Date: 2019-11-20 09:18:34
'''
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton, QHBoxLayout, QLineEdit,\
    QVBoxLayout, QGridLayout, QTextEdit, QFormLayout
from PyQt5.QtCore import Qt
import sys

class testWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):

        # 水平布局

        # self.hLayout = QHBoxLayout()

        # self.btn1 = QPushButton("按钮1")
        # self.label1 = QLabel("标签1")
        # self.LineEdit1 = QLineEdit("输入框1")

        # 第二个参数代表权重

        # self.hLayout.addWidget(self.btn1, 1)
        # self.hLayout.addWidget(self.label1, 3)
        # self.hLayout.addWidget(self.LineEdit1, 5)

        # self.setLayout(self.hLayout)

        # 垂直布局

        # self.vLayout = QVBoxLayout()
        # self.resize(800,200)

        # self.btn2 = QPushButton("按钮2")
        # self.label2 = QLabel("标签2")
        # self.LineEdit2 = QLineEdit("输入框2")
        # self.vLayout.addWidget(self.btn2)
        # self.vLayout.addWidget(self.label2, 0, Qt.AlignLeft|Qt.AlignTop)
        # self.vLayout.addWidget(self.LineEdit2 ,0 , Qt.AlignRight|Qt.AlignBottom)

        # self.setLayout(self.vLayout)

        # 绝对布局

        # btn3 = QPushButton("按钮3", self)
        # label3 = QLabel("标签3", self)
        # LineEdit3 = QLineEdit("输入框3", self)

        # btn3.move(30,30)
        # label3.move(60, 60)
        # LineEdit3.move(80, 80)

        # self.setGeometry(1300,300,200,200)

        # 网格布局1

        # grid = QGridLayout()

        # self.setLayout(grid)

        # names = ['A', 'B', '', 'D',
        #          'E', 'F', 'G', 'H',
        #          '8', '9', '10', 'J',
        #          '4', '5', '6', '7',
        #          '0', '1', '2', '3']

        # positions = [(i,j) for i in range(5) for j in range(4)]
        # for position, name in zip(positions, names):
        #     if name == "":
        #         continue
        #     button = QPushButton(name)
        #     grid.addWidget(button, *position)
        # self.move(300, 150)
        # self.setWindowTitle("网格布局管理")

        # 网格布局2

        # personLabel = QLabel("申请人")
        # authorLabel = QLabel("提交人")
        # contextLable = QLabel("内容")

        # personEdit = QLineEdit()
        # authorEdit = QLineEdit()
        # contextEdit = QTextEdit()

        # grid = QGridLayout()
        # grid.setSpacing(10)

        # grid.addWidget(personLabel, 1, 0)
        # grid.addWidget(personEdit, 1, 1)

        # grid.addWidget(authorLabel, 2, 0)
        # grid.addWidget(authorEdit, 2, 1)

        # grid.addWidget(contextLable, 3,0)
        # # 最后两个参数表示的是 所占的行和所占的列
        # grid.addWidget(contextEdit,3, 1, 5,1)

        # self.setLayout(grid)

        fLayout = QFormLayout()

        personLabel = QLabel("申请人")
        authorLabel = QLabel("提交人")
        contextLable = QLabel("内容")

        personEdit = QLineEdit()
        authorEdit = QLineEdit()
        contextEdit = QTextEdit()

        fLayout.addRow(personLabel, personEdit)
        fLayout.addRow(authorLabel, authorEdit)
        fLayout.addRow(contextLable, contextEdit)

        self.setLayout(fLayout)


if __name__  == "__main__":
    app = QApplication(sys.argv)
    w = testWindow()
    w.show()
    sys.exit(app.exec_())
