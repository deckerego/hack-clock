#/bin/python
# MUST BE RUN AS ROOT - this sets proper internal pull up resistors for GPIO pins
# This is a temporary work-around until the wiringPi gpio command can set this

import RPi.GPIO as GPIO
import sys

gpioPin = int(sys.argv[1])
print "Setting BCM GPIO %d to INPUT mode with internal pullup resistor" % gpioPin

GPIO.setmode(GPIO.BCM)
GPIO.setup(gpioPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
