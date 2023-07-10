import serial
import port as usb

# Port connection to the display
port = usb.Port.port

# Boot-up screen commands
save_start_chars = b'\xfe\xc2'
save_custom_chars = b'\xfe\xc1'
change_start_screen = b'\xfe\x40'
load_custom_chars = b'\xfe\xc0'

# Custom character memory banks
mem_bank_zero = bytes([0x0])
mem_bank_one = bytes([0x1])
mem_bank_two = bytes([0x2])
mem_bank_three = bytes([0x3])
mem_bank_four = bytes([0x4])

# Start screen character creation

# Inmarsat Gov Logo
logo_id = bytes([0x1])

logo_data = bytes([0x11,0xc, 0x6, 0x13, 0x9, 0xb, 0x1b, 0x12])

logo_save_custom_char = save_custom_chars + mem_bank_zero + logo_id + logo_data
logo_save_start_chars = save_start_chars + logo_id + logo_data

# Upper left of box
upper_left_id = bytes([0x3])

upper_left_data = bytes([0x0, 0x0, 0x0, 0x7, 0xf, 0xe, 0xc, 0xc])

upper_left_save_custom_char = save_custom_chars + mem_bank_zero + upper_left_id + upper_left_data
upper_left_save_start_chars = save_start_chars + upper_left_id + upper_left_data

# Upper right of box
upper_right_id = bytes([0x4])

upper_right_data = bytes([0x0, 0x0, 0x0, 0x1c, 0x1e, 0xe, 0x6, 0x6])

upper_right_save_custom_char = save_custom_chars + mem_bank_zero + upper_right_id + upper_right_data
upper_right_save_start_chars = save_start_chars + upper_right_id + upper_right_data

# Lower left of box
lower_left_id = bytes([0x5])

lower_left_data = bytes([0xc, 0xc, 0xe, 0xf, 0x7, 0x0, 0x0, 0x0])

lower_left_save_custom_char = save_custom_chars + mem_bank_zero + lower_left_id + lower_left_data
lower_left_save_start_chars = save_start_chars + lower_left_id + lower_left_data

# Lower right of box
lower_right_id = bytes([0x6])

lower_right_data = bytes([0x6, 0x6, 0xe, 0x1e, 0x1c, 0x0, 0x0, 0x0])

lower_right_save_custom_char = save_custom_chars + mem_bank_zero + lower_right_id + lower_right_data
lower_right_save_start_chars = save_start_chars + lower_right_id + lower_right_data

# Top and bottom of box
bar_id = bytes([0x0])

bar_data = bytes([0x0, 0x0,0x0,0x1F,0x1F,0x0,0x0,0x0])

bar_save_custom_char = save_custom_chars + mem_bank_zero + bar_id + bar_data
bar_save_start_chars = save_start_chars + bar_id + bar_data

# Sides of box
side_left_id = bytes([0x7])

side_left_data = bytes([0xc, 0xc,0xc,0xc,0xc,0xc,0xc,0xc])

side_left_save_custom_char = save_custom_chars + mem_bank_zero + side_left_id + side_left_data
side_left_save_start_chars = save_start_chars + side_left_id + side_left_data


side_right_id = bytes([0x2])

side_right_data = bytes([0x6, 0x6,0x6,0x6,0x6,0x6,0x6,0x6])

side_right_save_custom_char = save_custom_chars + mem_bank_zero + side_right_id + side_right_data
side_right_save_start_chars = save_start_chars + side_right_id + side_right_data


# saving custom characters to memory
port.write(bar_save_custom_char)
port.write(side_right_save_custom_char)
port.write(logo_save_custom_char)
port.write(upper_left_save_custom_char)
port.write(upper_right_save_custom_char)
port.write(lower_left_save_custom_char)
port.write(lower_right_save_custom_char)
port.write(side_left_save_custom_char)

# saving start screen characters
port.write(bar_save_start_chars)
port.write(side_left_save_start_chars)
port.write(logo_save_start_chars)
port.write(upper_left_save_start_chars)
port.write(upper_right_save_start_chars)
port.write(lower_left_save_custom_char)
port.write(lower_right_save_custom_char)
port.write(side_right_save_start_chars)

# loading characters from memory
port.write(load_custom_chars + mem_bank_zero)

logo = bytes([0x1])
side_right = bytes([0x2])
bar_left = bytes([0x3])
bar_right = bytes([0x4])
lower_left = bytes([0x5])
lower_right = bytes([0x6])
bar = bytes([0x0])
side_left = bytes([0x7])

# Data representation of board 

board_array = [[bar_left,bar,bar,bar,bar,bar,bar,bar,bar,bar,bar,bar,bar,bar,bar,bar,bar,bar,bar,bar_right],
               [side_left," "," "," "," "," ","I","n","m","a","r","s","a","t",logo," "," "," "," ",side_right],
               [side_left," "," "," "," ","G","o","v","e","r","n","m","e","n","t"," "," "," "," ",side_right],
               [lower_left,bar,bar,bar,bar,bar,bar,bar,bar,bar,bar,bar,bar,bar,bar,bar,bar,bar,bar,lower_right]]

# Loop and print the characters to the screen

for row in board_array:
    for char in row:
        if not (type(char) == str):
            change_start_screen = change_start_screen + char
        else:
            change_start_screen = change_start_screen+ char.encode()
        
port.write(change_start_screen)

