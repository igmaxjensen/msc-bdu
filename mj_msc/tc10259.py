from i2cdevice import Device, Register, BitField
import re

# This class represents the fan control device 
# The device has properties of each fan and its failures and alarms
class TC10259:
    def __init__(self, i2c_addr, i2c_dev = None):
        self._i2c_addr = i2c_addr
        self.dev = Device(self._i2c_addr, i2c_dev = None, bit_width=8,
                          registers=(
            Register('ALARM1', 0x00, fields=(
                BitField('fan_failure', 0xFF),
            ),),
            Register('ALARM2', 0x01, fields=(
                BitField('fan_failure', 0xFF),
            ),),
            Register('SETPOINT', 0x02, fields=(
                BitField('set_speed', 0xFF),
            ),),
            Register('FANSPEED1', 0x03, fields=(
                BitField('fan_speed', 0xFF),
            ),),
            Register('FANSPEED2', 0x04, fields=(
                BitField('fan_speed', 0xFF),
            ),),
            Register('FANSPEED3', 0x05, fields=(
                BitField('fan_speed', 0xFF),
            ),),
            Register('FANSPEED4', 0x06, fields=(
                BitField('fan_speed', 0xFF),
            ),),
            Register('FANPWM', 0x07, fields=(
                BitField('fan_power', 0xFF),
            ),),
            Register('INTERNALTHERM', 0x0a, fields=(
                BitField('internal_temp', 0xFF),
            ),),
            Register('MINTEMP', 0x0e, fields=(
                BitField('min_temp', 0xFF),
            ),),
            Register('MIDTEMP', 0x0f, fields=(
                BitField('mid_temp', 0xFF),
            ),),
            Register('MAXTEMP', 0x10, fields=(
                BitField('max_temp', 0xFF),
            ),),
            Register('MINSPEED', 0x13, fields=(
                BitField('min_speed', 0xFF),
            ),),
            Register('MIDSPEED', 0x14, fields=(
                BitField('mid_speed', 0xFF),
            ),),
            Register('MAXSPEED', 0x15, fields=(
                BitField('max_speed', 0xFF),
            ),),
            Register('FAULTSPEED', 0x16, fields=(
                BitField('fault_speed', 0xFF),
            ),),
            Register('FANFAILLIMIT', 0x17, fields=(
                BitField('fan_fail_limit', 0xFF),
            ),),
            Register('FANQTY', 0x1D, fields=(
                BitField('fan_quantity', 0xFF),
            ),),
        ))

        self._alarm1 = self.extract_data(str(self.dev.get('ALARM1')))
        self._alarm2 = self.extract_data(str(self.dev.get('ALARM2')))
        self._setpoint = self.extract_data(str(self.dev.get('SETPOINT')))
        self._fan_speeds = [self.extract_data(str(self.dev.get('FANSPEED1'))),self.extract_data(str(self.dev.get('FANSPEED2'))),self.extract_data(str(self.dev.get('FANSPEED3'))),self.extract_data(str(self.dev.get('FANSPEED4')))]
        self._fan_pwm = self.extract_data(str(self.dev.get('FANPWM')))
        self._temp = self.extract_data(str(self.dev.get('INTERNALTHERM')))
        self._temp_levels = [self.extract_data(str(self.dev.get('MINTEMP'))),self.extract_data(str(self.dev.get('MIDTEMP'))),self.extract_data(str(self.dev.get('MAXTEMP')))]
        self._speed_levels = [self.extract_data(str(self.dev.get('MINSPEED'))),self.extract_data(str(self.dev.get('MIDSPEED'))),self.extract_data(str(self.dev.get('MAXSPEED')))]
        self._fault_speed = self.extract_data(str(self.dev.get('FAULTSPEED')))
        self._fan_qty = self.extract_data(str(self.dev.get('FANQTY')))

    def alarm1(self):
        string = str(self.dev.get('ALARM1'))
        number = self.extract_data(string)
        self._alarm1  = number
        return self._alarm1

    def alarm2(self):
        string = str(self.dev.get('ALARM2'))
        number = self.extract_data(string)
        self._alarm2 = number
        return self._alarm2

    def setpoint(self):
        string = str(self.dev.get('SETPOINT'))
        number = self.extract_data(string)
        self._setpoint = number
        return self._setpoint

    def fan_speeds(self):
        data =[self.dev.get('FANSPEED1'),self.dev.get('FANSPEED2'),self.dev.get('FANSPEED3'),self.dev.get('FANSPEED4')]
        new_data = []
        for i in range(0,4):
            string = str(data[i])
            number = self.extract_data(string)
            new_data.append(number)
        self._fan_speeds = new_data
        return self._fan_speeds

    def fan_pwm(self):
        string = str(self.dev.get('FANPWM'))
        number = self.extract_data(string)
        self._fan_pwm = number
        return self._fan_pwm

    def temp(self):
        string = str(self.dev.get('INTERNALTHERM'))
        number = self.extract_data(string)
        self._temp = number
        return self._temp

    def temp_levels(self):
        data =[self.dev.get('MINTEMP'),self.dev.get('MIDTEMP'),self.dev.get('MAXTEMP')]
        new_data = []
        for i in range(0,3):
            string = str(data[i])
            number = self.extract_data(string)
            new_data.append(number)
        self._temp_levels = new_data
        return self._temp_levels

    def speed_levels(self):
        data = [self.dev.get('MINSPEED'),self.dev.get('MIDSPEED'),self.dev.get('MAXSPEED')]
        new_data = []
        for i in range(0,3):
            string = str(data[i])
            number = self.extract_data(string)
            new_data.append(number)
        self._speed_levels = new_data
        return self._speed_levels

    def fault_speed(self):
        string = str(self.dev.get('FAULTSPEED'))
        number = self.extract_data(string)
        self._fault_speed = number
        return self._fault_speed

    def fan_qty(self):
        string = str(self.dev.get('FANQTY'))
        number = self.extract_data(string)
        self._fan_qty = number
        return self._fan_qty

    def extract_data(self,string):
        data = re.search(r'\((.*?)\)',string).group(1)
        number = re.search(r'\d+',data).group()
        return number
    
    def handle_alarms(self, alarm):
        pass
