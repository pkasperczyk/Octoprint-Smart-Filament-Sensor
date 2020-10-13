import threading
import time

class FilamentMotionSensor(threading.Thread):
    keepRunning = True

    # Initialize FilamentMotionSensor
    #def __init__(self, threadID, threadName, pPrinter, pSamplingTime):
    def __init__(self, threadID, threadName, pPrinter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = threadName
        #self.pSamplingTime = pSamplingTime
        self._printer = pPrinter

    # Override run method of threading
    # Poll printer with M114 to detect current position in a configured sampling time
    def run(self):
        while self.keepRunning:
            self._printer.commands("M114")
            time.sleep(1)
        