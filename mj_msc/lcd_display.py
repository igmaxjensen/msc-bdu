
import threading
from led import LED
from tc10259 import TC10259
from port import Port
from menu import Menu1
import time

class LCD:

    def __init__(self):
        # initializes LCD
        # later add config to take out the hardcoded 
        # port_name and other parameters
        self.display = Port.port
        self.thread = None
        self.running = False
        self.home_menu = Menu1()
        self._dim_level = 200
        self._x_cursor_pos = 1
        self._y_cursor_pos = 1
        self._menu = self.home_menu
        self._contrast = 128
        self._backlight = "On"
        self.status = True
        self.alarm = True
        self.fault = True
        self.led = LED()
        self.fan_ctrl = TC10259(0x60)
    
    def start(self):
        # starts a thread
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._update_thread)
            self.display.open()
            self.thread.start()
            self.contrast = 128
            # self.backlight = "On"
            self.clear()
            self.dim = 200
            self.led.start_state(self.display)
            self.menu.display_menu(self)
            
    def stop(self):
         # stops a thread
        if self.running:
            self.running = False
            self.display.close()
            self.thread.join()
            
    def _update_thread(self):
        # opens while loop to recieve keys
        while self.running:
            try:
                alarm1 = list(bin(int(self.fan_ctrl.alarm1()))[2:].zfill(8))
                if alarm1[7] == 1 or alarm1[6] == 1:
                    self.status = False
                    self.fault = False
                elif alarm1[5] == 1 or alarm1[4] == 1 or alarm1[3] == 1 or alarm1[2] == 1 or alarm1[1] == 1:
                    self.status = False
                    self.alarm = False
                command = self.display.read(1)
                if command is not None and len(command) != 0:
                    if command == b'G':
                        self.clear()
                        self.menu = self.home_menu
                        self.home_menu.display_menu(self)
                        self.display.write(b'\xfe\x53')
                    else:
                        self.menu.processkey(command, self)
                if self.status:
                    # make status led green                    
                    self.led.one_green(self.display)
                    self.led.two_off(self.display)
                    self.led.three_off(self.display)
                else:
                    # make led red
                    self.led.one_red(self.display)
                    if not self.alarm:
                        # make alarm led red
                        self.led.two_red(self.display)
                    if not self.fault:
                        # make fault led red
                        self.led.three_red(self.display)
            except Exception as e:
                print(str(e))
                
    def text(self, message):
        # displays given text to the display
        length = len(message)
        if self.x_cursor_pos + length > 20:
            self.y_cursor_pos += 1
            self.x_cursor_pos = 1
        self.display.write(message.encode())
        self.x_cursor_pos += length
        
    def clear(self):
        # clears the display
        self.display.write(b'\xfe\x58')
        self.x_cursor_pos = 1
        self.y_cursor_pos = 1
        
    def open_port(self):
        if not self.display.is_open:
            self.display.open()
            
    def close_port(self):
        if self.display.is_open:
            self.display.close()
            
    def home_menu(self):
        self.menu = self.home_menu
    
    def home_line(self):
        self.x_cursor_pos = 1
        self.y_cursor_pos = 1
        
    def new_line(self):
        self.y_cursor_pos += 1
        self.x_cursor_pos = 1
        
    def backlight_on(self):
        time = bytes([0x0])
        command = b'\xfe\x42'
        self.display.write(command + time)
        
    def backlight_off(self):
        self.display.write(b'\xfe\x46')
    
    @property
    def menu(self):
        return self._menu
    
    @menu.setter
    def menu(self,new_menu):
        new_menu.display_menu(self)
        self._menu = new_menu
    
    @property
    def x_cursor_pos(self):
        return self._x_cursor_pos
    
    @property
    def y_cursor_pos(self):
        return self._y_cursor_pos
    
    @x_cursor_pos.setter
    def x_cursor_pos(self, new_x):
        if new_x > 20:
            new_x = 20
        if new_x < 1:
            new_x = 1
        cursor_command = bytes([0xfe, 0x47, new_x, self.y_cursor_pos])
        self.display.write(cursor_command)
        self._x_cursor_pos = new_x
        
    @y_cursor_pos.setter
    def y_cursor_pos(self, new_y):
        if new_y > 4:
            new_y = 4
        if new_y < 1:
            new_y = 1
        cursor_command = bytes([0xfe, 0x47, self.x_cursor_pos, new_y])
        self.display.write(cursor_command)
        self._y_cursor_pos = new_y
        
    @property
    def dim(self):
        return self._dim_level
        
    @dim.setter
    def dim(self, level):
        if level > 255:
            level = 255
        if level < 0:
            level = 0
        dim_command = bytes([0xfe, 0x99, level])
        self.display.write(dim_command)
        self._dim_level = level
        
    @property 
    def contrast(self):
        return self._contrast
    
    @contrast.setter
    def contrast(self, level):
        if level > 255:
            level = 255
        if level < 0:
            level = 0
        contrast_command = bytes([0xfe, 0x91, level])
        self.display.write(contrast_command)
        self._contrast = level

    @property
    def backlight(self):
        return self._backlight
    
    @contrast.setter
    def backlight(self,status):
        if self._backlight == "On":
            # turn off backlight
            self.display.write(b'\xfe\x46')
            self._backlight = status
        else:
            # turn on backlight
            command = bytes([0xfe,0x42,0x0])
            self.display.write(command)
            self._backlight = status