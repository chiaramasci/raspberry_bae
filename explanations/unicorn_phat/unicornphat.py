import colorsys
import math
import time

import unicornhat as uh

#set phat instead of hat
uh.set_layout(uh.PHAT)

#flip the pixel coordinates (either 0 or 180)
uh.rotation(180)

#set brightness
uh.brightness(0.5)

#set pixel
while True:
    uh.set_pixel(0, 0, 255, 0, 0)
    uh.show()