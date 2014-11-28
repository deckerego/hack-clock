from Adafruit.SevenSegment import SevenSegment
from bitstring import BitArray

class ClockDisplay(SevenSegment):
  # Indicator Bit Flags
  __MID_COLON                = 14
  __LEFT_TOP                 = 13
  __LEFT_BOTTOM              = 12
  __RIGHT_TOP                = 11

  def __init__(self, address=0x70):
    SevenSegment.__init__(self, address)
    self.showTime = True

  def setBrightness(self, level):
    self.disp.setBrightness(level)

  def setColon(self, state=True):
    row = BitArray('uint:16=%d' % self.disp.getBufferRow(2))
    row[self.__MID_COLON] = state
    self.disp.setBufferRow(2, int(row.hex, 16))

  def setEvening(self, state=True):
    row = BitArray('uint:16=%d' % self.disp.getBufferRow(2))
    row[self.__LEFT_TOP] = state
    self.disp.setBufferRow(2, int(row.hex, 16))

  def setMinutes(self, minutes):
    self.writeDigit(3, int(minutes / 10))   # Tens
    self.writeDigit(4, minutes % 10)        # Ones

  def setHours(self, hours):
    self.writeDigit(0, int(hours / 10))   # Tens
    self.writeDigit(1, hours % 10)        # Ones
