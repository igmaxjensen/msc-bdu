#!/usr/bin/python3

from lcd_display import LCD
import time

lcd = LCD()
lcd.display.close()
lcd.start()
time.sleep(30)
lcd.stop()