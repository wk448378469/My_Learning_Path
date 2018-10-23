# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 16:28:59 2018

@author: 凯风
"""

class CeilingFan(object):
    HIGH = 3
    MEDIUM = 2
    LOW = 1
    OFF = 0
    
    def __init__(self, location):
        self.location = location
        self.level = self.OFF

    def high(self):
        self.level = self.HIGH
        print(self.location + " ceiling fan is on high")
    
    def medium(self):
        self.level = self.MEDIUM
        print(self.location + " ceiling fan is on medium")
    
    def low(self):
        self.level = self.LOW
        print(self.location + " ceiling fan is on low")
    
    def off(self):
        self.level = self.OFF
        print(self.location + " ceiling fan is off")
    
    def getSpeed(self):
        return self.level
    

class Light(object):
    def __init__(self, location):
        self.location = location
    
    def on(self):
        print(self.location + " light is on")
    
    def off(self):
        print(self.location + " light is off")


class GarageDoor(object):
    def __init__(self, location):
        self.location = location
    
    def up(self):
        print(self.location + " garage door is up")
    
    def down(self):
        print(self.location + " garage door is down")


class Stereo(object):
    def __init__(self, location):
        self.location = location
    
    def on(self):
        print(self.location + "stereo is on")
    
    def off(self):
        print(self.location + "stereo is off")
    
    def setCD(self):
        print(self.location + "stereo is set for CD input")
    
    def setDVD(self):
        print(self.location + "stereo is set for DVD input")
    
    def setVolume(self, volume):
        print(self.location + "stereo volume set to " + str(volume))