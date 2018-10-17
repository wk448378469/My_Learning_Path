# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 09:08:02 2018

@author: 凯风
"""

from abc import ABCMeta,abstractmethod

class Subject(metaclass = ABCMeta):
    @abstractmethod
    def registerObserver(observer):
        pass
    
    @abstractmethod
    def removeObserver(observer):
        pass
    
    @abstractmethod
    def notifyObservers():
        pass


class Observer(metaclass = ABCMeta):
    @abstractmethod
    def update(temp, humidity, pressure):
        pass

class DisplayElement(metaclass = ABCMeta):
    @abstractmethod
    def display():
        pass