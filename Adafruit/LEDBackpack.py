###
# Copyright (c) 2012-2013 Limor Fried, Kevin Townsend and Mikey Sklar for Adafruit Industries. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met: * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution. * Neither the name of the nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Copied verbatim from https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/
###

import time
from copy import copy
from I2C import Adafruit_I2C

# ============================================================================
# LEDBackpack Class
# ============================================================================

class LEDBackpack:
  i2c = None

  # Registers
  __HT16K33_REGISTER_DISPLAY_SETUP        = 0x80
  __HT16K33_REGISTER_SYSTEM_SETUP         = 0x20
  __HT16K33_REGISTER_DIMMING              = 0xE0

  # Blink rate
  __HT16K33_BLINKRATE_OFF                 = 0x00
  __HT16K33_BLINKRATE_2HZ                 = 0x01
  __HT16K33_BLINKRATE_1HZ                 = 0x02
  __HT16K33_BLINKRATE_HALFHZ              = 0x03

  # Display buffer (8x16-bits)
  __buffer = [0x0000, 0x0000, 0x0000, 0x0000, \
              0x0000, 0x0000, 0x0000, 0x0000 ]

  # Constructor
  def __init__(self, address=0x70, debug=False):
    self.i2c = Adafruit_I2C(address)
    self.address = address
    self.debug = debug

    # Turn the oscillator on
    self.i2c.write8(self.__HT16K33_REGISTER_SYSTEM_SETUP | 0x01, 0x00)

    # Turn blink off
    self.setBlinkRate(self.__HT16K33_BLINKRATE_OFF)

    # Set maximum brightness
    self.setBrightness(15)

    # Clear the screen
    self.clear()

  def setBrightness(self, brightness):
    "Sets the brightness level from 0..15"
    if (brightness > 15):
      brightness = 15
    self.i2c.write8(self.__HT16K33_REGISTER_DIMMING | brightness, 0x00)

  def setBlinkRate(self, blinkRate):
    "Sets the blink rate"
    if (blinkRate > self.__HT16K33_BLINKRATE_HALFHZ):
       blinkRate = self.__HT16K33_BLINKRATE_OFF
    self.i2c.write8(self.__HT16K33_REGISTER_DISPLAY_SETUP | 0x01 | (blinkRate << 1), 0x00)

  def setBufferRow(self, row, value, update=True):
    "Updates a single 16-bit entry in the 8*16-bit buffer"
    if (row > 7):
      return                    # Prevent buffer overflow
    self.__buffer[row] = value  # value # & 0xFFFF
    if (update):
      self.writeDisplay()       # Update the display

  def getBufferRow(self, row):
    "Returns a single 16-bit entry in the 8*16-bit buffer"
    if (row > 7):
      return
    return self.__buffer[row]

  def getBuffer(self):
    "Returns a copy of the raw buffer contents"
    bufferCopy = copy(self.__buffer)
    return bufferCopy

  def writeDisplay(self):
    "Updates the display memory"
    bytes = []
    for item in self.__buffer:
      bytes.append(item & 0xFF)
      bytes.append((item >> 8) & 0xFF)
    self.i2c.writeList(0x00, bytes)

  def clear(self, update=True):
    "Clears the display memory"
    self.__buffer = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    if (update):
      self.writeDisplay()

led = LEDBackpack(0x70)
