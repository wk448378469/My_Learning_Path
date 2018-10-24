# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 08:56:50 2018

@author: 凯风
"""

from abc import ABCMeta, abstractmethod

class Voltage220(object):
    def output220V(self):
        src = 220
        print("我是" + str(src) + "V")
        return src

class Voltage5(metaclass = ABCMeta):
    @abstractmethod
    def output5V(self):
        pass



