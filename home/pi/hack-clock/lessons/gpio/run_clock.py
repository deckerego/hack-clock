from datetime import datetime
from hackclock.runapp.Libs.SevenSegment import Display
from hackclock.runapp.Libs.Output import Switch
from hackclock.runapp.Libs.Clock import Clock
from hackclock.runapp.Libs.Input import Button

Is_Evening = None
LED_On = None

display = Display()

gpio_25 = Switch(25)

"""Describe this function...
"""
def showCurrentTime():
  global Is_Evening, LED_On
  Is_Evening = datetime.now().hour > 12
  LED_On = not LED_On
  display.setHours((datetime.now().hour - 12 if Is_Evening else datetime.now().hour))
  display.setColon(True)
  display.setEvening(Is_Evening)
  display.setMinutes(datetime.now().minute)
  if LED_On:
    gpio_25.turnOn();
  else:
    gpio_25.turnOff();

clock = Clock()

"""Describe this function...
"""
def bright():
  global Is_Evening, LED_On
  display.setBrightness(15)

gpio_23 = Button(23)

gpio_24 = Button(24)

"""Describe this function...
"""
def dim():
  global Is_Evening, LED_On
  display.setBrightness(3)


LED_On = False
clock.onTick(showCurrentTime)
display.setBrightness(9)

gpio_23.whenPressed(dim)

gpio_24.whenPressed(bright)
