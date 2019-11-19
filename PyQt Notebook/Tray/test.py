'''
@Author: skypeee
@LastEditors: skypeee
@Description: file content
@Date: 2019-11-19 14:16:37
'''
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
        print(self.tray.showMessage("test","test", icon=0, msecs=100))
        self.tray.show
        self.tray.setToolTip("这是一个气泡提示信息！")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = TaryWiondw()
    sys.exit(app.exec_())