---

# FastAPI Serial Connection Project

This project demonstrates how to create a FastAPI application that reads data from a serial port (e.g., an Arduino) using the `pyserial` library. The application provides REST endpoints to interact with the serial device and return data to the user.

## Project Structure

```
/project-root/
├── /src/
│   ├── __init__.py            # Marks the src directory as a package
│   ├── serialConnection.py     # Contains the serial connection logic
│   └── main.py                 # FastAPI application
├── requirements.txt            # Dependencies
└── README.md                   # Project documentation
```

## Prerequisites

Before running this project, ensure that you have Python 3.x installed and have the following packages:

- `fastapi`
- `uvicorn`
- `pyserial`

You can install them using `pip`:

```bash
pip install fastapi uvicorn pyserial
```

## Files Overview

### 1. `serialConnection.py`

This file contains the `serialConnection` class, which manages the serial connection, opens/closes the connection, and reads data from the serial device (like Arduino).

#### Example:

```python
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
        if self.ser and self.ser.is_open:
            data = self.ser.readline().decode('utf-8').strip()
            return data
        return "No data"

    def close_connection(self):
        if self.ser and self.ser.is_open:
            self.ser.close()
            print("Serial port closed")
```

### 2. `main.py`

The FastAPI application is defined in `main.py`. It interacts with the `serialConnection` class to read data from the serial port and return it through REST API endpoints.

#### Example:

```python
from typing import Union
from fastapi import FastAPI
from src.serialConnection import serialConnection

app = FastAPI()
sc = serialConnection('COM3', 9600)  # Update the port and baud rate as necessary
sc.open_connection()

@app.get("/")
async def read_root():
    data = sc.read_data()
    return {"data": data}
```

## Running the Project

1. **Clone the Repository** (if applicable) or download the project files.

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the FastAPI Application**:

   Make sure you are in the project root directory, and run the following command:

   ```bash
   uvicorn src.main:app --reload
   ```

   The `--reload` flag enables automatic reloading of the server when code changes.

4. **Access the API**:

   Once the server is running, you can access the endpoints at:

   - Root endpoint: `http://127.0.0.1:8000/` (this will return the data read from the serial device).

5. **Close the Serial Connection**:

   The serial connection will be closed when the application is interrupted (e.g., using `Ctrl+C` in the terminal).

## Notes

- Make sure that the serial port (`COM3` in this example) is available and not being used by another application (e.g., Arduino IDE).
- Adjust the `port` and `baud_rate` in the `serialConnection` instantiation to match your device configuration.

## Dependencies

This project uses the following Python libraries:

- [FastAPI](https://fastapi.tiangolo.com/) - A modern, fast web framework for building APIs with Python.
- [Uvicorn](https://www.uvicorn.org/) - A lightning-fast ASGI server for Python.
- [PySerial](https://pythonhosted.org/pyserial/) - A library to interact with the serial ports in Python.

To install the dependencies:

```bash
pip install fastapi uvicorn pyserial
```

Or install them from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License.

---
