# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 21:14:05 2018

@author: 凯风
"""

from abc import ABCMeta, abstractmethod

class Sauce(metaclass = ABCMeta):
    @abstractmethod
    def __str__(self):
        pass
    
class MarinaraSauce(Sauce):
    def __str__(self):
        return "Marinara Sauce"
        
class PlumTomatoSauce(Sauce):
    def __str__(self):
        return "Plum Tomato Sauce"

