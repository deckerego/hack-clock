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
import datetime
from LEDBackpack import LEDBackpack

# ===========================================================================
# 7-Segment Display
# ===========================================================================

# This class is meant to be used with the four-character, seven segment
# displays available from Adafruit

class SevenSegment:
  disp = None

  # Hexadecimal character lookup table (row 1 = 0..9, row 2 = A..F)
  digits = [ 0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07, 0x7F, 0x6F, \
             0x77, 0x7C, 0x39, 0x5E, 0x79, 0x71 ]

  # Constructor
  def __init__(self, address=0x70, debug=False):
    if (debug):
      print "Initializing a new instance of LEDBackpack at 0x%02X" % address
    self.disp = LEDBackpack(address=address, debug=debug)

  def writeDigitRaw(self, charNumber, value):
    "Sets a digit using the raw 16-bit value"
    if (charNumber > 7):
      return
    # Set the appropriate digit
    self.disp.setBufferRow(charNumber, value)

  def writeDigit(self, charNumber, value, dot=False):
    "Sets a single decimal or hexademical value (0..9 and A..F)"
    if (charNumber > 7):
      return
    if (value > 0xF):
      return
    # Set the appropriate digit
    self.disp.setBufferRow(charNumber, self.digits[value] | (dot << 7))

  def setColon(self, state=True):
    "Enables or disables the colon character"
    # Warning: This function assumes that the colon is character '2',
    # which is the case on 4 char displays, but may need to be modified
    # if another display type is used
    if (state):
      self.disp.setBufferRow(2, 0xFFFF)
    else:
      self.disp.setBufferRow(2, 0)
