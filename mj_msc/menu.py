
import port
from tc10259 import TC10259
    
class Menu1:
    
    def __init__(self):
       pass
   
    def display_menu(self, lcd):
       lcd.clear() 
       lcd.display.write(b'\xfe\x53')
       lcd.text("   -Device Name-   ")
       lcd.text("+ System Status   ")
       lcd.text("+ Edit            ")
       lcd.text("+ System Info     ")
       lcd.x_cursor_pos = 1
       lcd.y_cursor_pos = 2
    
        
    def processkey(self, command, lcd):
        # processes a key to a command to alter the display
        if command == b'B':
            row = lcd.y_cursor_pos 
            if row <= 2:
                pass
            else:
                lcd.y_cursor_pos -= 1
        elif command == b'H':
            lcd.y_cursor_pos += 1
        elif command == b'E':
            row = lcd.y_cursor_pos
            if row == 2:
                lcd.menu = SystemStatusMenu()
                lcd.menu.display_menu(lcd)
            elif row == 3:
                lcd.menu = EditMenu()
                lcd.menu.display_menu(lcd)

            elif row == 4:
                lcd.menu = SystemInfoMenu()
                lcd.menu.display_menu(lcd)
            else:
                pass
        else:
            pass

class SystemStatusMenu:
    def __init__(self):
        pass
    
    def display_menu(self, lcd):
        lcd.clear()
        lcd.display.write(b'\xfe\x53')
        lcd.text("  -System Status-  ")
        lcd.new_line()
        # Input way to get the mode
        mode = "LAISR"
        lcd.text("Mode: " + mode)
        lcd.new_line()
        lcd.text("+ Alarms")
        lcd.new_line()
        lcd.text("+ LAISR")
        lcd.x_cursor_pos = 1
        lcd.y_cursor_pos = 3
       
    def processkey(self, command, lcd):
        # processes a key to a command to alter the display
        if command == b'A':
            lcd.menu = Menu1()
            lcd.menu.display_menu(lcd)
        elif command == b'B':
            row = lcd.y_cursor_pos 
            if row <= 3:
                pass
            else:
                lcd.y_cursor_pos -= 1
        elif command == b'H':
            lcd.y_cursor_pos += 1
        elif command == b'E':
            row = lcd.y_cursor_pos
            if row == 3:
                lcd.menu = AlarmsMenu()
                lcd.menu.display_menu(lcd)
            elif row == 4:
                lcd.menu = LaisrMenu()
                lcd.menu.display_menu(lcd)
            else:
                pass
        else:
            pass
        
class AlarmsMenu:
    def __init__(self):
       pass
    
    def display_menu(self, lcd):
        lcd.clear()
        lcd.display.write(b'\xfe\x53')
        lcd.text("      -Alarms-     ")
        lcd.new_line()
        lcd.text("+ Active Alarms")
        lcd.new_line()
        lcd.text("+ Alarm History")
        lcd.x_cursor_pos = 1
        lcd.y_cursor_pos = 2
       
       
    def processkey(self, command, lcd):
        # processes a key to a command to alter the display
        if command == b'A':
            lcd.menu = SystemStatusMenu()
            lcd.menu.display_menu(lcd)
        elif command == b'B':
            row = lcd.y_cursor_pos 
            if row <= 2:
                pass
            else:
                lcd.y_cursor_pos -= 1
        elif command == b'H':
            row = lcd.y_cursor_pos
            if row >= 3:
                pass
            else:
                lcd.y_cursor_pos += 1
        elif command == b'E':
            row = lcd.y_cursor_pos
            if row == 2:
                lcd.menu = ActiveAlarmsData()
                lcd.menu.display_menu(lcd)
            elif row == 3:
                lcd.menu = AlarmHistoryData()
                lcd.menu.display_menu(lcd)
            else:
                pass
        else:
            pass
        
