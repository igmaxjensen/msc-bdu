#!/usr/bin/python3

from tc10259 import TC10259
import time

def main():
    device = TC10259(0x60)
    print(device.alarm1())
    print(device.alarm2())
    print(device.setpoint())
    print(device.fan_speeds())
    print(device.fan_pwm())
    print(device.temp())
    print(device.temp_levels())
    print(device.speed_levels())
    print(device.fault_speed())
    print(device.fan_qty())

if __name__ == '__main__':
    main()