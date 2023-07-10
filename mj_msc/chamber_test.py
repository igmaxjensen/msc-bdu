#!/usr/bin/python3

import csv
from tc10259 import TC10259
import time

def main():
    device = TC10259(0x60)
    running = True
    file_path = 'chamber_test_data.csv'
    with open(file_path,'w',newline='') as csv_file:
        fieldnames = ['alarm1','alarm2','temp','fan1speed','fan2speed','fan3speed','fan4speed','fanpwm']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        while running:
            fan_speeds = device.fan_speeds()
            data = {
                'alarm1' : device.alarm1(),
                'alarm2' : device.alarm2(),
                'temp' : device.temp(),
                'fan1speed' : fan_speeds[0],
                'fan2speed' : fan_speeds[1],
                'fan3speed' : fan_speeds[2],
                'fan4speed' : fan_speeds[3],
                'fanpwm' : device.fan_pwm()
            }
            writer.writerow(data)
            fan_speeds = device.fan_speeds()
            
            print("Live Data:")
            print("alarm1: " + device.alarm1())
            print("alarm2: " + device.alarm2())
            print("fan 1 speed: " + fan_speeds[0])
            print("fan 2 speed: " + fan_speeds[1])
            print("fan 3 speed: " + fan_speeds[2])
            print("fan 4 speed: " + fan_speeds[3])
            print("fan pwm: " + device.fan_pwm())
            print("temperature: " + device.temp())
            print("                 ")
            print(device.dev.get('ALARM1'))
            time.sleep(3)
    

if __name__ == '__main__':
    main()