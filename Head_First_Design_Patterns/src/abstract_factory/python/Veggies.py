# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 20:58:18 2018

@author: 凯风
"""

from abc import ABCMeta, abstractmethod

class Veggies(metaclass = ABCMeta):
    @abstractmethod
    def __str__(self):
        pass

class BlackOlives(Veggies):
    def __str__(self):
        return "Black Olives"

class Eggplant(Veggies):
    def __str__(self):
        return "Eggplant"

class Garlic(Veggies):
    def __str__(self):
        return "Garlic"

class Mushroom(Veggies):
    def __str__(self):
        return "Mushroom"
        
class Onion(Veggies):
    def __str__(self):
        return "Onion"

class RedPepper(Veggies):
    def __str__(self):
        return "Red Pepper"

class Spinach(Veggies):
    def __str__(self):
        return "Spinach"