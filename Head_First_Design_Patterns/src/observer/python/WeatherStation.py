# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 10:14:19 2018

@author: 凯风
"""

from WeatherData import WeatherData
from Observers import CurrentConditionsDisplay, ForecastDisplay, StatisticsDisplay

class WeatherStation(object):
    def __init__(self):
        weatherData = WeatherData()
        currentConditionsDisplay = CurrentConditionsDisplay(weatherData)
        forecastDisplay = ForecastDisplay(weatherData)
        statisticsDisplay = StatisticsDisplay(weatherData)
        
        weatherData.setMeasurements(80, 65, 30.4)
        print("\n")
        weatherData.setMeasurements(82, 70, 29.3)
        print("\n")
        weatherData.setMeasurements(78, 90, 26.4)
        


if __name__ == "__main__":
    WeatherStation()