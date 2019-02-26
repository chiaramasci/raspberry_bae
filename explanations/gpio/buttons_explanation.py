'''
This code shows only explanations of the methods needed to use buttons
'''

#import module
import RPi.GPIO as GPIO

#set mode in which pins are enumerated
GPIO.setmode(GPIO.BCM)

#setting input or output mode for pin
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)

#--PARENTHESES ABOUT PULL UP RESISTORS --
#if you want to set a pull up (useful in case of buttons and switches)
#more info about pull up resistors: https://learn.sparkfun.com/tutorials/pull-up-resistors/all

#in this case, when button is pressed it returns 0
#the button has to be connected to the ground
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#--CLOSED PARENTHESES ABOUT PULL UP RESISTORS--

#this method detects whether the button has been pressed
#(This works if no pull resistors has been set or if there is a pull down resistor)
#it has to be put in a while loop has it has to continuously check the state of the button
if(GPIO.input(23) == 1):
    print(“Button 1 pressed”)


def fun_function():
    print "so much fuuuuun"

GPIO.add_event_detect(23, GPIO.RISING, callback=fun_function, bouncetime=300)


#this command has to be put at the end of your program
#as during the program you have manipulated the state of your pins, you have to reset them
#in order to make them work correctly in your other programs
GPIO.cleanup()
