import serial
import time

class Esp32Uart:
    def __init__(self, port='COM1', baudrate=115200):
        """
        初始化串口通信
        :param port: 串口号，默认为'COM3'
        :param baudrate: 波特率，默认为9600
        """
        self.port = port
        self.baudrate = baudrate
        try:
            self.ser = serial.Serial(self.port, self.baudrate)
            print(f"Serial port {self.port} opened successfully.")
        except serial.SerialException as e:
            print(f"Error opening serial port: {e}")

    def send_data(self, data):
        """
        向串口发送数据
        :param data: 要发送的数据，可以是字符串或其他可编码为字节串的对象
        """
        if self.ser and self.ser.is_open:
            try:
                self.ser.write(data)
                print(f"Sent: {data}")
            except Exception as e:
                print(f"Error sending data: {e}")
        else:
            print("Serial port is not open.")

    def close(self):
        """关闭串口"""
        if self.ser and self.ser.is_open:
            self.ser.close()
            print(f"Serial port {self.port} closed.")
        else:
            print("Serial port is already closed.")

if __name__ == "__main__":
    # 创建一个SerialCommunicator实例
    communicator = SerialCommunicator()

    try:
        while True:
            user_input = input("Enter message to send (or 'exit' to quit): ")
            if user_input.lower() == 'exit':
                break
            # 调用send_data方法发送数据
            communicator.send_data(user_input)
            time.sleep(1)  # 可选的延时
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        # 确保在退出前关闭串口
        communicator.close()