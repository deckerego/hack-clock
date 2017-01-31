import httplib
import logging
import json
import datetime
import platform

logger = logging.getLogger('ifttt')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
logger.addHandler(console)

class IFTTT:
  __SERVER = "maker.ifttt.com"
  __PORT = 443
  __KEY = None
  __HEADERS = { "Content-type": "application/json" }
  __NAME = "hackclock"

  def __init__(self, key):
      self.__NAME = platform.node()
      self.__KEY = key

  def sendMakerEvent(self, eventName):
      if not self.__KEY:
          logger.error("IFTTT Maker Key is not set! Will not send event.")
          return

      datejson = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
      body = json.dumps({"value1": self.__NAME, "value2": datejson})
      logger.info("IFTTT Body: %s" % body)

      conn = httplib.HTTPSConnection(self.__SERVER, self.__PORT)
      conn.request("POST", "/trigger/wake_up/with/key/%s" % self.__KEY, body, self.__HEADERS)

      response = conn.getresponse()
      logger.info("IFTTT Response: %s %s" % (response.reason, str(response.status)))
      conn.close()
