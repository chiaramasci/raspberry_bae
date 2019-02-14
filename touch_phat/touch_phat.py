#to install library
#curl https://get.pimoroni.com/touchphat  | bash

import touchphat
import time

def turnonled_all():
    touchphat.all_on()

def turnoffled_all():
    touchphat.all_off()

#led can be either a value from 1 to 6 or the pad name
#pad names: "Back", "A", "B", "C", "D", and "Enter"
def turnonled(led):
    touchphat.led_on(led)

def turnoffled(led):
    touchphat.led_off(led)

def light(duration_sec = None)
    if duration_sec == None:
        while True:
            for led in range(1,7):
                touchphat.led_on(led)
                time.sleep(0.25)
                touchphat.led_off(led)
    else:
        t_end = time.time() + duration_sec
        while time.time() < t_end:
            for led in range(1,7):
                touchphat.led_on(led)
                time.sleep(0.25)
                touchphat.led_off(led)

#pad can be either a value from 1 to 6 or the pad name
#pad names: "Back", "A", "B", "C", "D", and "Enter"
def set_action(pad,func,*args):
        @touchphat.on_touch(pad)
        func(args)
