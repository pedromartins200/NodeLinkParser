class Link:
    def __init__(self, firstElement, lastElement, capacity):
        self.firstElement = firstElement
        self.lastElement = lastElement
        self.capacity = capacity

    def __str__(self):
        return "" + self.firstElement + " " + self.lastElement + " capacity:" + self.capacity
