# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 16:43:39 2018

@author: 凯风
"""

from executor import CeilingFan
from abc import ABCMeta, abstractmethod

class Command(metaclass = ABCMeta):
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def undo(self):
        pass


class NoCommand(Command):
    def execute(self):
        pass
    def undo(self):
        pass


class MacroCommand(Command):
    def __init__(self, commands):
        self.commands = commands
    
    def execute(self):
        for command in self.commands:
            command.execute()
    
    def undo(self):
        for command in self.commands:
            command.undo()


class CeilingFanHighCommand(Command):
    def __init__(self, ceilingFan):
        self.ceilingFan = ceilingFan
        self.prevSpeed = 0
    
    def execute(self):
        self.prevSpeed = self.ceilingFan.getSpeed()
        self.ceilingFan.high()
    
    def undo(self):
        if (self.prevSpeed == CeilingFan.HIGH):
            self.ceilingFan.high()
        elif (self.prevSpeed == CeilingFan.MEDIUM):
            self.ceilingFan.medium()
        elif (self.prevSpeed == CeilingFan.LOW):
            self.ceilingFan.low()
        elif (self.prevSpeed == CeilingFan.OFF):
            self.ceilingFan.off()


class CeilingFanMediumCommand(Command):
    def __init__(self, ceilingFan):
        self.ceilingFan = ceilingFan
        self.prevSpeed = 0
    
    def execute(self):
        self.prevSpeed = self.ceilingFan.getSpeed()
        self.ceilingFan.medium()
    
    def undo(self):
        if (self.prevSpeed == CeilingFan.HIGH):
            self.ceilingFan.high()
        elif (self.prevSpeed == CeilingFan.MEDIUM):
            self.ceilingFan.medium()
        elif (self.prevSpeed == CeilingFan.LOW):
            self.ceilingFan.low()
        elif (self.prevSpeed == CeilingFan.OFF):
            self.ceilingFan.off()


class CeilingFanLowCommand(Command):
    def __init__(self, ceilingFan):
        self.ceilingFan = ceilingFan
        self.prevSpeed = 0
    
    def execute(self):
        self.prevSpeed = self.ceilingFan.getSpeed()
        self.ceilingFan.low()
    
    def undo(self):
        if (self.prevSpeed == CeilingFan.HIGH):
            self.ceilingFan.high()
        elif (self.prevSpeed == CeilingFan.MEDIUM):
            self.ceilingFan.medium()
        elif (self.prevSpeed == CeilingFan.LOW):
            self.ceilingFan.low()
        elif (self.prevSpeed == CeilingFan.OFF):
            self.ceilingFan.off()


class CeilingFanOffCommand(Command):
    def __init__(self, ceilingFan):
        self.ceilingFan = ceilingFan
        self.prevSpeed = 0
    
    def execute(self):
        self.prevSpeed = self.ceilingFan.getSpeed()
        self.ceilingFan.off()
    
    def undo(self):
        if (self.prevSpeed == CeilingFan.HIGH):
            self.ceilingFan.high()
        elif (self.prevSpeed == CeilingFan.MEDIUM):
            self.ceilingFan.medium()
        elif (self.prevSpeed == CeilingFan.LOW):
            self.ceilingFan.low()
        elif (self.prevSpeed == CeilingFan.OFF):
            self.ceilingFan.off()


class GarageDoorDownCommand(Command):
    def __init__(self, garageDoor):
        self.garageDoor = garageDoor
    
    def execute(self):
        self.garageDoor.down()
    
    def undo(self):
        self.garageDoor.up()
    

class GarageDoorUpCommand(Command):
    def __init__(self, garageDoor):
        self.garageDoor = garageDoor
    
    def execute(self):
        self.garageDoor.up()
    
    def undo(self):
        self.garageDoor.down()
    

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.off()
    
    def undo(self):
        self.light.on()


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.on()
    
    def undo(self):
        self.light.off()


class StereoOffCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo
    
    def execute(self):
        self.stereo.off()
    
    def undo(self):
        self.stereo.on()
        self.stereo.setDVD()
        self.stereo.setVolume(10)

class StereoOnWithCDCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo
    
    def execute(self):
        self.stereo.on()
        self.stereo.setDVD()
        self.stereo.setVolume(10)

    def undo(self):
        self.stereo.off()




