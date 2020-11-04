from Link import *
from Demand import *

class Variable:
    def __init__(self, link, demand):
        self.link = link
        self.demand = demand

    def __str__(self):
        return "x_" + self.link.firstElement + "-" + self.link.lastElement\
               + "_" + self.demand.firstElement + "-" + self.demand.lastElement