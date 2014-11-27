import wiringpi2
import threading
import time

class Button(threading.Thread):
  __RESOLUTION = 100
  __running = True

  def __init__(self, pinNumber):
    threading.Thread.__init__(self)
    wiringpi2.wiringPiSetupSys()
    self.daemon = True
    self.pinNumber = pinNumber

  def run(self):
    while self.__running:
      if wiringpi2.digitalRead(self.pinNumber):
        self.myFunction(self.pinNumber)
        time.sleep(self.__RESOLUTION / 1000.0)

  def whenPressed(self, myFunction):
    self.myFunction = myFunction
    self.start()