class ActiveAlarmsData:
    def __init__(self):
        self.device = TC10259(0x60)
        self.alarm1 = self.device.alarm1()
        self.alarm2 = self.device.alarm2()
        self.page = 1
        
    def display_menu(self, lcd):
       self.show_alarms(lcd)
       lcd.x_cursor_pos = 16
       lcd.y_cursor_pos = 1
       
    def show_alarms(self,lcd):
        self.alarms = self.handle_alarms()
        if self.page == 1:
            self.header(lcd)
            lcd.text(self.alarms[0])
            lcd.new_line()
            lcd.text(self.alarms[1])
            lcd.new_line()
            lcd.text(self.alarm[2])
            pass
        elif self.page == 2:
            self.header(lcd)
            lcd.text(self.alarms[3])
            lcd.new_line()
            lcd.text(self.alarms[4])
            lcd.new_line()
            lcd.text(self.alarm[5])
        elif self.page == 3:
            self.header(lcd)
            lcd.text(self.alarms[6])
            lcd.new_line()
            lcd.text(self.alarms[7])
            lcd.new_line()
            lcd.text(self.alarm[8])
        
    def header(self,lcd):
        lcd.clear()
        lcd.text("Active Alarms: <")
        lcd.text(self.page)
        lcd.text(">")
        lcd.new_line()

    def handle_alarms(self):
        bin_alarm1 = list(bin(self.alarm1)[2:].zfill(8))
        alarms = []
        if bin_alarm1[7] == 1:
            alarms2 = self.handle_alarm2
            for alarm in alarms2:
                alarms.append(alarm)
        if bin_alarm1[6] == 1:
            alarms2 = self.handle_alarm2
            for alarm in alarms2:
                alarms.append(alarm)
        if bin_alarm1[5] == 1:
            alarms.append("Overtemp Failure")
        if bin_alarm1[2] == 1:
            alarms.append("Thermistor Failure")
        if bin_alarm1[1] == 1:
            alarms.append("Filter Blockage")
        return alarms

    def handle_alarm2(self):
        bin_alarm2 = list(bin(self.alarm2)[2:].zfill(8))
        alarms = []
        if bin_alarm2[7] == 1:
            alarms.append("Fan 1 Failure")
        if bin_alarm2[6] == 1:
            alarms.append("Fan 2 Failure")
        if bin_alarm2[5] == 1:
            alarms.append("Fan 3 Failure")
        if bin_alarm2[4] == 1:
            alarms.append("Fan 4 Failure")
        if bin_alarm2[3] == 1:
            alarms.append("Predict Fan 1 Fail")
        if bin_alarm2[2] == 1:
            alarms.append("Predict Fan 2 Fail")
        if bin_alarm2[1] == 1:
            alarms.append("Predict Fan 3 Fail")
        if bin_alarm2[0] == 1:
            alarms.append("Predict Fan 4 Fail")
        return alarms
        
    def processkey(self, command, lcd):
        # processes a key to a command to alter the display
        if command == b'A':
            lcd.menu = AlarmsMenu()
            lcd.menu.display_menu(lcd)
        elif command == b'C':
            lcd.x_cursor_pos = 18
        elif command == b'D':
            lcd.x_cursor_pos = 16
        elif command == b'B':
            pass
        elif command == b'H':
            pass
        elif command == b'E':
            col = lcd.x_cursor_pos
            if col == 16:
                if  self.page >=2:
                    self.page = self.page - 1
                    self.display.menu(lcd)
                    
            if col == 18:
                if self.page <= 2:
                    self.page = self.page + 1
                    self.display.menu(lcd)
        else:
            pass
        
class AlarmHistoryData:
    def __init__(self):
       pass
   
    def display_menu(self, lcd):
       lcd.clear()
       lcd.display.write(b'\xfe\x54')
       lcd.text("Alarm History:")
       lcd.new_line()
       lcd.text("OLD ALARM")
        
    def processkey(self, command, lcd):
        # processes a key to a command to alter the display
        if command == b'A':
            lcd.menu = AlarmsMenu()
            lcd.menu.display_menu(lcd)
        elif command == b'C':
            # lcd.x_cursor_pos += 1
            pass
        elif command == b'B':
            lcd.y_cursor_pos -= 1
            # coords = (lcd.x_cursor_pos, lcd.y_cursor_pos)
            # print(coords)
        elif command == b'H':
            lcd.y_cursor_pos += 1
            # coords = (lcd.x_cursor_pos, lcd.y_cursor_pos)
            # print(coords)
        elif command == b'E':
            pass
        else:
            pass
        
