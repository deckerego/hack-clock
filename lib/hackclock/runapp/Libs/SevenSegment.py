from Adafruit.SevenSegment import SevenSegment
from Adafruit.LEDBackpack import LEDBackpack
from bitstring import BitArray

class Display(SevenSegment):
  # Indicator Bit Flags
  __MID_COLON                = 14
  __LEFT_TOP                 = 13
  __LEFT_BOTTOM              = 12
  __RIGHT_TOP                = 11

  def __init__(self, address=0x70):
    self.display = LEDBackpack(address=address)
    self.showTime = True

  def setBrightness(self, level):
    self.display.setBrightness(level)

  def setColon(self, state=True):
    row = BitArray('uint:16=%d' % self.display.getBufferRow(2))
    row[self.__MID_COLON] = state
    self.display.setBufferRow(2, int(row.hex, 16))

  def setEvening(self, state=True):
    row = BitArray('uint:16=%d' % self.display.getBufferRow(2))
    row[self.__LEFT_TOP] = state
    self.display.setBufferRow(2, int(row.hex, 16))

  def setMinutes(self, minutes):
    self._writeDigit(3, int(minutes / 10))   # Tens
    self._writeDigit(4, minutes % 10)        # Ones

  def setHours(self, hours):
    hourTens = int(hours / 10) if hours >= 10 else None
    self._writeDigit(0, hourTens)          # Tens
    self._writeDigit(1, hours % 10)        # Ones

  def _writeDigit(self, charNumber, value, dot=False):
    if (charNumber > 7): return
    if (value > 9): return

    hexValue = SevenSegment.digits[value] if value != None else 0x00
    self.display.setBufferRow(charNumber, hexValue)
