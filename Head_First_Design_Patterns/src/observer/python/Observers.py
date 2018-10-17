# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 09:33:51 2018

@author: 凯风
"""

from interface import Observer, DisplayElement
from WeatherData import WeatherData

class CurrentConditionsDisplay(Observer, DisplayElement):
    
    def __init__(self, weatherData):
        if (isinstance(weatherData, WeatherData)):
            self.temperature = 0.0
            self.humidity = 0.0
            self.weatherData = weatherData
            weatherData.registerObserver(self)
    
    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.display()
        
    def display(self):
        print("Current conditions: {0} F degrees and {1}% humidity".format(
                self.temperature, self.humidity))


class StatisticsDisplay(Observer, DisplayElement):
    
    def __init__(self, weatherData):
        if (isinstance(weatherData, WeatherData)):
            self.maxTemp = 0.0
            self.minTemp = 200.0
            self.tempSum = 0.0
            self.numReadings = 0
            self.weatherData = weatherData
            weatherData.registerObserver(self)
    
    def update(self, temperature, humidity, pressure):
        self.tempSum += temperature
        self.numReadings = self.numReadings + 1
        
        if(temperature > self.maxTemp):
            self.maxTemp = temperature
        if(temperature < self.minTemp):
            self.minTemp = temperature
        
        self.display()
    
    def display(self):
        print("Avg/Max/Min temperature = {0}/{1}/{2}".format(
                self.tempSum/self.numReadings, self.maxTemp, self.minTemp))


class ForecastDisplay(Observer, DisplayElement):
    
    def __init__(self, weatherData):
        if(isinstance(weatherData, WeatherData)):
            self.currentPressure = 29.92
            self.lastPressure = 0.0
            self.weatherData = weatherData
            weatherData.registerObserver(self)
    
    def update(self, temperature, humidity, pressure):
        self.lastPressure = self.currentPressure
        self.currentPressure = temperature
        self.display()
    
    def display(self):
        if (self.currentPressure > self.lastPressure):
            temp = "Improving weather on the way!"
        elif (self.currentPressure == self.lastPressure):
            temp = "More of the same"
        else:
            temp = "Watch out for cooler, rainy weather"
        
        print("Forecast: " + temp)



















