# PyQt去边框以及移动问题

## 步骤

- 搭建基础PyQt架子

  ```python
  from PyQt5.QtWidgets import QApplication, QWidget
  import sys
  
  class MainWiondw(QWidget):
      def __init__(self):
          super().__init__()
  
  if __name__ == "__main__":
      app = QApplication(sys.argv)
      w = MainWiondw()
      w.show()
      sys.exit(app.exec_())
  ```

- 设置去边框参数

  ```python
  self.setWindowFlags(Qt.FramelessWindowHint)
  ```

- 重写鼠标按压、释放、移动事件

  ```python
  def mousePressEvent(self, event):
      if event.button()==Qt.LeftButton:
          self.m_flag=True
          self.m_Position=event.globalPos()-self.pos()
          event.accept()
          self.setCursor(QCursor(Qt.OpenHandCursor))
  
  def mouseMoveEvent(self, QMouseEvent):
      if Qt.LeftButton and self.m_flag:  
          self.move(QMouseEvent.globalPos()-self.m_Position)
          QMouseEvent.accept()
  def mouseReleaseEvent(self, QMouseEvent):
      self.m_flag=False
      self.setCursor(QCursor(Qt.ArrowCursor))
  ```

  

## 代码

```python
'''
@Author: skypeee
@LastEditors: skypeee
@Description: PrintScreen
@Date: 2019-11-18 08:59:09
'''
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent, QCursor
import sys

class MainWiondw(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  #更改鼠标图标
            
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:  
            self.move(QMouseEvent.globalPos()-self.m_Position)#更改窗口位置
            QMouseEvent.accept()
            
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QCursor(Qt.ArrowCursor))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWiondw()
    w.show()
    sys.exit(app.exec_())
```

