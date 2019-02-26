import explorerhat
import time

#leds

#there are 4 leds: blue,yellow (it is more orange than yellow, but... Eh),red,green

def turnon_all():
    explorerhat.light.on()
    
def turnoff_all():
    explorerhat.light.off()
    
def turnon_led(*leds)
    for led in leds:
        if led == "blue":
            explorerhat.light.blue.on()
        elif led == "yellow":
            explorerhat.light.yellow.on()
        elif led == "red":
            explorerhat.light.red.on()
        elif led == "green":
            explorerhat.light.green.on()
        else:
            print "invalid led color"
            
def turnoff_led(*leds)
    for led in leds:
        if led == "blue":
            explorerhat.light.blue.off()
        elif led == "yellow":
            explorerhat.light.yellow.off()
        elif led == "red":
            explorerhat.light.red.off()
        elif led == "green":
            explorerhat.light.green.off()
        else:
            print "invalid led color"

def pulse_all(duration_sec = None)
    if duration_sec == None:
        explorerhat.light.pulse()
    else:
        explorerhat.light.pulse()
        time_end = time.time + duration_sec
        while time.time < time_end:
            print "pulse"
        explorerhat.light.off()
        
def pulse_led(*leds,duration_sec = None)
    if duration_sec == None:
        for led in leds:
            if led == "blue":
                explorerhat.light.blue.pulse()
            elif led == "yellow":
                explorerhat.light.yellow.pulse()
            elif led == "red":
                explorerhat.light.red.pulse()
            elif led == "green":
                explorerhat.light.green.pulse()
            else:
                print "invalid led color"
    else:
        for led in leds:
            if led == "blue":
                explorerhat.light.blue.pulse()
            elif led == "yellow":
                explorerhat.light.yellow.pulse()
            elif led == "red":
                explorerhat.light.red.pulse()
            elif led == "green":
                explorerhat.light.green.pulse()
            else:
                print "invalid led color"
        time_end = time.time + duration_sec
        while time.time < time_end:
            print "pulse"
        explorerhat.light.off()
        
#input
def readinput_all():
    return explorerhat.input.read()

def readinput_one():
    return explorerhat.input.one.read()

def readinput_two():
    return explorerhat.input.two.read()

def readinput_three():
    return explorerhat.input.three.read()

def readinput_four():
    return explorerhat.input.four.read()

#output
#TODO look for output

        
#analog
def readanalog_all():        
    return explorerhat.analog.read()
    
def readanalog_one():
    return explorerhat.analog.one.read()

def readanalog_two():
    return explorerhat.analog.two.read()

def readanalog_three():
    return explorerhat.analog.three.read()

def readanalog_four():
    return explorerhat.analog.four.read()
            
#motor
#TODO: check why it does not work
explorerhat.motor.one.forward(100)
explorerhat.motor.one.stop()