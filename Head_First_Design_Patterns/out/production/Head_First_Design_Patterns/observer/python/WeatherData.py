# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 09:24:48 2018

@author: 凯风
"""

from interface import Subject, Observer

class WeatherData(Subject):
    
    def __init__(self):
        self.observers = []
        self.temperature = 0.0
        self.humidity = 0.0
        self.pressure = 0.0
    
    def registerObserver(self, observer):
        if(observer not in self.observers and isinstance(observer, Observer)):
            self.observers.append(observer)

    def removeObserver(self, observer):
        if (observer in self.observers):
            self.observers.remove(observer)
    
    def notifyObservers(self):
        for obs in self.observers:
            obs.update(self.temperature, self.humidity, self.pressure)
    
    def measurementsChanged(self):
        self.notifyObservers()
    
    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurementsChanged()
    
    