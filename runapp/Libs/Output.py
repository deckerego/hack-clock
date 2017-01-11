import wiringpi

class Switch:
  def __init__(self, pinNumber):

    self.pinNumber = pinNumber

    # So... I do acknowledge that Drogon considers calling the wiringPiSetup
    # routines more than once a "fatal error," however using a global var
    # in Python to guarantee once-only execution is a huge pain in the case of
    # keeping run_clock.py succinct and free of clutter. So I'll take advantage
    # of if(alreadyDoneThis) return 0; for now with apologies to Drogon
    wiringpi.wiringPiSetupSys()

    wiringpi.digitalWrite(self.pinNumber, 0)

  def turnOn(self):
    wiringpi.digitalWrite(self.pinNumber, 1)

  def turnOff(self):
    wiringpi.digitalWrite(self.pinNumber, 0)
