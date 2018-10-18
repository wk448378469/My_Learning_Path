# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 17:27:42 2018

@author: 凯风
"""

from Beverage import Beverage
from abc import abstractmethod

class CondimentDecorator(Beverage):
    @abstractmethod
    def getDescription(self):
        pass