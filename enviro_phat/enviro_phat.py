#curl https://get.pimoroni.com/envirophat | bash

from envirophat import light
from envirophat import leds
from envirophat import weather
from envirophat import motion
from envirophat import analog
import time

#light/color sensing

def light_sensing():
    return light.light()

def color_sensing(accurate = True):
    if(accurate)
        leds.on()
        time.sleep(0.5)
    color = light.rgb()
    time.sleep(0.5)
    if(accurate)
        leds.off()

    return color

#temperature and pressure

#degrees Celsius
def temp_sensing():
    return weather.temperature()

#hecto Pascals
def pressure_sensing():
    return weather.pressure(unit='hPa')

#HEADING AND ACCELEROMETER

north = 0

def compass_calibration():
    print "Point the Enviro pHAT with the text the right way up (relative to you) towards north"
    north = motion.heading()

def compass():
    return (motion.heading() - north) % 360
