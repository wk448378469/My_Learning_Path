# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 22:01:44 2018

@author: 凯风
"""

from abc import ABCMeta, abstractmethod

class Duck(metaclass = ABCMeta):
    @abstractmethod
    def quack(self):
        pass
    
    @abstractmethod
    def fly(self):
        pass


class Turkey(metaclass = ABCMeta):
    @abstractmethod
    def gobble(self):
        pass
    
    @abstractmethod
    def fly(self):
        pass

