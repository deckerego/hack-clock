import threading
import datetime
import time

class Clock(threading.Thread):
    __RESOLUTION = 1000
    __running = True
    __waitLock = threading.Lock()

    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = False
        self.tickFunc = None
        self.additionalWait = 0
        self.timedEvents = []
        self.timedEventsIdx = -1

        self.atTime(0, 0, None) # The EOF event

        self.start()

    def __del__(self):
        self.__running = False

    def __executeEvents(self):
        if self.timedEventsIdx > -1:
            now = datetime.datetime.now()
            currentHash = (now.hour * 60) + now.minute
            (timeHash, action) = self.timedEvents[self.timedEventsIdx]

            if timeHash == currentHash:
                self.timedEventsIdx = (self.timedEventsIdx + 1) % len(self.timedEvents)
                if action: action()

    def run(self):
        while self.__running:
            if self.tickFunc: self.tickFunc()
            self.__executeEvents()

            self.__waitLock.acquire()
            totalWait = self.__RESOLUTION + self.additionalWait
            self.additionalWait = 0
            self.__waitLock.release()
            time.sleep(totalWait / 1000.0)

    def atTime(self, hour, minute, action):
        timeHash = (hour * 60) + minute
        event = (timeHash, action)
        self.timedEvents.append(event)
        self.timedEvents = sorted(self.timedEvents)

        now = datetime.datetime.now()
        currentHash = (now.hour * 60) + now.minute
        # Find the index of the next event that should fire based on the tuple's time key
        self.timedEventsIdx = next((self.timedEvents.index(evt) for evt in self.timedEvents if evt[0] >= currentHash), 0)

    def onTick(self, tickFunc):
        self.tickFunc = tickFunc

    def waitAbout(self, seconds):
        self.__waitLock.acquire()
        self.additionalWait = seconds * 1000
        self.__waitLock.release()
