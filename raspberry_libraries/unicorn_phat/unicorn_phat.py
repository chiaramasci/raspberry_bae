#to install library
#curl https://get.pimoroni.com/unicornhat  | bash

import unicornhat as uh
import time
import colorsys

def initialize(brightness = 0.5):
    uh.set_layout(uh.PHAT)
    uh.brightness(brightness)

def turnon_pixel(x,y,red,green,blue):
    uh.set_pixel(x, y, red, green, blue)
    uh.show()

def turnoff_pixel(x,y):
    uh.set_pixel(x,y,0,0,0)
    uh.show

def turnoff_all():
    uh.clear()
    uh.show()

def turnon_all(red,green,blue):
    for x in range(8):
        for y in range(4):
            uh.set_pixel(x, y, 0, 255, 255)
    uh.show()

def blink_all(red,green,blue,duration_sec = None,blink_time = 0.25):
    if duration_sec == None:
        while True:
            turnon_all(red,green,blue)
            time.sleep(blink_time)
            uh.clear()
            uh.show()
            time.sleep(blink_time)
    else:
        t_end = time.time() + duration_sec
        while time.time() < t_end:
            turnon_all(red,green,blue)
            time.sleep(blink_time)
            uh.clear()
            uh.show()
            time.sleep(blink_time)
