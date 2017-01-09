import wiringpi

global WIRINGPI_INIT
WIRINGPI_INIT = False

class Switch:

  def __init__(self, pinNumber):
    self.daemon = True
    self.pinNumber = pinNumber

    if not WIRINGPI_INIT: # Can only init this once per execution!
        wiringpi.wiringPiSetupSys()
        global WIRINGPI_INIT
        WIRINGPI_INIT = True

    wiringpi.digitalWrite(self.pinNumber, 0)

  def turnOn(self):
    wiringpi.digitalWrite(self.pinNumber, 1)

  def turnOff(self):
    wiringpi.digitalWrite(self.pinNumber, 0)
