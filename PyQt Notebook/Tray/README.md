# PyQt5创建托盘

## 使用到的包

1. QtWidgets.Qwidget、QtWidgets.QsystemTrayIcon、QtWidgets.QMenu、QtWidgets.QAction、QtWidgets.QApplication
2. QtGui.Qicon、QtGui.QColor、QtGui.QPixmap
3. sys

## 步骤

1. 创建PyQt基本套路

2. 创建QSystemTrayIcon托盘对象

   ```python
   self.tray = QSystemTrayIcon()
   ```

3. 创建QIcon对象，将其设置为Tray（托盘）图标

   ```python
   self.trayIconPix = QPixmap(16,16)
   self.trayIconPix.fill(QColor(100,100,100))
   self.Icon = QIcon(self.trayIconPix)
   self.tray.setIcon(self.Icon)
   ```

4. 创建QMenu（菜单）对象，创建QAction（行为）对象，将QAction（行为）对象添加至QMenu（菜单）对象中，相当于绑定点击事件

   ```python
   showAction = QAction("&Show", self, triggered = self.Show)
   quitAction = QAction("&Quit", self, triggered = self.Exit)
   self.trayMenu = QMenu(self)
   self.trayMenu.addAction(showAction)
   self.trayMenu.addSeparator()
   self.trayMenu.addAction(quitAction)
   ```

5. 将QMenu（菜单）对象设置到右键触发（setContextMenu）事件中

   ```python
   self.tray.setContextMenu(self.trayMenu)
   ```

## 问题

- 点击关闭叉叉按钮或者托盘右键出来的Quit虽然程序已经结束了，但是托盘图标还是会继续停留在系统托盘中，直到鼠标移到图标上才会消失
  - 解决：需要重写退出事件，在程序结束前需要先将QSystemTrayIcon对象内存清空

## 代码

```python
from PyQt5.QtWidgets import QApplication, QWidget, QSystemTrayIcon, QAction, QMenu
from PyQt5.QtGui import QIcon, QPixmap, QColor
import sys

class TaryWiondw(QWidget):
    def __init__(self):
        super().__init__()
        # 创建托盘对象
        self.tray = QSystemTrayIcon()

        # 创建QIcon对象，用于设置图标（图片过大会出错）
        self.trayIconPix = QPixmap(16,16)
        self.trayIconPix.fill(QColor(100,100,100))
        self.Icon = QIcon(self.trayIconPix)

        # 设置托盘图标（QIcon图标过大或者出错会导致托盘显示不出来）
        self.tray.setIcon(self.Icon)

        # 创建QAction
        showAction = QAction("&Show", self, triggered = self.Show)
        quitAction = QAction("&Quit", self, triggered = self.Exit)
        # 创建菜单对象
        self.trayMenu = QMenu(self)
        # 将动作对象添加到菜单
        self.trayMenu.addAction(showAction)
        # 增加分割线
        self.trayMenu.addSeparator()
        self.trayMenu.addAction(quitAction)
        # 将菜单栏加入到右键按钮中
        self.tray.setContextMenu(self.trayMenu)

    def Exit(self):
        # 点击关闭按钮或者点击退出事件会出现图标无法消失的bug，需要手动将图标内存清除
        self.tray = None
        sys.exit(app.exec_())

    def Show(self):
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = TaryWiondw()
    sys.exit(app.exec_())
```

