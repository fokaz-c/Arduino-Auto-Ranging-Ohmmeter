import random

import serial


class serialConnection:
    def __init__(self, port, baud_rate, timeout=1):
        self.port = port
        self.baud_rate = baud_rate
        self.timeout = timeout
        self.ser = None

    def open_connection(self):
        try:
            self.ser = serial.Serial(self.port, self.baud_rate, timeout=self.timeout)
            if self.ser.is_open:
                print('Serial port open')
        except serial.SerialException as e:
            print(f"Error opening serial port: {e}")

    def read_data(self):
        try:
            if self.ser and self.ser.is_open:
                # Read a line from the serial port
                data = self.ser.readline().decode('utf-8').strip()
                if data:
                    print(f"Received: {data}")
                    return data  # Return the received data
        except:
            pass
        return random.randrange(1, 10000, 10)

    def close_connection(self):
        if self.ser and self.ser.is_open:
            self.ser.close()
            print("Serial port closed")
