from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QMainWindow

from apex_yolov5 import global_img_info
from apex_yolov5.KeyAndMouseListener import KMCallBack
from apex_yolov5.socket.config import global_config


class CircleWindow(QMainWindow):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.desktop_width = self.config.desktop_width
        self.desktop_height = self.config.desktop_height
        self.center = QPoint(self.config.desktop_width // 2, self.config.desktop_height // 2)
        self.radius = self.config.mouse_moving_radius
        self.setGeometry(0, 0, self.desktop_width, self.desktop_height)
        self.setWindowTitle("")
        self.setWindowFlags(Qt.Tool | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        KMCallBack.connect(KMCallBack("m", "right", self.update_circle, False))
        KMCallBack.connect(KMCallBack("m", "right", self.update_circle))

    def update_circle(self, pressed=False, toggle=False):
        if pressed:
            self.radius = self.config.aim_mouse_moving_radius
        else:
            self.radius = self.config.mouse_moving_radius
        self.radius = round(
            self.radius
            * max(
                global_img_info.get_current_img().shot_width / self.config.default_shot_width,
                global_img_info.get_current_img().shot_height / self.config.default_shot_height,
            ),
            2,
        )
        self.update()

    def update_circle_auto_change(self, radius):
        if self.radius != radius:
            self.radius = radius
            self.update()

    def init_form_config(self):
        self.desktop_width = self.config.desktop_width
        self.desktop_height = self.config.desktop_height
        self.center = QPoint(self.config.desktop_width // 2, self.config.desktop_height // 2)
        self.radius = self.config.mouse_moving_radius
        self.setGeometry(0, 0, self.desktop_width, self.desktop_height)
        if self.config.show_circle:
            self.show()
        else:
            self.hide()
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(Qt.red, 1, Qt.SolidLine))
        painter.drawEllipse(self.center, self.radius, self.radius)

    def close(self):
        KMCallBack.remove("m", "right")
        super().close()


circle_window: CircleWindow = None


def get_circle_window():
    global circle_window
    if circle_window is None:
        circle_window = CircleWindow(global_config)
    return circle_window


def destory_circle_window():
    global circle_window
    if circle_window is not None:
        circle_window.close()
        circle_window = None
