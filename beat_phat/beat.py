#curl -sS get.pimoroni.com/phatbeat  | bash

#audio test from command line: speaker-test -c2 -t wav

import phatbeat

'''
LEDS
They can be turned on/off by:
- considering them as single pixels indexed from 0 to 15 (included)
- as two different columns ("channel") in which each pixel is indexed from 0 to 6 (included)
'''

def turnon_led(led, red, green, blue, channel_mode = False):
    if channel_mode = True:
        for channel in (0,1):
            phatbeat.set_pixel(led, red, green, blue, channel=channel)
    else:
        phatbeat.set_pixel(led, red, green, blue)

def clear_leds():
    phatbeat.clear()
    phatbeat.show()


'''
buttons
phatbeat.BTN_FASTFWD
phatbeat.BTN_REWIND
phatbeat.BTN_PLAYPAUSE
phatbeat.BTN_VOLUP
phatbeat.BTN_VOLDN
phatbeat.BTN_ONOFF
'''

buttons = [phatbeat.BTN_FASTFWD,phatbeat.BTN_REWIND,phatbeat.BTN_PLAYPAUSE,phatbeat.BTN_VOLUP,
phatbeat.BTN_VOLDN,
phatbeat.BTN_ONOFF]

def addaction_button (button,func,*args):
    if(button in buttons):
        @phatbeat.on(button)
        func(args)
    else:
        raise Exception('button is not in the list of available options (see buttons)')
