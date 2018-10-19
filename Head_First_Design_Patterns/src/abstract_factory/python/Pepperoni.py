# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 21:17:34 2018

@author: 凯风
"""

from abc import ABCMeta, abstractmethod

class Pepperoni(metaclass = ABCMeta):
    @abstractmethod
    def __str__(self):
        pass

class SlicedPepperoni(Pepperoni):
    def __str__(self):
        return "Sliced Pepperoni"
        


