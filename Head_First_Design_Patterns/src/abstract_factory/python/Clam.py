# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 21:16:39 2018

@author: 凯风
"""

from abc import ABCMeta, abstractmethod

class Clam(metaclass = ABCMeta):
    @abstractmethod
    def __str__(self):
        pass

class FreshClams(Clam):
    def __str__(self):
        return "Fresh Clams"

class FrozenClams(Clam):
    def __str__(self):
        return "Frozen Clams"