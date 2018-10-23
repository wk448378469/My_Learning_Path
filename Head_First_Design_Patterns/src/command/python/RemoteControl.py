# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 17:02:47 2018

@author: 凯风
"""

from command import NoCommand

class RemoteControl(object):
    def __init__(self):
        self.onCommands = []
        self.offCommands = []
        
        noCommand = NoCommand()
        for i in range(7):
            self.onCommands.append(noCommand)
            self.offCommands.append(noCommand)
        
        self.undoCommand = noCommand
    
    def setCommand(self, slot, onCommand, offCommand):
        self.onCommands[slot] = onCommand
        self.offCommands[slot] = offCommand
    
    def onButtonWasPressed(self, slot):
        self.onCommands[slot].execute()
        self.undoCommand = self.onCommands[slot]
    
    def offButtonWasPushed(self, slot):
        self.offCommands[slot].execute()
        self.undoCommand = self.offCommands[slot]
    
    def undoButtonPushed(self):
        self.undoCommand.undo()

    def __str__(self):
        result = "\n----- Remote Control -----\n"
        for i in range(len(self.onCommands)):
            result += "[slot {0}] {1}        {2}\n".format(i,
                       str(type(self.onCommands[i])), str(type(self.offCommands[i])))
        return result



