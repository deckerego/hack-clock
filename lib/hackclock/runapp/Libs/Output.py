from hackclock.runapp.Libs.WiringPi import WiringPiSingleton
import wiringpi

class Switch:
  def __init__(self, pinNumber):

    self.pinNumber = pinNumber

    WiringPiSingleton().setup()

    wiringpi.digitalWrite(self.pinNumber, 0)

  def turnOn(self):
    wiringpi.digitalWrite(self.pinNumber, 1)

  def turnOff(self):
    wiringpi.digitalWrite(self.pinNumber, 0)
