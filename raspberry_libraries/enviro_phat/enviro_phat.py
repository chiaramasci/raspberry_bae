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
    if(accurate):
        leds.on()
        time.sleep(0.5)
    color = light.rgb()
    time.sleep(0.5)
    if(accurate):
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

def get_accelerometer_instant():
    return motion.accelerometer()

def print_accelerometer_movement(duration_sec = None):
    if duration_sec == None:
        while True:
            print(get_accelerometer_instant())
            time.sleep(0.1)
    else:
        t_end = time.time() + duration_sec
        while time.time() < t_end:
            print(get_accelerometer_instant())
            time.sleep(0.1)

north = 0

def compass_calibration():
    print "Point the Enviro pHAT with the text the right way up (relative to you) towards north and press ENTER"
    north = motion.heading()

#0 is north and 180 is south
#However without calibration (see compass_calibration), measuraments can be wrong
def compass():
    return (motion.heading() - north) % 360

#OTHER ANALOG SENSORS
def read_analog(inp):
    if inp == 4:
        return analog.read_all()
    else:
        return analog.read(inp)
