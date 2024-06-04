import ctypes

from apex_yolov5.log.Logger import Logger
from apex_yolov5.mouse_mover.MouseMover import MouseMover

# pip install pyserial
from apex_yolov5.socket.esp32_uart import Esp32Uart


class Esp32(MouseMover):
    def __init__(self, logger: Logger, mouse_mover_param):
        super().__init__(mouse_mover_param)
        self.logger = logger
        self.esp32u = Esp32Uart()

    def move_rp(self, x: int, y: int, re_cut_size=0):
        c = [x, y, '\n']
        self.esp32u.send_data(c)

    # """
    #    传入的应该是相对移动的xy距离
    # """
    def move(self, x: int, y: int):
        c = [x, y, '\n']
        self.esp32u.send_data(c)
    def destroy(self):
        self.esp32u.close()

