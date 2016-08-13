import wiringpi
import threading
import time

global WIRINGPI_INIT
WIRINGPI_INIT = False

class Button(threading.Thread):
  __RESOLUTION = 100
  __running = True
  __initialState = 0
  __previousState = 0

  def __init__(self, pinNumber):
    threading.Thread.__init__(self)

    self.daemon = True
    self.pinNumber = pinNumber

    if not WIRINGPI_INIT: # Can only init this once per execution!
        wiringpi.wiringPiSetupSys()
        global WIRINGPI_INIT
        WIRINGPI_INIT = True

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