class LaisrMenu:
    def __init__(self):
       pass
   
    def display_menu(self, lcd):
       lcd.clear() 
       lcd.display.write(b'\xfe\x53')
       lcd.text("    -LAISR Menu-   ")
       lcd.new_line()
       lcd.text("+ Connection Info")
       lcd.new_line()
       lcd.text("+ Bit Rates")
       lcd.new_line()
       lcd.text("+ RX Es/No")
       lcd.x_cursor_pos = 1
       lcd.y_cursor_pos = 2
      
    
        
    def processkey(self, command, lcd):
        # processes a key to a command to alter the display
        if command == b'A':
            lcd.menu = SystemStatusMenu()
            lcd.menu.display_menu(lcd)
        elif command == b'C':
            # lcd.x_cursor_pos += 1
            pass
        elif command == b'B':
            row = lcd.y_cursor_pos 
            if row <= 2:
                pass
            else:
                lcd.y_cursor_pos -= 1
        elif command == b'H':
            lcd.y_cursor_pos += 1
            # coords = (lcd.x_cursor_pos, lcd.y_cursor_pos)
            # print(coords)
        elif command == b'E':
            row = lcd.y_cursor_pos
            if row == 2:
                lcd.menu = ConnectionInfoData()
                lcd.menu.display_menu(lcd)
            elif row == 3:
                lcd.menu = BitRatesData()
                lcd.menu.display_menu(lcd)

            elif row == 4:
                lcd.menu = RxEsNoData()
                lcd.menu.display_menu(lcd)
            else:
                pass
        else:
            pass
        
class ConnectionInfoData:
    def __init__(self):
       pass
   
    def display_menu(self, lcd):
       lcd.clear()
       lcd.display.write(b'\xfe\x54')
       lcd.text("Connection Info:")
       lcd.new_line()
       satelitte = "alphasat"
       lcd.text("Satellite: " + satelitte)
       lcd.new_line()
       beam = "Beam 1"
       lcd.text("Beam: " + beam)
      
    
        
    def processkey(self, command, lcd):
        # processes a key to a command to alter the display
        if command == b'A':
            lcd.menu = LaisrMenu()
            lcd.menu.display_menu(lcd)
        elif command == b'C':
            # lcd.x_cursor_pos += 1
            pass
        elif command == b'B':
            lcd.y_cursor_pos -= 1
            # coords = (lcd.x_cursor_pos, lcd.y_cursor_pos)
            # print(coords)
        elif command == b'H':
            lcd.y_cursor_pos += 1
            # coords = (lcd.x_cursor_pos, lcd.y_cursor_pos)
            # print(coords)
        elif command == b'E':
            pass
        else:
            pass
        
        
class BitRatesData:
    def __init__(self):
       pass
       
    def display_menu(self, lcd):
       lcd.clear() 
       lcd.display.write(b'\xfe\x54')
       lcd.text("Bit Rates:")
       lcd.new_line()
       tx_bit_rate = 100
       lcd.text("TX Bit Rate: " + str(tx_bit_rate))
       lcd.new_line()
       rx_bit_rate = 200
       lcd.text("RX Bit Rate: " + str(rx_bit_rate))
      
    
        
    def processkey(self, command, lcd):
        # processes a key to a command to alter the display
        if command == b'A':
            lcd.menu = LaisrMenu()
            lcd.menu.display_menu(lcd)
        elif command == b'C':
            # lcd.x_cursor_pos += 1
            pass
        elif command == b'B':
            lcd.y_cursor_pos -= 1
            # coords = (lcd.x_cursor_pos, lcd.y_cursor_pos)
            # print(coords)
        elif command == b'H':
            lcd.y_cursor_pos += 1
            # coords = (lcd.x_cursor_pos, lcd.y_cursor_pos)
            # print(coords)
        elif command == b'E':
            pass
        else:
            pass
        

class RxEsNoData:
    def __init__(self):
       pass
   
    def display_menu(self, lcd):
       lcd.clear()
       lcd.display.write(b'\xfe\x54')
       lcd.text("RX Es/No:")
       lcd.new_line()
       rx_es_no = 350
       lcd.text(str(rx_es_no))
      
    
        
    def processkey(self, command, lcd):
        # processes a key to a command to alter the display
        if command == b'A':
            lcd.menu = LaisrMenu()
            lcd.menu.display_menu(lcd)
        elif command == b'C':
            # lcd.x_cursor_pos += 1
            pass
        elif command == b'B':
            lcd.y_cursor_pos -= 1
            # coords = (lcd.x_cursor_pos, lcd.y_cursor_pos)
            # print(coords)
        elif command == b'H':
            lcd.y_cursor_pos += 1
            # coords = (lcd.x_cursor_pos, lcd.y_cursor_pos)
            # print(coords)
        elif command == b'E':
            pass
        else:
            pass
        
        

        
