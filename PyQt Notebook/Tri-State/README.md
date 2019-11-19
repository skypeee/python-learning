## 鼠标事件

- 做GUI编程很常见的一个需求，要将按钮或者其他控件的光标移入、移出、按压时三种情况的控件样式都不一样，有些人把这三种情况叫做控件的三态
- 另一种情况需要更改光标的样式

## 光标

- 更改鼠标移入光标

  ```python
  self.btn.setCursor(QCursor(Qt.PointingHandCursor))
  ```

  | 参数               | 效果                 |
  | ------------------ | -------------------- |
  | PointingHandCursor | 变为手型             |
  | CrossCursor        | 变为十字型           |
  | ArrowCursor        | 变为箭头型           |
  | UpArrowCursor      | 变为向上箭头型       |
  | IBeamCursor        | 变为文本输入型       |
  | WaitCursor         | 变为等待型           |
  | BusyCursor         | 变为繁忙型           |
  | ForbiddenCursor    | 变为禁止型           |
  | WhatsThisCursor    | 变为问号型           |
  | SizeVerCursor      | 变为垂直拖拽型       |
  | SizeHorCursor      | 变为水平拖拽性       |
  | SizeBDiagCursor    | 变为对角线调整大小型 |
  | SizeAllCursor      | 变为移动对象型       |
  | SplitHCursor       | 变为水平拆分型       |
  | SplitVCursor       | 变为垂直拆分型       |
  | OpenHandCursor     | 变为打开型           |
  | ClosedHandCursor   | 变为关闭型           |
  | BlankCursor        | 变为空白型           |

## 鼠标移入事件

- 如果想要将控件的鼠标移入或者移出绑定函数、搞自己的功能，那就得写一个类继承此控件（QLable、QPushButton）然后重写此类的相关方法

  ```python
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
  ```

- 相关事件总结（由于个人时间有限无法全部查找测试其功能，这里整理了常用的一部分，都是简单英文组合，应该不难懂）

  | 事件                  | 作用             |
  | --------------------- | ---------------- |
  | enterEvent            | 鼠标移入触发     |
  | leaveEvent            | 鼠标离开触发     |
  | mouseDoubleClickEvent | 鼠标双击点击触发 |
  | mouseMoveEvent        | 鼠标移动触发     |
  | mousePressEvent       | 鼠标按压触发     |
  | mouseReleaseEvent     | 鼠标释放触发     |
  | keyPressEvent         | 键盘按下触发     |
  | keyReleaseEvent       | 键盘释放触发     |
  | closeEvent            | 关闭时触发       |
  | resizeEvent           | 设置大小时触发   |
  | showEvent             | 显示控件时触发   |
  | dragLeaveEvent        |                  |
  | dragMoveEvent         |                  |
  | dropEvent             |                  |
  | focusInEvent          |                  |
  | focusOutEvent         |                  |
  | hideEvent             |                  |
  | inputMethodEvent      |                  |
  | installEventFilter    |                  |
  | customEvent           |                  |
  | dragEvent             |                  |
  | actionEvent           |                  |
  | changeEvent           |                  |
  | childEvent            |                  |
  | contextMenuEvent      |                  |
  | moveEvent             |                  |
  | nativeEvent           |                  |
  | paintEvent            |                  |
  | removeEventFliter     |                  |
  | tabletEvent           |                  |
  | timerEvent            |                  |
  | wheelEvent            |                  |

  

- 详细代码

  ```python
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
  ```

  