# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 17:34:00 2018

@author: 凯风
"""

from Beverage import Beverage
from CondimentDecorator import CondimentDecorator

class Mocha(CondimentDecorator):
    
    def __init__(self, beverage):
        self.beverage = beverage
    
    def getDescription(self):
        return self.beverage.getDescription() + ", Mocha"
    
    def cost(self):
        return self.beverage.cost() + 0.2


class Soy(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage
    
    def getDescription(self):
        return self.beverage.getDescription() + ", Soy"
    
    def cost(self):
        return self.beverage.cost() + 0.15


class Whip(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage
    
    def getDescription(self):
        return self.beverage.getDescription() + ", Whip"
    
    def cost(self):
        return self.beverage.cost() + 0.1
        