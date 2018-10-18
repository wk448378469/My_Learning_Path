# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 17:23:20 2018

@author: 凯风
"""

from abc import ABCMeta, abstractmethod

class Beverage(metaclass = ABCMeta):
    
    def __init__(self):
        self.description = "Unknown Beverage"
    
    def getDescription(self):
        return self.description
    
    @abstractmethod
    def cost(self):
        pass