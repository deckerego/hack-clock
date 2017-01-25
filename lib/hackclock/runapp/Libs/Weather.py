import datetime
from datetime import timedelta
import urllib2
import xml.etree.ElementTree as ET
from decimal import Decimal

class Weather:
  __TEMP_F = 'temp_f'
  __TEMP_C = 'temp_c'
  __WINDCHILL_F = 'windchill_f'
  __WINDCHILL_C = 'windchill_c'
  __WINDSPEED_MPH = 'wind_mph'
  __WINDSPEED_KT = 'wind_kt'
  __RELATIVE_HUMIDITY = 'relative_humidity'
  __LOCATION = 'location'
  __STATION = 'station_id'
  __REFRESH_DELTA = timedelta(minutes=60)

  def __init__(self, weatherStation):
    self.last_fetch = datetime.datetime.min
    # List of weather stations is available at http://forecast.weather.gov/stations.php
    self.url = "http://w1.weather.gov/xml/current_obs/%s.xml" % weatherStation

  def __refreshData(self):
    refresh_delta = datetime.datetime.now() - self.last_fetch

    # Don't refresh data after every call - wait DELTA seconds
    if refresh_delta > self.__REFRESH_DELTA:
      response = urllib2.urlopen(self.url)
      data = response.read()
      self.root = ET.fromstring(data)
      self.last_fetch = datetime.datetime.now()

  def getCurrentTemp(self):
    self.__refreshData()
    temp_string = self.root.findall(self.__TEMP_F)[0].text
    return int(Decimal(temp_string).to_integral())

  def getCurrentWindchill(self):
    self.__refreshData()
    temp_string = self.root.findall(self.__WINDCHILL_F)[0].text
    return int(Decimal(temp_string).to_integral())

  def getCurrentWindspeed(self):
    self.__refreshData()
    temp_string = self.root.findall(self.__WINDSPEED_MPH)[0].text
    return int(Decimal(temp_string).to_integral())

  def getCurrentRelativeHumidity(self):
    self.__refreshData()
    temp_string = self.root.findall(self.__RELATIVE_HUMIDITY)[0].text
    return int(Decimal(temp_string).to_integral())

  def getLocation(self):
    self.__refreshData()
    return self.root.findall(self.__LOCATION)[0].text

  def getStation(self):
    self.__refreshData()
    return self.root.findall(self.__STATION)[0].text
