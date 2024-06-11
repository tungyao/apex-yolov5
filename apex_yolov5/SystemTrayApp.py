import os

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QMenu, QSystemTrayIcon


class SystemTrayApp:
    def __init__(self, main_window, config):
        self.main_window = main_window
        self.config = config
        if not QSystemTrayIcon.isSystemTrayAvailable():
            print("系统托盘不可用")
            return

        icon = QIcon("images/ag.ico")
        if icon.isNull():
            print("无效的图标")
            return

        self.show_action = QAction("显示应用", self.main_window)
        self.hide_action = QAction("隐藏应用", self.main_window)
        self.exit_action = QAction("退出", self.main_window)

        self.init_ui()

    def init_ui(self):
        self.tray_menu = QMenu(self.main_window)
        self.tray_menu.addAction(self.show_action)
        self.tray_menu.addAction(self.hide_action)
        self.tray_menu.addSeparator()
        self.tray_menu.addAction(self.exit_action)

        self.show_action.triggered.connect(self.show_app)
        self.hide_action.triggered.connect(self.hide_app)
        self.exit_action.triggered.connect(self.exit_app)

        self.tray_icon = QSystemTrayIcon(self.main_window)
        self.change_icon(self.config.ai_toggle)
        self.tray_icon.setContextMenu(self.tray_menu)
        # 添加 activated 信号的处理
        self.tray_icon.activated.connect(self.tray_activated)
        self.tray_icon.show()

    def show_app(self):
        self.config.set_config("show_config", True)
        self.config.save_config()
        self.main_window.show()
        self.main_window.showNormal()

    def hide_app(self):
        self.config.set_config("show_config", False)
        self.config.save_config()
        self.main_window.hide()

    def change_icon(self, open_status):
        # 在这里更改图标，例如，切换到另一个图标
        if open_status:
            self.tray_icon.setIcon(QIcon("images/ag.ico"))  # 切换到第二个图标
        else:
            self.tray_icon.setIcon(QIcon("images/close.ico"))  # 切换回第一个图标

    def tray_activated(self, reason):
        # 处理双击事件
        if reason == QSystemTrayIcon.double-click:
            if self.main_window.isHidden():
                self.show_app()
            else:
                self.hide_app()

    def exit_app(self):
        self.tray_icon.hide()
        os._exit(0)
