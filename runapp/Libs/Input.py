import wiringpi
import threading
import time

# So... I do acknowledge that Drogon considers calling the wiringPiSetup
# routines more than once a "fatal error," however using a global var
# in Python to guarantee once-only execution is a huge pain in the case of
# keeping run_clock.py succinct and free of clutter. So I'll take advantage
# of if(alreadyDoneThis) return 0; for now with apologies to Drogon
wiringpi.wiringPiSetupSys()

class Button(threading.Thread):
  __RESOLUTION = 100
  __running = True
  __initialState = 0
  __previousState = 0

  def __init__(self, pinNumber):
    threading.Thread.__init__(self)

    self.daemon = True
    self.pinNumber = pinNumber

    self.__initialState = wiringpi.digitalRead(self.pinNumber)
    self.__previousState = self.__initialState

  def run(self):
    while self.__running:
      state = wiringpi.digitalRead(self.pinNumber)
      if state != self.__previousState:
        self.onStateChange(state)

      self.__previousState = state
      time.sleep(self.__RESOLUTION / 1000.0)

  def onStateChange(self, state):
    if state != self.__initialState:
      self.myFunction()

  def whenPressed(self, myFunction):
    self.myFunction = myFunction
    self.start()
