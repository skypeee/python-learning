#  PyQt5 布局

## 布局基本套路

1. 创建布局对象

   ```python
   hLayout = QHBoxLayout() # 创建水平布局对象
   ```

2. 将控件添加至布局

   ```python
   hLayout.addWidget(btn1) # 参数为要加入的控件
   ```

3. 如果有多层布局，将子布局添加到主布局下

   ```python
   hLayout.addLayout(layout1)
   ```

4. 将布局设置为窗体布局

   ```python
   self.setLayout(hLayout)
   ```

## 5种布局

### 绝对布局

- PS：写为绝对布局其实为没啥布局，自己设置按钮在窗体的绝对位置

- 效果

  ![绝对布局](C:\workspace\笔记\pyqt5\窗体布局\绝对布局.png)

- 代码

  ```python
  from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton, QHBoxLayout, QLineEdit
  from PyQt5.QtCore import Qt
  import sys
  class testWindow(QWidget):
      def __init__(self):
          super().__init__()
          self.initUI()
  
      def initUI(self):
          # 创建控件，第二个参数为父窗体，绝对布局需要将控件的父窗体指定为主窗体，否则会创建新的窗体
          btn3 = QPushButton("按钮3", self)
          label3 = QLabel("标签3", self)
          lineEdit3 = QLineEdit("输入框3", self)
  		# 设置窗体的位置
          btn3.move(30,30)
          label3.move(60, 60)
          lineEdit3.move(80, 80)
  		# 设置窗体的横纵坐标（从屏幕左上角开始计算），窗体大小
          self.setGeometry(300,300,200,200)
  
  if __name__ == "__main__":
      # 创建QT应用对象
      app = QApplication(sys.argv)
      #创建窗体对象
      w = testWindow()
      # 显示窗体
      w.show()
      # 进入进程循环
      sys.exec(app.exec_())
  ```

  

### 水平布局QHBoxLayout

- 效果

![水平布局](C:\workspace\笔记\pyqt5\窗体布局\水平布局.png)

- 代码

  ```python
  from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton, QHBoxLayout, QLineEdit
  from PyQt5.QtCore import Qt
  import sys
  class testWindow(QWidget):
      def __init__(self):
          super().__init__()
          self.initUI()
      
      def initUI(self):
          
  		# 创建布局对象
          self.hLayout = QHBoxLayout()
  		# 创建控件
          self.btn1 = QPushButton("按钮1")
          self.label1 = QLabel("标签1")
          self.lineEdit1 = QLineEdit("输入框1")
  
          # 将控件添加进入布局中，第二个参数代表权重
          self.hLayout.addWidget(self.btn1, 1)
          self.hLayout.addWidget(self.label1, 3)
          self.hLayout.addWidget(self.lineEdit1, 5)
          # 设置主窗体布局
          self.setLayout(self.hLayout)
  
  if __name__ == "__main__":
    # 创建QT应用对象
      app = QApplication(sys.argv)
      #创建窗体对象
      w = testWindow()
      # 显示窗体
      w.show()
      # 进入进程循环
      sys.exec(app.exec_())
  ```

### 垂直布局QVBoxLayout

- 效果

  ![垂直布局](C:\workspace\笔记\pyqt5\窗体布局\垂直布局.png)

- 代码

  ```python
  from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton, QHBoxLayout, QLineEdit
  from PyQt5.QtCore import Qt
  import sys
  class testWindow(QWidget):
      def __init__(self):
          super().__init__()
          self.initUI()
  
      def initUI(self):
          
          # 创建垂直布局对象
          self.vLayout = QVBoxLayout()
          # 设置窗体大小
          self.resize(800,200)
  		# 创建控件
          self.btn2 = QPushButton("按钮2")
          self.label2 = QLabel("标签2")
          self.lineEdit2 = QLineEdit("输入框2")
          # 将控件加入布局， 第二个参数为权值，第三个参数为位置，如果不加第三个参数的话控件会自适应，加了之后会保持原始大小
          self.vLayout.addWidget(self.btn2, 0, Qt.AlignLeft|Qt.AlignTop)
          self.vLayout.addWidget(self.label2, 0, Qt.AlignLeft|Qt.AlignTop)
          self.vLayout.addWidget(self.lineEdit2 ,0 , Qt.AlignRight|Qt.AlignBottom)
  		# 设置主窗体布局
          self.setLayout(self.vLayout)
  
  if __name__ == "__main__":
      # 创建QT应用对象
      app = QApplication(sys.argv)
      #创建窗体对象
      w = testWindow()
      # 显示窗体
      w.show()
      # 进入进程循环
      sys.exec(app.exec_())
  ```

### 网格布局QGridLayout 

- 效果

  ![网格布局](C:\workspace\笔记\pyqt5\窗体布局\网格布局.png)

- 代码

  ```python
  from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton, QHBoxLayout, QLineEdit
  from PyQt5.QtCore import Qt
  import sys
  class testWindow(QWidget):
      def __init__(self):
          super().__init__()
          self.initUI()
  
      def initUI(self):
          
          # 网格布局
          grid = QGridLayout()
          # 将布局设置为主窗体的布局
          self.setLayout(grid)
  		# 创建网格列表
          names = ['A', 'B', '', 'D',
                   'E', 'F', 'G', 'H',
                   '8', '9', '10', 'J',
                   '4', '5', '6', '7',
                   '0', '1', '2', '3']
  		#创建4X5的矩阵
          positions = [(i,j) for i in range(5) for j in range(4)]
          # 进入循环，循环从names中解包出名称
          for position, name in zip(positions, names):
              if name == "":
                  continue
              # 创建控件
              button = QPushButton(name)
              # 将控件添加至网格布局中
              grid.addWidget(button, *position)
          # 设置窗体标题
          self.setWindowTitle("网格布局管理")
  
  if __name__ == "__main__":
      # 创建QT应用对象
      app = QApplication(sys.argv)
      #创建窗体对象
      w = testWindow()
      # 显示窗体
      w.show()
      # 进入进程循环
      sys.exec(app.exec_())
  ```

### 表单布局QFormLayout 

- 效果

  ![表单布局](C:\workspace\笔记\pyqt5\窗体布局\表单布局.png)

- 代码

  ```python
  from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton, QHBoxLayout, QLineEdit, QTextEdit
  from PyQt5.QtCore import Qt
  import sys
  class testWindow(QWidget):
      def __init__(self):
          super().__init__()
          self.initUI()
  
      def initUI(self):
          # 创建表单布局
          fLayout = QFormLayout()
  		# 创建控件
          personLabel = QLabel("申请人")
          authorLabel = QLabel("提交人")
          contextLable = QLabel("内容")
          personEdit = QLineEdit()
          authorEdit = QLineEdit()
          contextEdit = QTextEdit()
  		# 将每行表单信息添加到控件
          fLayout.addRow(personLabel, personEdit)
          fLayout.addRow(authorLabel, authorEdit)
          fLayout.addRow(contextLable, contextEdit)
  		# 将布局设置为主窗体布局
          self.setLayout(fLayout)
  
  if __name__ == "__main__":
      # 创建QT应用对象
      app = QApplication(sys.argv)
      #创建窗体对象
      w = testWindow()
      # 显示窗体
      w.show()
      # 进入进程循环
      sys.exec(app.exec_())
  ```

  

