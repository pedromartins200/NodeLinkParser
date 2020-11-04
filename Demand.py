class Demand:
    def __init__(self, firstElement, lastElement, volume):
        self.firstElement = firstElement
        self.lastElement = lastElement
        self.volume = volume

    def getVolume(self):
        return str(self.volume)

    def __str__(self):
        return "" + self.firstElement + " " + self.lastElement + " volume:" + self.volume