class EditMenu:
    def __init__(self):
        pass
    
    def display_menu(self, lcd):
        lcd.clear()
        lcd.display.write(b'\xfe\x53')
        lcd.text("    -Edit Menu-    ")
        lcd.new_line()
        lcd.text("+ System Mode")
        lcd.new_line()
        lcd.text("+ Reboot")
        lcd.new_line()
        lcd.text("+ Screen Settings")
        lcd.x_cursor_pos = 1
        lcd.y_cursor_pos = 2
       
    def processkey(self, command, lcd):
        # processes a key to a command to alter the display
        if command == b'A':
            lcd.menu = Menu1()
            lcd.menu.display_menu(lcd)
        elif command == b'C':
            # lcd.x_cursor_pos += 1
            pass
        elif command == b'B':
            row = lcd.y_cursor_pos 
            if row <= 2:
                pass
            else:
                lcd.y_cursor_pos -= 1
        elif command == b'H':
            lcd.y_cursor_pos += 1
            # coords = (lcd.x_cursor_pos, lcd.y_cursor_pos)
            # print(coords)
        elif command == b'E':
            row = lcd.y_cursor_pos
            if row == 2:
                lcd.menu = ChangeSystemModeMenu()
                lcd.menu.display_menu(lcd)
            elif row == 3:
                lcd.menu = RebootMenu()
                lcd.menu.display_menu(lcd)
            elif row == 4:
                lcd.menu = ScreenSettingsMenu()
                lcd.menu.display_menu(lcd)
            else:
                pass
        else:
            pass   
        
class ChangeSystemModeMenu:
    def __init__(self):
       pass
   
    def display_menu(self, lcd):
       lcd.clear() 
       lcd.display.write(b'\xfe\x53')
       lcd.text("System Mode:")
       lcd.new_line()
       # ask how we can get the current mode
       # later mode will be an lcd attribute so that 
       # both display_meny and processkey can call it
       sys_mode = "LAISR"
       lcd.text("Mode: " + sys_mode)
       lcd.text("~ Change Mode")     
       lcd.x_cursor_pos = 1
       lcd.y_cursor_pos = 3
    
        
    def processkey(self, command, lcd):
        # processes a key to a command to alter the display
        if command == b'A':
            lcd.menu = EditMenu()
            lcd.menu.display_menu(lcd)
        elif command == b'C':
            # lcd.x_cursor_pos += 1
            pass
        elif command == b'B':
            lcd.y_cursor_pos -= 1
            # coords = (lcd.x_cursor_pos, lcd.y_cursor_pos)
            # print(coords)
        elif command == b'H':
            lcd.y_cursor_pos += 1
            # coords = (lcd.x_cursor_pos, lcd.y_cursor_pos)
            # print(coords)
        elif command == b'E':
            row = lcd.y_cursor_pos
            if row == 3:
                # Switch Mode
                # later will have to set the current mode and off mode
                print("Switch Mode")
            else:
                pass
        else:
            pass
        
class RebootMenu:
    def __init__(self):
       self.prev_menu = EditMenu()
   
    def display_menu(self, lcd):
       lcd.clear() 
       lcd.display.write(b'\xfe\x53')
       lcd.text("Reboot Menu:")
       lcd.new_line()
       lcd.text("~ Reboot ADU")
       lcd.new_line()
       lcd.text("~ Reboot BDU")
       lcd.new_line()
       lcd.text("~ Reboot All")
       lcd.x_cursor_pos = 1
       lcd.y_cursor_pos = 2
      
    
        
    def processkey(self, command, lcd):
        # processes a key to a command to alter the display
        if command == b'A':
            lcd.menu = EditMenu()
            lcd.menu.display_menu(lcd)
        elif command == b'C':
            # lcd.x_cursor_pos += 1
            pass
        elif command == b'B':
            lcd.y_cursor_pos -= 1
            # coords = (lcd.x_cursor_pos, lcd.y_cursor_pos)
            # print(coords)
        elif command == b'H':
            lcd.y_cursor_pos += 1
            # coords = (lcd.x_cursor_pos, lcd.y_cursor_pos)
            # print(coords)
        elif command == b'E':
            row = lcd.y_cursor_pos
            if row == 2:
                # reboot ADU
                print("Reboot ADU")
            elif row == 3:
                # reboot BDU
                print("Reboot BDU")
            elif row == 4:
                # reboot both
                print("Reboot Both")
        else:
            pass
        
