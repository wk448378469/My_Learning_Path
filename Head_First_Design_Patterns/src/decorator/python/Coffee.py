# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 17:28:56 2018

@author: 凯风
"""

from Beverage import Beverage

class Espresso(Beverage):
    def __init__(self):
        self.description = "Espresso"
    
    def cost(self):
        return 1.99

class HouseBlend(Beverage):
    def __init__(self):
        self.description = "House Blend Coffee"
    
    def cost(self):
        return 0.89

class DarkRoast(Beverage):
    def __init__(self):
        self.description = "Dark Roast"
    
    def cost(self):
        return 0.99

class Decaf(Beverage):
    def __init__(self):
        self.description = "Decaf"
    
    def cost(self):
        return 1.05
