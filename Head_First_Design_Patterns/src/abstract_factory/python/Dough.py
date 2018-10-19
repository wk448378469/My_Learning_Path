# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 21:00:50 2018

@author: 凯风
"""

from abc import ABCMeta, abstractmethod

class Dough(metaclass = ABCMeta):
    @abstractmethod
    def __str__(self):
        pass

class ThickCrustDough(Dough):
    def __str__(self):
        return "Thick Crust Dough"

class ThinCrustDough(Dough):
    def __str__(self):
        return "Thin Crust Dough"