class ScreenSettingsMenu:
    def __init__(self):
       self.x_cursor_pos = 1
       self.y_cursor_pos = 2
   
    def display_menu(self, lcd):
       lcd.clear() 
       lcd.display.write(b'\xfe\x53')
       lcd.text("LCD Control:")
       lcd.new_line()
       # later make backlight a lcd attribute
       on_status = lcd._backlight
       lcd.text("<> Brightness: " + str(lcd.dim))
       lcd.new_line()
       lcd.text("<> Contrast: " + str(lcd.contrast)) # make contrast an lcd attribute
       lcd.new_line()
       lcd.text(" ~ Backlight: " + str(on_status))
       lcd.x_cursor_pos = self.x_cursor_pos
       lcd.y_cursor_pos = self.y_cursor_pos
      
    
        
    def processkey(self, command, lcd):
        # processes a key to a command to alter the display
        if command == b'A':
            lcd.menu = EditMenu()
            lcd.menu.display_menu(lcd)
        elif command == b'C':
            col = lcd.x_cursor_pos
            if col >= 2:
                pass
            else:
                lcd.x_cursor_pos += 1
        elif command == b'D':
            lcd.x_cursor_pos -= 1
        elif command == b'B':
            lcd.y_cursor_pos -= 1
        elif command == b'H':
            lcd.y_cursor_pos += 1
        elif command == b'E':
            col = lcd.x_cursor_pos
            row = lcd.y_cursor_pos
            if row == 2 and col == 1:
                lcd.dim -= 5
                self.x_cursor_pos = 1
                self.y_cursor_pos = 2
                self.display_menu(lcd)
            elif row == 2 and col == 2:
                lcd.dim += 5
                self.x_cursor_pos = 2
                self.y_cursor_pos = 2
                self.display_menu(lcd)
            elif row == 3 and col == 1:
                # Turn down contrast
                lcd.contrast -= 5
                self.x_cursor_pos = 1
                self.y_cursor_pos = 3
                self.display_menu(lcd)
            elif row == 3 and col == 2:
                # Turn up constrast
                lcd.contrast += 5
                self.x_cursor_pos = 2
                self.y_cursor_pos = 3
                self.display_menu(lcd)
            elif row == 4 and col == 2:
                # Change Backlight
                if lcd._backlight == "Off":
                    lcd.backlight = "On"
                elif lcd._backlight == "On":
                    lcd.backlight = "Off"
                self.x_cursor_pos = 2
                self.y_cursor_pos = 4
                self.display_menu(lcd)
                
            else:
                pass
        else:
            pass    
        
class SystemInfoMenu:
    def __init__(self):
        pass
    
    def display_menu(self, lcd):
        # Later make this recieve info
        lcd.clear()
        lcd.display.write(b'\xfe\x53')
        lcd.text("   -System Info-   ")
        lcd.new_line()
        lcd.text("+ Firmware Version")
        lcd.new_line()
        lcd.text("+ BDU Info")
        lcd.new_line()
        lcd.text("+ Other Info")
        lcd.x_cursor_pos = 1
        lcd.y_cursor_pos = 2
        
    def processkey(self, command, lcd):
        # processes a key to a command to alter the display
        if command == b'D':
            lcd.menu = Menu1()
            lcd.menu.display_menu(lcd)
        elif command == b'C':
            # lcd.x_cursor_pos += 1
            pass
        elif command == b'B':
            row = lcd.y_cursor_pos 
            if row <= 2:
                pass
            else:
                lcd.y_cursor_pos -= 1
        elif command == b'H':
            row = lcd.y_cursor_pos 
            if row >= 3:
                pass
            else:
                lcd.y_cursor_pos += 1
        elif command == b'E':
            row = lcd.y_cursor_pos
            if row == 2:
                lcd.menu = FirmwareVersionData()
                lcd.menu.display_menu(lcd)
            elif row == 3:
                lcd.menu = OtherInfoData()
                lcd.menu.display_menu(lcd)
            else:
                pass
        else:
            pass
        
