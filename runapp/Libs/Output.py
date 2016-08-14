import wiringpi
import threading
import time

class Switch:

  def __init__(self, pinNumber):
    self.daemon = True
    self.pinNumber = pinNumber

    wiringpi.digitalWrite(self.pinNumber, 0)

  def turnOn(self):
    wiringpi.digitalWrite(self.pinNumber, 1)

  def turnOff(self):
    wiringpi.digitalWrite(self.pinNumber, 0)
