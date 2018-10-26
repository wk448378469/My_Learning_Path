# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 15:22:50 2018

@author: 凯风
"""

from abc import ABCMeta, abstractmethod

class Iterator(metaclass = ABCMeta):
    @abstractmethod
    def hasNext(self):
        pass
    
    @abstractmethod
    def _next(self):
        pass


class Menu(metaclass = ABCMeta):
    @abstractmethod
    def createIterator(self):
        pass


class MenuItem(object):
    def __init__(self, name, desc, vegetarian, price):
        self.name = name
        self.desc = desc
        self.vegetarian = vegetarian
        self.price = price