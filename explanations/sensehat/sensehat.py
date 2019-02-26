'''
This code shows only explanations of the methods needed to use SenseHat
'''

from sense_hat import SenseHat

sense = SenseHat()

#show message with given scroll speed and rgb colors (text_colour and back_colour)
sense.show_message("Hello world", scroll_speed = 0.1,text_colour = (55,55,55),back_colour = (255,255,255))

#show single letter
sense.show_letter("Z")

#display color
sense.clear((40, 60, 90))

#lights up pixel at x, y coordinates and with rgb colour
sense.set_pixel(2, 2, (0, 0, 255))

#works with an array of 64 elements.
#These elements are the rgb colours of the pixel at a given position
#remember the grid is 8X8
sense.set_pixels(array)

#rotates the display of the SenseHat by 90, 180, 270 degrees (0 stays the same)
sense.set_rotation(180)

#mirrors the display horizontally
sense.flip_h()

#or verically
sense.flip_v()

pressure = sense.get_pressure()
humidity = sense.get_humidity()
get_temperature()
get_temperature_from_pressure()
