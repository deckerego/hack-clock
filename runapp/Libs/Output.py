import wiringpi

global WIRINGPI_INIT
WIRINGPI_INIT = False

# So... I do acknowledge that Drogon considers calling the wiringPiSetup
# routines more than once a "fatal error," however using a global var
# in Python to guarantee once-only execution is a huge pain in the case of
# keeping run_clock.py succinct and free of clutter. So I'll take advantage
# of if(alreadyDoneThis) return 0; for now with apologies to Drogon
wiringpi.wiringPiSetupSys()

class Switch:
  def __init__(self, pinNumber):

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
