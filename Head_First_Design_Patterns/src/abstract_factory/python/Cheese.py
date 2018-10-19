# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 21:15:19 2018

@author: 凯风
"""

from abc import ABCMeta, abstractmethod

class Cheese(metaclass = ABCMeta):
    @abstractmethod
    def __str__(self):
        pass

class MozzarellaCheese(Cheese):
    def __str__(self):
        return "Mozzarella Cheese"

class ParmesanCheese(Cheese):
    def __str__(self):
        return "Parmesan Cheese"
        
class ReggianoCheese(Cheese):
    def __str__(self):
        return "Reggiano Cheese"