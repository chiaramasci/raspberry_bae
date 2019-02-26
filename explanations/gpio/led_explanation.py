'''
This code shows only explanations of the methods needed to use leds
'''

import RPi.GPIO as GPIO

#set mode in which pins are enumerated
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)

#turn on led
GPIO.output(18, GPIO.HIGH)

#turn off led
GPIO.output(18, GPIO.LOW)

#this command has to be put at the end of your program
#as during the program you have manipulated the state of your pins, you have to reset them
#in order to make them work correctly in your other programs
GPIO.cleanup()
