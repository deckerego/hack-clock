from hackclock.runapp.Libs.Clock import Clock
from numbers import Number

tickCount = None

clock = Clock()

"""Describe this function...
"""
def clockTick():
  global tickCount
  tickCount = (tickCount if isinstance(tickCount, Number) else 0) + 1


tickCount = 0
clock.onTick(clockTick)
