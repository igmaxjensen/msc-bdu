
class LED:
    def __init__(self):
        self.gpo_on = b'\xfe\x57'
        self.gpo_off = b'\xfe\x56'
        self.set_gpo_start = b'\xfe\xc3'
        self.gpo_one = bytes([0x1])
        self.gpo_two = bytes([0x2])
        self.gpo_three = bytes([0x3])
        self.gpo_four = bytes([0x4])
        self.gpo_five = bytes([0x5])
        self.gpo_six = bytes([0x6])
        self.on = bytes([0x1])
        self.off = bytes([0x0])

    def one_green(self,lcd):
        red_off = self.gpo_off + self.gpo_one
        green_on = self.gpo_on + self.gpo_two
        lcd.write(red_off)
        lcd.write(green_on)
        
    def one_red(self,lcd):
        red_on = self.gpo_on + self.gpo_one
        green_off = self.gpo_off + self.gpo_two
        lcd.write(green_off)
        lcd.write(red_on)

    def one_off(self,lcd):
        red_off = self.gpo_off + self.gpo_one
        green_off = self.gpo_off + self.gpo_two
        lcd.write(red_off)
        lcd.write(green_off)        
        
    def two_green(self,lcd):
        red_off = self.gpo_off + self.gpo_three
        green_on = self.gpo_on + self.gpo_four
        lcd.write(red_off)
        lcd.write(green_on)
        
    def two_red(self,lcd):
        red_on = self.gpo_on + self.gpo_three
        green_off = self.gpo_off + self.gpo_four
        lcd.write(green_off)
        lcd.write(red_on)

    def two_off(self,lcd):
        red_off = self.gpo_off + self.gpo_three
        green_off = self.gpo_off + self.gpo_four
        lcd.write(red_off)
        lcd.write(green_off) 
        
    def three_green(self,lcd):
        red_off = self.gpo_off + self.gpo_five
        green_on = self.gpo_on + self.gpo_six
        lcd.write(red_off)
        lcd.write(green_on)
        
    def three_red(self,lcd):
        red_on = self.gpo_on + self.gpo_five
        green_off = self.gpo_off + self.gpo_six
        lcd.write(green_off)
        lcd.write(red_on)

    def three_off(self,lcd):
        red_off = self.gpo_off + self.gpo_five
        green_off = self.gpo_off + self.gpo_six
        lcd.write(red_off)
        lcd.write(green_off) 
        
    def start_state(self,lcd):
        lcd.write(self.set_gpo_start + self.gpo_one + self.off)
        lcd.write(self.set_gpo_start + self.gpo_two + self.on)
        lcd.write(self.set_gpo_start + self.gpo_three + self.off)
        lcd.write(self.set_gpo_start + self.gpo_four + self.off)
        lcd.write(self.set_gpo_start + self.gpo_five + self.off)
        lcd.write(self.set_gpo_start + self.gpo_six + self.off)

