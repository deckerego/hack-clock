import threading
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
        self.start()

    def __del__(self):
        self.__running = False

    def run(self):
        while self.__running:
            if self.tickFunc: self.tickFunc()

            self.__waitLock.acquire()
            totalWait = self.__RESOLUTION + self.additionalWait
            self.additionalWait = 0
            self.__waitLock.release()
            time.sleep(totalWait / 1000.0)

    def onTick(self, tickFunc):
        self.tickFunc = tickFunc

    def waitAbout(self, seconds):
        self.__waitLock.acquire()
        self.additionalWait = seconds * 1000
        self.__waitLock.release()
