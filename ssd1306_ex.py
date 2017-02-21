from ssd1306 import *

def show_bitmap(filename):
    set_pos()
    set_zoom(0)
    with open(filename, 'rb') as my_file:
        for i in range(0, 16):
            i2c.write(ADDR, b'\x40' + my_file.read(64))


