from Adafruit.SevenSegment import SevenSegment

class ClockDisplay(SevenSegment):
  # Indicator Flags
  __MID_COLON                = 0x0002
  __LEFT_TOP                 = 0x0004
  __LEFT_BOTTOM              = 0x0008
  __RIGHT_TOP                = 0x0010

  def setBrightness(self, level):
    self.disp.setBrightness(level)

  def setColon(self, state=True):
    flag = self.__MID_COLON if state else 0x0000
    row = self.disp.getBufferRow(2) | flag
    self.disp.setBufferRow(2, row)

  def setEvening(self, state=True):
    flag = self.__LEFT_TOP if state else 0x0000
    row = self.disp.getBufferRow(2) | flag
    self.disp.setBufferRow(2, row)

  def setMinutes(self, minutes):
    self.writeDigit(3, int(minutes / 10))   # Tens
    self.writeDigit(4, minutes % 10)        # Ones

  def setHours(self, hours):
    self.writeDigit(0, int(hours / 10))   # Tens
    self.writeDigit(1, hours % 10)        # Ones
