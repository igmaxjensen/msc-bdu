
import serial

class Port:
    
    port_name = "/dev/ttyUSB0"  # Replace with the correct serial port name
    baud_rate = 19200
    timeout = 0.1

    port = serial.Serial(port_name, baud_rate, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE, timeout, rtscts = False)
    