class FirmwareVersionData:
    
    def __init__(self):
       pass
   
    def display_menu(self, lcd):
       lcd.clear() 
       lcd.display.write(b'\xfe\x54')
       lcd.text("Firmware Version:")
       lcd.new_line()
       bdu_version = 1
       lcd.text("BDU: " + str(bdu_version))
       lcd.new_line()
       adu_version = 2
       lcd.text("ADU: " + str(adu_version))
       
        
    def processkey(self, command, lcd):
        # processes a key to a command to alter the display
        if command == b'A':
            lcd.menu = SystemInfoMenu()
            lcd.menu.display_menu(lcd)
        elif command == b'C':
            lcd.x_cursor_pos += 1
            # coords = (lcd.x_cursor_pos, lcd.y_cursor_pos)
            # print(coords)
        elif command == b'B':
            lcd.y_cursor_pos -= 1
            # coords = (lcd.x_cursor_pos, lcd.y_cursor_pos)
            # print(coords)
        elif command == b'H':
            lcd.y_cursor_pos += 1
            # coords = (lcd.x_cursor_pos, lcd.y_cursor_pos)
            # print(coords)
        elif command == b'E':
            pass
        else:
            pass
        
class BDUInfoData:
     def __init__(self):
       self.device = TC10259(0x60)
   
     def display_menu(self, lcd):
       lcd.clear() 
       lcd.text("BDU Info:")
       lcd.new_line()
       fan_speeds = self.device.fan_speeds()
       lcd.text("Fan Speeds: 1,2,3,4")
       lcd.new_line()
       lcd.text(fan_speeds[0])
       lcd.text(", ")
       lcd.text(fan_speeds[1])
       lcd.text(", ")
       lcd.text(fan_speeds[2])
       lcd.text(", ")
       lcd.text(fan_speeds[3])
       temp = self.device.temp()
       lcd.text("Internal Temp: ")
       lcd.text(temp)
       
       # display inner data
        
     def processkey(self, command, lcd):
        # processes a key to a command to alter the display
        if command == b'A':
            lcd.menu = SystemInfoMenu()
            lcd.menu.display_menu(lcd)
        elif command == b'C':
            lcd.x_cursor_pos += 1
            # coords = (lcd.x_cursor_pos, lcd.y_cursor_pos)
            # print(coords)
        elif command == b'B':
            lcd.y_cursor_pos -= 1
            # coords = (lcd.x_cursor_pos, lcd.y_cursor_pos)
            # print(coords)
        elif command == b'H':
            lcd.y_cursor_pos += 1
            # coords = (lcd.x_cursor_pos, lcd.y_cursor_pos)
            # print(coords)
        elif command == b'E':
            pass
        else:
            pass

class OtherInfoData:
    def __init__(self):
       pass
   
    def display_menu(self, lcd):
       lcd.clear() 
       lcd.display.write(b'\xfe\x54')
       lcd.text("Other Info:")
       lcd.new_line()
       imsi = 38290
       lcd.text("IMSI: " + str(imsi))
       lcd.new_line()
       ip_num = 27176389
       lcd.text("IP: " + str(ip_num))
       lcd.new_line()
       adu_serial = 9273083
       lcd.text("ADU Serial: " + str(adu_serial))
      
    
        
    def processkey(self, command, lcd):
        # processes a key to a command to alter the display
        if command == b'A':
            lcd.menu = SystemInfoMenu()
            lcd.menu.display_menu(lcd)
        elif command == b'C':
            lcd.x_cursor_pos += 1
            # coords = (lcd.x_cursor_pos, lcd.y_cursor_pos)
            # print(coords)
        elif command == b'B':
            lcd.y_cursor_pos -= 1
            # coords = (lcd.x_cursor_pos, lcd.y_cursor_pos)
            # print(coords)
        elif command == b'H':
            lcd.y_cursor_pos += 1
            # coords = (lcd.x_cursor_pos, lcd.y_cursor_pos)
            # print(coords)
        elif command == b'E':
            pass
        else:
            pass
        
        

       

        
