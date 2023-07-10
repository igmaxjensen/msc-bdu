import serial
import time
import port as usb
from led import LED

port = usb.Port.port

port.write(b'\xfe\x43') # turns on autowrap text
change_baud_rate = b'\xfe\x39'
change_ic_address = b'\xfe\x33'
set_brightness = b'\xfe\x98'
set_contrast = b'\xfe\x91'
set__key_backlight = b'\xfe\x9c'

baud_rate = bytes(0x33)
ic_address = bytes(0x50)
brightness = bytes(0xc8)
contrast = bytes(0x80)
key_backlight = bytes(0xff)

change_baud_rate = change_baud_rate + baud_rate
change_ic_address = change_ic_address + ic_address
set_brightness = set_brightness + brightness
set_contrast = set_contrast + contrast
set__key_backlight = set__key_backlight + key_backlight


time.sleep(3)
port.write(change_baud_rate)
port.write(change_ic_address)
port.write(set_brightness)
port.write(set_contrast)
port.write(set__key_backlight)

# set led to start state
led = LED()
led.set_gpo_start(port)


time.sleep(3)
port.close()
